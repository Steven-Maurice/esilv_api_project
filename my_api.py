# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:34:54 2024

@author: danie
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

#liste d'infos et d'articles
articles = [
    {"article number": "1", "title": "Article 1", "publication date": "2024-01-01", "content": "Content of Article 1"},
    {"article number": "2", "title": "Article 2", "publication date": "2024-01-02", "content": "Content of Article 2"}
    # Add more articles here
]

def recup_articles():
    return 0




@app.route("/")
def home():
    return "Home"

@app.route("/get_data")
def get_data():
    return "Fetching data"

@app.route("/articles")
def get_articles():
    article_data = {
        "article number": "12",
        "title" : "Niehehe",
        "publication date" : "hier",
        "Author" : "Dada"
    }
    return jsonify(article_data)


@app.route("/articles/<number>")
def get_content(number):
    return "Content of an article"


if __name__ == "__main__":
    app.run(debug=True)