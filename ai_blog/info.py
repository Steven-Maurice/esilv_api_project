
from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Fonction de scraping pour récupérer les données des articles à partir du site MIT News
def scrape_mit_news():
    url = "https://news.mit.edu/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        articles = []
        # Trouver toutes les balises d'articles
        article_tags = soup.find_all("div", class_="views-row")
        for article_tag in article_tags:
            # Extraire les informations pertinentes de chaque article
            title = article_tag.find("h3", class_="field-content").text.strip()
            date = article_tag.find("span", class_="date-display-single").text.strip()
            link = url + article_tag.find("a")["href"]
            articles.append({"title": title, "date": date, "link": link})
        return articles
    else:
        return None

@app.route('/get_data')
def get_data():
    # Appeler la fonction de scraping et retourner les données au format JSON
    data = scrape_mit_news()
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to retrieve data from MIT News."}), 500

if __name__ == '__main__':
    app.run(debug=True)
