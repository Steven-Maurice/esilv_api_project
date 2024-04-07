from flask import Blueprint, jsonify
from newsapi import NewsApiClient
from flask import Flask
import requests

articles_blueprint = Blueprint('articles', __name__)

#we will use the existing API 'https://newsapi.org' to access articles
#we create the 'get_data' endpoint that sends an API request to retrieve the top 5 most relevant articles (top-headlines)
@articles_blueprint.route('/get_data', methods=['GET'])
def get_data():
    """
    Retrieves data from the News API.

    Returns:
        dict: JSON response containing the retrieved data.
    """
    url = ('https://newsapi.org/v2/top-headlines?'
           'q=Artificial Intelligence&'
           'pageSize=5&'
           'apiKey=2dc9629039304cbd8d0a69e75a3509ee')
    
    #we send the get request to the API
    response = requests.get(url)
    data = response.json()
    return jsonify(data)


#we create the 'articles' endpoint that provides information about the articles such as the article number, title, and publication date, but not the content
@articles_blueprint.route('/articles', methods=['GET'])
def articles():
    """
    Retrieves information about articles from the News API.

    Returns:
        dict: JSON response containing information about articles.
    """
    url = ('https://newsapi.org/v2/top-headlines?'
            'q=Artificial Intelligence&'
            'pageSize=5&'
            'apiKey=2dc9629039304cbd8d0a69e75a3509ee')
    
    #we send the get request to the API
    response = requests.get(url)
    data = response.json()
    articles_data = data['articles']

    #we simplify the articles data
    simplified_articles = [
        {
            'article_number': idx + 1,
            'title': article['title'],
            'publication_date': article['publishedAt'],
            'description': article['description'],
            'author': article.get('author'),
            'source_name': article['source']['name'],
            'url': article['url']
        }
        for idx, article in enumerate(articles_data)
    ]
    return jsonify(simplified_articles)