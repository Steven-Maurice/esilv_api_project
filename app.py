# -*- coding: utf-8 -*-

from flask import Flask, render_template
import requests
import feedparser

app = Flask(__name__)

ARXIV_API_URL = "http://export.arxiv.org/api/query"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search/last')
def latest_publication():
    params = {
        "search_query": "e",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": 5 
    }
    response = requests.get(ARXIV_API_URL, params=params)
    feed = feedparser.parse(response.content)

    if not feed.entries:
        return render_template('page.html', entries=None, message="Aucune publication récente trouvée.")

    publications = []
    for entry in feed.entries:
        authors = [author.name for author in entry.authors] if entry.authors else 'Anonymous'
        publication = {
            'title': entry.title,
            'authors': authors,
            'summary': entry.summary,
            'published': entry.published
        }
        publications.append(publication)

    return render_template('page.html', entries=publications)



@app.route('/search/last/<theme>')
def latest_publication_by_theme(theme):
    params = {
        "search_query": f"all:{theme}",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": 5  
    }
    response = requests.get(ARXIV_API_URL, params=params)
    feed = feedparser.parse(response.content)
    if not feed.entries:
        return render_template('page.html', entries=[], message="Aucune publication récente trouvée pour le thème spécifié.")
    
    entries = [{
        'title': entry.get('title', 'Pas de titre'),
        'authors': ', '.join(author.name for author in entry.authors),
        'summary': entry.get('summary', 'Pas de résumé'),
        'published': entry.get('published', 'Date de publication inconnue')
    } for entry in feed.entries]
    
    return render_template('page.html', entries=entries)



if __name__ == '__main__':
    app.run(debug=True)

