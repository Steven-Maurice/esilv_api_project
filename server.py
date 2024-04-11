from flask import Flask, jsonify, request
from scraper import get_articles, get_content
from ml import analyze_sentiment, summarize_article
import re


app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the OpenAI Blog API!'

@app.route('/get_data')
def get_data():
    base_url = 'https://openai.com/blog/'
    articles = get_articles(base_url)
    return jsonify(articles)

@app.route('/articles')
def articles():
    base_url = 'https://openai.com/blog/'
    articles_data = get_articles(base_url)  # Directly using the scraping function to get data

    articles_summary = []

    # Regular expression to match the date pattern "Month day, Year"
    date_pattern = re.compile(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2},\s\d{4}')

    for i, article in enumerate(articles_data):
        # Extract the title and URL from the article data
        title_with_date = article[0]
        url = article[1]

        # Use regex to find the publication date within the title
        date_match = date_pattern.search(title_with_date)
        if date_match:
            # Extract the publication date from the matched pattern
            publication_date = date_match.group()
            # Remove the publication date from the title
            title = title_with_date.replace(publication_date, '').strip()
        else:
            # If no date is found, handle accordingly
            publication_date = 'Unknown date'
            title = title_with_date.strip()  # Use the original string as title

        articles_summary.append({
            'number': i + 1,
            'title': title,
            'publication_date': publication_date,
            'url': url
        })

    return jsonify(articles_summary)

@app.route('/article/<int:number>')
def article(number):
    articles_data = get_articles('https://openai.com/blog/')
    
    # Check if the requested article number is within the range of available articles
    if number < 1 or number >= len(articles_data):
        return jsonify({'error': 'Article number out of range'}), 404
    
    # Get the article data tuple by index
    article_tuple = articles_data[number - 1]
    
    # Extract the title_with_date and url from the tuple
    title_with_date, article_url = article_tuple
        
    # Get the content of the article using the URL
    article_content = get_content(article_url)
    
    return jsonify({
        'number': number,
        'title': title_with_date,  
        'content': article_content
    })

@app.route('/ml/<int:number>')
def ml(number):
    articles_data = get_articles('https://openai.com/blog/')
    if number < 1 or number > len(articles_data):
        return jsonify({'error': 'Article number out of range'}), 404

    article_url = articles_data[number - 1][1]
    content = get_content(article_url)

    # If the content could not be retrieved, handle the error
    if not content:
        return jsonify({'error': 'Failed to retrieve content'}), 500

    # Perform sentiment analysis
    sentiment = analyze_sentiment(content)

    # Perform summarization
    summary = summarize_article(article_url)

    # Return both sentiment and summary in the JSON response
    if summary:
        return jsonify({
            'number': number,
            'sentiment': sentiment,
            'summary': summary
        })
    else:
        return jsonify({'error': 'Failed to summarize the article'}), 500
    

if __name__ == '__main__':
    app.run()
