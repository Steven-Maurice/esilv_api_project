from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
 
app = Flask(__name__)
 
def scrape_articles():
    url = "https://www.artificialintelligence-news.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    articles = []
    for article in soup.find_all("article", class_="post"):
        title = article.find("h2", class_="entry-title").get_text(strip=True)
        link = article.find("a")["href"]
        articles.append({"title": title, "url": link})
    return articles
 
 
@app.route('/articles', methods=['GET'])
def articles():
    articles = scrape_articles()
    return jsonify(articles[:5])
 

@app.route('/article/<number>', methods=['GET'])
def article(number):
    return jsonify({"error": "Endpoint not implemented"})
 
