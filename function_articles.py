
from flask import Flask, jsonify, Blueprint


articles = Blueprint('articles', __name__)

@articles.route('/articles', methods=['GET'])
def get_articles():
    api_url = "http://eventregistry.org/api/v1/article/getArticles"
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
        "articlesSortBy": "date",
        "articlesCount": 5,
        "includeArticleBody": False,
        "includeArticleLocation": True,
        "includeArticleImage":False,
        "includeArticleEventUri": False,
        "apiKey": "36f9340a-b5b7-42dd-bac1-00296478472e"
    }

    response = requests.post(api_url, json=query_payload, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code



article = Blueprint('article', __name__)


#The number is uri number of the article
@article.route('/article/<number>', methods=['GET'])
def get_article(number):
    api_url = "http://eventregistry.org/api/v1/article/getArticle"
    params = {
        "action": "getArticle",
        "articleUri": number,
        "infoArticleBodyLen": -1,
        "resultType": "info",
        "apiKey": "36f9340a-b5b7-42dd-bac1-00296478472e"
    }

    response = requests.post(api_url, json=params)

    if response.status_code == 200:

        return jsonify(response.json())
    else:

        return jsonify({"error": "Failed to fetch article content"}), response.status_code
