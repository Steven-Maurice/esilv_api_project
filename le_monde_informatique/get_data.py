# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:12:30 2024

@author: 33623
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime

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


from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/articles')
def articles():
    articles_data = fetch_articles('https://www.lemondeinformatique.fr/intelligence-artificielle-154.html')
    articles_metadata = [
        {
            'number': idx,
            'title': article['title'],
            'link': article['link'],
            'publication_date': article['publication_date'],
        }
        for idx, article in enumerate(articles_data, 1)  
    ]
    return jsonify(articles_metadata)

if __name__ == '__main__':
    app.run(debug=True)

