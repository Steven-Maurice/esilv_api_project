# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:58:21 2024

@author: mariu
"""

from flask import Flask, jsonify, request
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

API_KEY = '36afffa8669d4a44ae8844be637803cb'
BASE_URL = 'https://newsapi.org/v2/everything'


analyzer = SentimentIntensityAnalyzer()

# Un dictionnaire pour stocker les articles récupérés
articles_data = {}

def fetch_articles():
    """Récupère les articles depuis NewsAPI."""
    params = {
        'q': 'intelligence artificielle',
        'pageSize': 5, # Choisir le nombre d'articles que l'on veut
        'apiKey': API_KEY,
        'language': 'fr'  # Choisir la langue des articles
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        for idx, article in enumerate(articles, start=1):
            articles_data[idx] = {
                'Titre': article['title'],
                'Date': article['publishedAt'],
                'Lien': article['url'],
                'Contenu': article['content'],
                'Auteur': article['author']
            }
    else:
        print("Erreur lors de la récupération des articles.")

@app.route('/get_data', methods=['GET'])
def get_data():
    fetch_articles()
    return jsonify(list(articles_data.values()))

@app.route('/articles', methods=['GET'])
def list_articles():
    summary = [{key: val for key, val in value.items() if key != 'Contenu'} for value in articles_data.values()]
    return jsonify(summary)

@app.route('/article/<int:number>', methods=['GET'])
def get_article(number):
    article = articles_data.get(number)
    if article:
        return jsonify(article)
    else:
        return jsonify({"error": "Article non trouvé"}), 404

@app.route('/ml', methods=['GET'])
def ml_all():
    result = {}
    for number, article in articles_data.items():
        # Analyse du sentiment de l'article
        sentiment = analyze_sentiment(article['Contenu'])
        result[number] = {
            'Titre': article['Titre'],
            'Sentiment': sentiment
        }
    return jsonify(result)

@app.route('/ml/<int:number>', methods=['GET'])
def ml_single(number):
    article = articles_data.get(number)
    if article:
        # Analyse du sentiment de l'article
        sentiment = analyze_sentiment(article['Contenu'])
        return jsonify({
            'Titre': article['Titre'],
            'Sentiment': sentiment
        })
    else:
        return jsonify({"error": "Article non trouvé"}), 404

def analyze_sentiment(text):
    """Analyse le sentiment du texte."""
    score = analyzer.polarity_scores(text)
    if score['compound'] >= 0.05:
        return 'Positif'
    elif score['compound'] <= -0.05:
        return 'Negatif'
    else:
        return 'Neutre'

if __name__ == '__main__':
    app.run(debug=True)

    
    


