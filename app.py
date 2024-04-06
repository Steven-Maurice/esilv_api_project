# -*- coding: utf-8 -*-

from flask import Flask, request, Response, render_template, redirect, url_for, flash, jsonify
import requests
import feedparser
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import nltk
from bs4 import BeautifulSoup

nltk.download('vader_lexicon')

app = Flask(__name__)

ARXIV_API_URL = "http://export.arxiv.org/api/query"

app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

def fetch_arxiv_data(search_query, start=0, max_results=10, sortBy='submittedDate', sortOrder='descending'):
    params = {
        "search_query": search_query,
        "start": start, 
        "max_results": max_results,
        "sortBy": sortBy, 
        "sortOrder": sortOrder
    }
    response = requests.get(ARXIV_API_URL, params=params)
    return feedparser.parse(response.content)

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_result = sia.polarity_scores(text)
    if sentiment_result['compound'] >= 0.05:
        return sentiment_result,'Positive'
    elif sentiment_result['compound'] <= -0.05:
        return sentiment_result,'Negative'
    else:
        return sentiment_result,'Neutral'




@app.route('/about')
@login_required
def about():
    return render_template('about.html')

@app.route('/search')
@login_required
def search():
    query = request.args.get('query', '')
    author = request.args.get('author', '')
    start = request.args.get('start', '0')
    max_results = request.args.get('max_results', '10')
    sortBy = request.args.get('sortBy', 'lastUpdatedDate')
    sortOrder = request.args.get('sortOrder', 'descending')  

    if author:
        search_query = f"all:{query} AND au:{author}" if query else f"all:e AND au:{author}"
    else:
        search_query = f"all:{query}" if query else "all:e"

    feed = fetch_arxiv_data(search_query, start, max_results, sortBy, sortOrder)

    if not feed.entries:
        return render_template('search.html', entries=[], message="No results found.")

    entries = []
    for entry in feed.entries:

        published_date = entry.published.replace('T', ' ').replace('Z', '')

        _,sentiment_class = analyze_sentiment(entry.summary)

        authors = [author.name for author in entry.authors] if entry.authors else 'Anonymous'
        entry_data = {
            'title': entry.title,
            'authors': ', '.join(authors),
            'summary': entry.summary,
            'published': published_date,
            'link': entry.link,
            'sentiment': sentiment_class,
            'arxiv_id': entry.id.split('/abs/')[-1] 
        }
        entries.append(entry_data)

    return render_template('search.html', entries=entries)

@app.route('/download/pdf/<paper_id>')
@login_required
def download_pdf(paper_id):
    pdf_url = f"https://arxiv.org/pdf/{paper_id}.pdf"
    response = requests.get(pdf_url)
    if response.status_code == 200:
        return Response(
            response.content,
            mimetype='application/pdf',
            headers={"Content-Disposition": f"attachment;filename={paper_id}.pdf"}
        )
    else:
        return f"Error downloading PDF: Status {response.status_code}", 500




class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @property
    def is_admin(self):
        return self.email in admins_list

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if User.query.filter_by(email=email).first():
            flash('Email already exists.')
            return redirect(url_for('signup'))
        new_user = User(email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)  
        return redirect(url_for('about'))  
    return render_template('signup.html')

