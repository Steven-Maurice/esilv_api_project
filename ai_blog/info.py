from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_mit_news():
    try:
        url = "https://news.mit.edu/topic/artificial-intelligence2"
        response = requests.get(url)
        response.raise_for_status()  # Gérer les erreurs HTTP
        soup = BeautifulSoup(response.content, "html.parser")
        articles = []
        # Trouver toutes les balises d'articles
        article_tags = soup.find_all("div", class_="term-page--news-article--item--descr")
        for article_tag in article_tags[:5]:  # Limiter aux 5 premiers articles
            # Extraire les informations pertinentes de chaque article
            title = article_tag.find("h3", class_="term-page--news-article--item--title").text.strip()
            link = "https://news.mit.edu" + article_tag.find("a", class_="term-page--news-article--item--title--link")["href"]
            date = article_tag.find("time").text.strip()
            articles.append({"title": title, "date": date, "link": link})
        return articles
    except Exception as e:
        print("Error fetching data from MIT News:", e)
        return []

@app.route('/')
def index():
    return "Welcome to the AI News Overview API!"

@app.route('/get_data')
def get_data():
    # Appeler la fonction de scraping et retourner les données au format JSON
    data = scrape_mit_news()
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to retrieve data from MIT News."}), 500

@app.route('/articles')
def get_articles():
    # Appeler la fonction de scraping et retourner les informations de base des articles au format JSON
    articles = scrape_mit_news()
    if articles:
        article_info = [{"title": article["title"], "date": article["date"], "link": article["link"]} for article in articles]
        return jsonify(article_info)
    else:
        return jsonify({"error": "Failed to retrieve data from MIT News."}), 500

if __name__ == '__main__':
    app.run(debug=True)
