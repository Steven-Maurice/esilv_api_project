from flask import Flask
import json
from collections import Counter
from scraping import scrape
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/get_data')
def get_data():
    scrape()
    return 'Scrapping is complete'

@app.route('/nb_articles')  
def get_nb_articles():
    
    with open('articles.json') as json_file:
        data = json.load(json_file)
    
    return {'Number of articles': len(data)}

@app.route('/scraped_data')
def get_scraped_data():
    with open('articles.json') as json_file:
        data = json.load(json_file)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run()
