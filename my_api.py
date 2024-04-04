# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:34:54 2024

@author: danie
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/get_data")
def get_data():
    return "Fetching data"

@app.route("/articles")
def get_articles():
    return "Infos about articles"


@app.route("/articles/<number>")
def get_content(number):
    return "Content of an article"


if __name__ == "__main__":
    app.run(debug=True)