admins_list = {
    'admin@gmail.com': 'admin'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            if email in admins_list:
                return redirect(url_for('dashboard'))
            return redirect(url_for('about'))
        else:
            flash('Invalid email or password')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
            flash("Accès non autorisé : vous devez être administrateur.")
            return redirect(url_for('about'))
    users = User.query.all()  
    return render_template('dashboard.html', users=users) 

@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user.email = email
        if password:  
            user.set_password(password)
        db.session.commit()
        flash('User updated successfully.')
        return redirect(url_for('dashboard'))
    return render_template('edit_user.html', user=user)


@app.route('/delete_user/<int:user_id>')
@login_required
def delete_user(user_id):
    user_to_delete = User.query.get_or_404(user_id)
    db.session.delete(user_to_delete)
    db.session.commit()
    flash('User has been deleted.')
    return redirect(url_for('dashboard'))

@app.route('/add_user', methods=['POST'])
@login_required
def add_user():
    email = request.form['email']
    password = request.form['password']
    existing_user = User.query.filter_by(email=email).first()
    if existing_user is not None:
        flash('Email is already in use.')
        return redirect(url_for('dashboard'))
    
    new_user = User(email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    flash('New user added successfully.')
    return redirect(url_for('dashboard'))


def scrape_article_details(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    if response.status_code != 200:
            return jsonify({'error': 'Article not found or failed to load'}), response.status_code
    
    title = soup.find('h1', class_='title').text.replace("Title:", "").strip()
    summary = soup.find('blockquote', class_='abstract').text.replace("Abstract:", "").strip()
    authors = [tag.text.strip() for tag in soup.find_all('div', class_='authors')]
    published_date = soup.find('div', class_='dateline').text
    link = article_url

    return {
        'title': title,
        'summary': summary,
        'authors': authors,
        'published_date': published_date,
        'link': link
    }



@app.route('/get_data/', defaults={'topic': 'AI'})
@app.route('/get_data/<topic>')
@login_required
def get_article_ids(topic):
    search_query = f'all:{topic}'
    feed = fetch_arxiv_data(search_query)
    articles_data = []
    for entry in feed.entries:
        arxiv_id = entry.id.split('/abs/')[-1]
        article_url = f'https://arxiv.org/abs/{arxiv_id}'
        article_details = scrape_article_details(article_url)

        articles_data.append({
            'id': arxiv_id,
            'title': article_details['title']
        })
    
    return jsonify(articles_data), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/articles')
@login_required
def articles():
    topic = 'AI'  
    search_query = f'all:{topic}'
    feed = fetch_arxiv_data(search_query)
    articles_data = []
    for entry in feed.entries:
        arxiv_id = entry.id.split('/abs/')[-1]
        article_url = f'https://arxiv.org/abs/{arxiv_id}'
        article_details = scrape_article_details(article_url)
    
        articles_data.append({
            'title': article_details['title'],
            'authors': article_details['authors'],
            'published': article_details['published_date'],
            'link': article_details['link'],
            'id': arxiv_id
        })

    return jsonify(articles_data), 200, {'Content-Type': 'application/json; charset=utf-8'}


@app.route('/article/', defaults={'number': '2404.03624v1'})
@app.route('/article/<number>')
@login_required
def article(number):
     
    article_url = f'https://arxiv.org/abs/{number}'
    article_details = scrape_article_details(article_url)
    
    article_data = []

    article_data.append({
        'title': article_details['title'],
        'authors': article_details['authors'],
        'summary': article_details['summary'],
        'published_date': article_details['published_date'],
        'link': article_details['link'],
        'id': number,
    })

    return jsonify(article_data), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/ml/', defaults={'article_id': '2404.03624v1'})
@app.route('/ml/<article_id>')
@login_required
def ml_sentiment_analysis(article_id):
    article_url = f'https://arxiv.org/abs/{article_id}'
    response = requests.get(article_url)

    if response.status_code != 200:
        return jsonify({'error': 'Article not found or failed to load'}), response.status_code

    soup = BeautifulSoup(response.content, 'html.parser')

    summary = soup.find('blockquote', class_='abstract').text.replace("Abstract:", "").strip()
    
    sentiment_result,sentiment_estimation = analyze_sentiment(summary)


    result = {
        'arxiv_id': article_id,
        'title': soup.find('h1', class_='title').text.replace("Title:", "").strip(), 
        'sentiment': {
            'compound_average': sentiment_result,  
            'estimation': sentiment_estimation
        }
    }

    return jsonify(result), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/endpoints')
@login_required
def endpoints():
    return render_template('endpoints.html')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


