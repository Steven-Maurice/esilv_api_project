# -*- coding: utf-8 -*-

from flask import Flask, request, Response, render_template, redirect, url_for, flash
import requests
import feedparser
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import nltk

nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

app = Flask(__name__)

ARXIV_API_URL = "http://export.arxiv.org/api/query"

app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search')
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

    params = {
        "search_query": search_query,
        "start": start, 
        "max_results": max_results,
        "sortBy": sortBy, 
        "sortOrder": sortOrder
        
 
    }
    response = requests.get(ARXIV_API_URL, params=params)
    feed = feedparser.parse(response.content)

    if not feed.entries:
        return render_template('search.html', entries=[], message="No results found.")

    entries = []
    for entry in feed.entries:

        published_date = entry.published.replace('T', ' ').replace('Z', '')

        sentiment = sid.polarity_scores(entry.summary)
        sentiment_class = 'Neutral'
        if sentiment['compound'] >= 0.05:
            sentiment_class = 'Positive'
        elif sentiment['compound'] <= -0.05:
            sentiment_class = 'Negative'

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
        return redirect(url_for('search'))  
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
            return redirect(url_for('search'))
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



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


