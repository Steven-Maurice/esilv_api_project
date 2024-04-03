print("Hello world")

# 1. _getdata

# Rainie0000: Yufei
from flask import Flask, jsonify
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

def retrieve_articles():
    url = 'http://export.arxiv.org/api/query?search_query=cat:cs.CV&max_results=5'
    response = requests.get(url)
    response_xml = ET.fromstring(response.content)

    articles = []
    for entry in response_xml.iter('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        author = entry.find('{http://www.w3.org/2005/Atom}author/{http://www.w3.org/2005/Atom}name').text
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text

        article = {
            'title': title,
            'author': author,
            'summary': summary
        }
        articles.append(article)

    return articles

@app.route('/get_data')
def get_data():
    articles = retrieve_articles()

    # Récupérez les 5 premiers articles
    five_articles = articles[:5]

    # Retournez les articles en tant que réponse JSON
    return jsonify(five_articles)

if __name__ == '__main__':
    app.run()
    
    