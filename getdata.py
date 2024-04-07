from flask import Flask, jsonify, Blueprint
import requests

get_data = Blueprint('get_data', __name__)

@get_data.route('/get_data', methods=['GET'])
def getdata():
    api_key = "9d6a051bb3d44dcbb973b776b33191a6"
    url = "http://newsapi.org/v2/everything?q=Artificial%20Intelligence&sortBy=publishedAt&language=en&apiKey=" + api_key
    
    try:
        response = requests.get(url)
        response.raise_for_status()  

        articles = response.json().get('articles', [])
        simplified_articles = [
            {
                "title": article['title'],
                "publishedAt": article['publishedAt'],
                "source": article['source']['name'],
                "url": article['url']
            }
            for article in articles[:5]  
        ]

        return jsonify(simplified_articles)
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch data", "details": str(e)}), 500

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(get_data)
    app.run(debug=True)