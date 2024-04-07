#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 16:12:23 2024

@author: arthur
"""

from flask import Flask, jsonify
from scraping import fetch_articles
from feelings_analysis import FeelingsAnalysis


# Initialisation de l'application Flask
app = Flask(__name__)

@app.route('/get_data')
def get_data():
    articles = fetch_articles()[:5]
    return jsonify(articles)




@app.route('/articles')
def articles():
    # Afficher les informations requises des articles
    articles_info = [{'number': idx+1, 'title': article['title'], 'url': article['url'], 'publication_date': article['publication_date']} for idx, article in enumerate(fetch_articles())]
    return jsonify(articles_info)

@app.route('/article/<int:number>')
def article(number):
    # Accéder au contenu d'un article spécifié par son numéro
    all_articles = fetch_articles()
    if 0 < number < len(all_articles):
        article_content = {
            'title': all_articles[number]['title'],
            'summary': all_articles[number]['summary'],
            'url': all_articles[number]['url']
        }
        return jsonify(article_content)
    return jsonify({'error': 'Article not found'}), 404


@app.route('/ml/<int:number>')
def sentiment(number=None):
    all_articles = fetch_articles()
    if number is not None and 0 <= number < len(all_articles):
        article = all_articles[number]
        sentiment = FeelingsAnalysis(article['title'])
        return jsonify({'number': number, 'sentiment': sentiment})
    return jsonify({'error': 'Article not found'}), 404



# Route principale
@app.route('/')
def index():
    return 'Hello, World!'

# Point d'entrée principal
if __name__ == '__main__':
    app.run(debug=True)