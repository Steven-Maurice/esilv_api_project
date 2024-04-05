from flask import Flask, jsonify, Blueprint
from eventregistry import *


get_data = Blueprint('get_data', __name__)


#Get only the articles titles
@get_data.route('/get_data', methods=['GET'])
def getdata():
    url = "http://eventregistry.org/api/v1/article/getArticles"
    headers = {'Content-Type': 'application/json'}
    query_payload = {
        "query": {
            "$query": {
                "$and": [
                    {"conceptUri": "http://en.wikipedia.org/wiki/Artificial_intelligence"},
                    {"categoryUri": "dmoz/Computers/Artificial_Intelligence"},
                    {"lang": "eng"}
                ]
            },
            "$filter": {
                "forceMaxDataTimeWindow": "31",
                "startSourceRankPercentile": 80,
                "endSourceRankPercentile": 100
            }
        },
        "resultType": "articles",
        "articlesSortBy": "rel",
        "articlesCount": 5,
        "includeArticleBasicInfo": False,
        "includeArticleBody": False,
        "includeArticleEventUri": False,
        "includeArticleImage":False,
        "apiKey": "36f9340a-b5b7-42dd-bac1-00296478472e"
    }
    response = requests.post(url, json=query_payload, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code
