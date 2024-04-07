from flask import Blueprint, jsonify
from newsapi import NewsApiClient
from flask import Flask
import requests

articles_blueprint = Blueprint('articles', __name__)

#we will use the existing API 'https://newsapi.org' to access articles
#we create the 'get_data' route that sends an API request to retrieve the top 5 most relevant articles (top-headlines)
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