from flask import Flask, jsonify, Blueprint



ml_positive = Blueprint('ml_positive', __name__)


#We only get the articles with a positive score of sentiment analysis
@ml_positive.route('/ml_positive', methods=['GET'])
def get_ml_positive():
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
                "endSourceRankPercentile": 100,
                "minSentiment": 0.1,
                "maxSentiment": 1
            }
        },
        "resultType": "articles",
        "articlesSortBy": "date",
        "articlesCount": 5,
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

ml_negative = Blueprint('ml_p', __name__)

#We only get the articles with a negative score of sentiment analysis

@ml_negative.route('/ml_negative', methods=['GET'])
def get_ml_negative():
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
                "endSourceRankPercentile": 100,
                "minSentiment": -1,
                "maxSentiment": -0.1
            }
        },
        "resultType": "articles",
        "articlesSortBy": "date",
        "articlesCount": 5,
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