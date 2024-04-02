# -*- coding: utf-8 -*-

import requests
from flask import Flask, jsonify, render_template
import feedparser  # We'll use feedparser to parse the XML response

app = Flask(__name__)

ARXIV_API_URL = "http://export.arxiv.org/api/query"

@app.route('/')
def home():
    return 'Welcome to our API!'

@app.route('/page')
def latest_publications():
    params = {
        "search_query": "all:Autoregressive",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": 1
    }
    response = requests.get(ARXIV_API_URL, params=params)
    feed = feedparser.parse(response.content)
    entries = [
            {
                'title': entry.title,
                'authors': [author.name for author in entry.authors],
                'summary': entry.summary,
                'published': entry.published
            }
            for entry in feed.entries
        ]
    return render_template('page.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)

