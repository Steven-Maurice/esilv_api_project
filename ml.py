from flask import Flask, jsonify, Blueprint
from textblob import TextBlob
import requests

ml_blueprint = Blueprint('ml', __name__)

cached_articles = []

@ml_blueprint.route('/ml', methods=['GET'])
def get_articles_sentiment():
    sentiments = []
    for article in cached_articles:
        analysis = TextBlob(article.get('content', '') or article.get('description', ''))
        sentiment = analysis.sentiment.polarity  # -1 (negative) to 1 (positive)
        sentiments.append({
            "title": article['title'],
            "sentiment": "positive" if sentiment > 0 else "negative",
            "polarity": sentiment
        })
    return jsonify(sentiments)

@ml_blueprint.route('/ml/<int:number>', methods=['GET'])
def get_article_sentiment(number):
    if number < 0 or number >= len(cached_articles):
        return jsonify({"error": "Article number out of range"}), 404
    
    article = cached_articles[number]
    analysis = TextBlob(article.get('content', '') or article.get('description', ''))
    sentiment = analysis.sentiment.polarity  # -1 (negative) to 1 (positive)
    detailed_sentiment = {
        "title": article['title'],
        "sentiment": "positive" if sentiment > 0 else "negative",
        "polarity": sentiment
    }

    return jsonify(detailed_sentiment)

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(ml_blueprint, url_prefix='/ml')
    app.run(debug=True)