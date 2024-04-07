import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
from flask import Flask, jsonify, abort, make_response
from textblob import TextBlob


def fetch_articles(url):
    articles_list = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article', class_='item', limit=5)

    for article in articles:
        title = article.find('h2').text if article.find('h2') else article.find('a').text
        link = article.find('a')['href'] if article.find('a') else ''
        summary = article.find('p').text if article.find('p') else 'No summary available'
        date_str = article.find('span', class_='theme').b.text if article.find('span', class_='theme') else 'No date'
        

        articles_list.append({
            'title': title.strip(),
            'link': link.strip(),
            'summary': summary.strip(),
            'publication_date': date_str.strip(),
        })

    return articles_list

def fetch_full_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content_div = soup.find('div', class_='article-body')
    if content_div:
        content_text = content_div.text.strip()
    else:
        content_text = "Content not found"
    
    return content_text

def convert_newlines(content):
    """Convertit les sauts de ligne en balises <br> pour l'affichage HTML."""
    return content.replace('\n', '<br>')


from flask import Flask, jsonify, abort, make_response


def analyze_sentiment(text):
    """Perform sentiment analysis on the provided text."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

app = Flask(__name__)

@app.route('/ml', methods=['GET'])
@app.route('/ml/<int:number>', methods=['GET'])
def ml(number=None):
    articles_data = fetch_articles('https://www.lemondeinformatique.fr/intelligence-artificielle-154.html')
    if number:
        if number < 1 or number > len(articles_data):
            abort(404)
        articles_data = [articles_data[number - 1]]
    for article in articles_data:
        content = fetch_full_article(article['link'])
        sentiment = analyze_sentiment(content)
        article['sentiment'] = sentiment

    return jsonify(articles_data)


if __name__ == '__main__':
 #   test_url = 'https://www.lemondeinformatique.fr/actualites/lire-des-llm-en-local-avec-opera-one-developer-93409.html'
 #   fetch_full_article(test_url)
    app.run(debug=False)

