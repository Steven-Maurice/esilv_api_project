from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from transformers import pipeline

app = Flask(__name__)

@app.route('/get_data')
def get_data():
    response = requests.get('https://www.forbes.com/ai/')
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article', limit=5)

    data = []
    for i, article in enumerate(articles):
        title = article.find('h2').text
        date = article.find('time')['datetime']
        data.append({'number': i+1, 'title': title, 'date': date})

    return jsonify(data)

@app.route('/articles')
def articles():
    response = requests.get('https://www.forbes.com/ai/')
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')

    data = []
    for i, article in enumerate(articles):
        title = article.find('h2').text
        date = article.find('time')['datetime']
        data.append({'number': i+1, 'title': title, 'date': date})

    return jsonify(data)

@app.route('/article/<int:number>')
def article(number):
    response = requests.get('https://www.forbes.com/ai/')
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')

    if number <= 0 or number > len(articles):
        return jsonify({'error': 'Article number out of range'}), 404

    article = articles[number-1]
    title = article.find('h2').text
    date = article.find('time')['datetime']
    content = article.find('div', class_='article-body').text

    return jsonify({'number': number, 'title': title, 'date': date, 'content': content})

@app.route('/ml')
def ml():
    response = requests.get('https://www.forbes.com/ai/')
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')

    data = []
    sentiment_analyzer = pipeline('sentiment-analysis')

    for i, article in enumerate(articles):
        title = article.find('h2').text
        date = article.find('time')['datetime']
        content = article.find('div', class_='article-body').text

        sentiment = sentiment_analyzer(content)[0]['label']
        data.append({'number': i+1, 'title': title, 'date': date, 'sentiment': sentiment})

    return jsonify(data)

@app.route('/ml/<int:number>')
def ml_number(number):
    # Implement your machine learning script here
    pass

if __name__ == '__main__':
    app.run(debug=True)