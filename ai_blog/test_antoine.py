from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Mock data for demonstration
articles_info = [
    {"number": 1, "title": "Article One", "publication_date": "2024-04-01"},
    {"number": 2, "title": "Article Two", "publication_date": "2024-04-02"},
    # Add more articles as needed
]

def fetch_articles():
    # This is a simplified scraper function for demonstration.
    # You'll replace this URL with the actual page you intend to scrape.
    url = 'https://news.mit.edu/topic/artificial-intelligence'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Find all article titles (this will depend on the site's structure)
    titles = soup.find_all('h3')  # Placeholder tag

    articles_list = [{"number": i+1, "title": title.text.strip(), "publication_date": "Unknown date"} for i, title in enumerate(titles[:5])]
    return articles_list

@app.route('/')
def home():
    return "Welcome to the AI News Overview API!"

@app.route('/get_data', methods=['GET'])
def get_data():
    articles = fetch_articles()
    return jsonify(articles)

@app.route('/articles', methods=['GET'])
def articles():
    return jsonify(articles_info)

@app.route('/article/<int:number>', methods=['GET'])
def article(number):
    article = next((item for item in articles_info if item["number"] == number), None)
    if article:
        return jsonify(article)
    else:
        return jsonify({"error": "Article not found"}), 404

@app.route('/ml', defaults={'number': None})
@app.route('/ml/<int:number>', methods=['GET'])
def ml(number):
    if number is None:
        # Apply ML to all articles (placeholder)
        return jsonify({"message": "ML analysis for all articles"})
    else:
        # Apply ML to a specific article (placeholder)
        return jsonify({"message": f"ML analysis for article {number}"})

if __name__ == '__main__':
    app.run(debug=True)
