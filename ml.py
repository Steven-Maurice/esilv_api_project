from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
 
app = Flask(__name__)
 
def scrape_articles():
    url = "https://www.artificialintelligence-news.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    articles = []
    # Example: Find article containers - Adjust the selector as needed
    for article in soup.find_all("article", class_="post"):
        title = article.find("h2", class_="entry-title").get_text(strip=True)
        link = article.find("a")["href"]
        articles.append({"title": title, "url": link})
    return articles

@app.route('/ml', defaults={'number': None}, methods=['GET'])
@app.route('/ml/<number>', methods=['GET'])
def ml(number):
    return jsonify({"error": "ML Endpoint not implemented"})