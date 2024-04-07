from flask import Flask, jsonify
from scraper import fetch_articles
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

BLOG_URL = 'https://openai.com/blog'

@app.route('/get_data')
def get_data():
    fetch_articles(BLOG_URL)  
    return jsonify({"message": "Data successfully scraped from OpenAI Blog"})

@app.route('/articles')
def articles():
    return jsonify(fetch_articles(BLOG_URL))

@app.route('/article/<int:number>')
def article(number):
    articles = fetch_articles(BLOG_URL)
    try:
        return jsonify(articles[number])
    except IndexError:
        return jsonify({'error': 'Article not found'}), 404

@app.route('/ml/', defaults={'number': None})
@app.route('/ml/<int:number>')
def ml(number):
    articles = fetch_articles(BLOG_URL)
    if number is not None:
        try:
            article = articles[number]
            sentiment = analyze_sentiment(article['title'])
            return jsonify({'number': number, 'sentiment': sentiment})
        except IndexError:
            return jsonify({'error': 'Article not found'}), 404
    else:
        sentiments = {idx: analyze_sentiment(article['title']) for idx, article in enumerate(articles)}
        return jsonify({'all_articles_sentiment': sentiments})

@app.route('/')
def index():
    return 'Welcome to the OpenAI Blog API!'

if __name__ == '__main__':
    app.run(debug=True)
