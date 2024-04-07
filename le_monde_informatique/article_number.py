# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 16:00:44 2024

@author: 33623
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

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

app = Flask(__name__)

@app.route('/article/<int:number>')
def article(number):
    articles_data = fetch_articles('https://www.lemondeinformatique.fr/intelligence-artificielle-154.html')
    if number < 1 or number > len(articles_data):
        abort(404)
    article_metadata = articles_data[number - 1]
    article_content = fetch_full_article(article_metadata['link'])
    article_content_with_br = article_content.replace('\n', '<br>')
    article_metadata['content'] = article_content_with_br
    data_json_pretty = json.dumps(article_metadata, ensure_ascii=False, indent=2)
    html_response = f"""
    <html>
    <head>
        <style>
            body {{ 
                display: flex;
                justify-content: center;
                margin: 0;
                padding: 0;
                height: 100vh;
                align-items: center;
            }}
            pre {{
                width: 80%; /* Limite la largeur à 80% de la largeur de l'écran */
                margin: auto;
                white-space: pre-wrap; /* Permet aux mots de passer à la ligne selon la largeur */
                word-wrap: break-word; /* Assure la césure des mots si nécessaire */
                background-color: #f5f5f5; /* Couleur de fond légère pour le <pre> */
                padding: 20px;
                border-radius: 10px; /* Bords arrondis pour le <pre> */
                box-shadow: 0 0 10px rgba(0,0,0,0.1); /* Ombre subtile pour le <pre> */
            }}
        </style>
    </head>
    <body>
        <pre>{data_json_pretty}</pre>
    </body>
    </html>
    """

    response = make_response(html_response)
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response


if __name__ == '__main__':
 #   test_url = 'https://www.lemondeinformatique.fr/actualites/lire-des-llm-en-local-avec-opera-one-developer-93409.html'
 #   fetch_full_article(test_url)
    app.run(debug=False)
