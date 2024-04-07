from flask import Flask, jsonify, Blueprint, request
import requests

articles_blueprint = Blueprint('articles', __name__)

API_KEY = "9d6a051bb3d44dcbb973b776b33191a6"
BASE_URL = "http://newsapi.org/v2/everything"

cached_articles = []

@articles_blueprint.route('/articles', methods=['GET'])
def get_articles():
    global cached_articles
    query = "Artificial Intelligence" 
    url = f"{BASE_URL}?q={query}&sortBy=publishedAt&language=en&apiKey={API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 

        articles_data = response.json().get('articles', [])
        cached_articles = articles_data[:5] 

        simplified_articles = [
            {
                "number": idx,
                "title": article['title'],
                "publishedAt": article['publishedAt'],
                "source": article['source']['name']
            }
            for idx, article in enumerate(cached_articles)
        ]

        return jsonify(simplified_articles)
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch data", "details": str(e)}), 500

@articles_blueprint.route('/article/<int:number>', methods=['GET'])
def get_article(number):
    if number < 0 or number >= len(cached_articles):
        return jsonify({"error": "Article number out of range"}), 404

    article = cached_articles[number]
    detailed_article = {
        "title": article['title'],
        "publishedAt": article['publishedAt'],
        "source": article['source']['name'],
        "description": article.get('description', 'No description available.'),
        "content": article.get('content', 'Content not available.'),
        "url": article['url'] 
    }

    return jsonify(detailed_article)

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(articles_blueprint, url_prefix='/articles')
    app.run(debug=True)