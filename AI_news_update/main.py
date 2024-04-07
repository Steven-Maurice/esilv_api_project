from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the AI News API!'})

@app.route('/get_data')
def get_data():
    url = 'https://openai.com/blog/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    articles = []
    for i, article in enumerate(soup.find_all('h3', {'class': 'f-subhead-2'})):
        title = article.text
        formatted_title = re.sub(r'[^\w\s-]', '', title.lower()).replace(' ', '-')
        article_url = f"{url}{formatted_title}"
        a = article.find('a')
        if a is not None:
            article_url = a['href']
        articles.append({'number': i, 'title': title, 'link': article_url})

    return jsonify(articles)

@app.route('/articles') 
def articles(): 
    articles_data = get_data().get_json()  
    full_articles = []
    for article in articles_data:
        article_url = article["link"]

        response = requests.get(article_url)
        if response.status_code == 200:
            article_soup = BeautifulSoup(response.text, 'html.parser')
            title_element = article_soup.find('h1', class_='f-display-2 text-balance')
            if title_element:
                title=title_element.text
            else:
                title_element = article_soup.find('h1', class_='f-display-2 text-balance md:pr-40 lg:pr-44')
                if title_element:
                    title=title_element.text
                else: 
                    title='Titre inconnu'
            
            author_element = article_soup.find('h4', class_='f-subhead-2')
            author = author_element.text if author_element else 'Auteur inconnu'
            date_element = article_soup.find('span', class_='f-meta-2')
            date = date_element.text if date_element else 'Date inconnu'

            categories_elements = article_soup.find_all('span', class_='underline-thickness-1 underline-offset-4 underline')
            categories = ', '.join([elem.text for elem in categories_elements if elem.text != "OpenAI " and elem.text != "View all articles"])
            full_articles.append({
                'number':article['number'],
                'title': title,
                'author': author,
                'date': date,
                'categories': categories,
                'link': article_url
            })
        else:
            print(f"Failed to retrieve {article_url}")

    return jsonify(full_articles)

@app.route('/ml', methods=['GET'])
def analyze_all_articles_sentiment():
    articles = get_data().get_json()
    results = []
    
    for article in articles:
        article_content = fetch_article_content(article['link'])
        sentiment_score = sia.polarity_scores(article_content)
        results.append({
            'number': article['number'],
            'title': article['title'],
            'sentiment': sentiment_score
        })
    
    return jsonify(results)

@app.route('/ml/<int:number>', methods=['GET'])
def analyze_single_article_sentiment(number):
    articles = get_data().get_json()
    if number < 1 or number > len(articles):
        return jsonify({'error': 'Article number out of range'}), 404
    
    article = articles[number - 1]
    article_content = fetch_article_content(article['link'])
    sentiment_score = sia.polarity_scores(article_content)
    
    return jsonify({
        'number': article['number'],
        'title': article['title'],
        'sentiment': sentiment_score
    })

def fetch_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = ' '.join(p.text for p in soup.find_all('p'))
    return content

sia = SentimentIntensityAnalyzer()

if __name__ == '__main__':
    app.run(debug=True)

