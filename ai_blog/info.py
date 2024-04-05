from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

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
    articles = scrape_mit_news()
    if articles:
        # Retourner uniquement les images et les titres des articles
        data = [{"title": article["title"]} for article in articles]
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


# Fonction de scraping pour récupérer le contenu d'un article spécifique
def scrape_article_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Gérer les erreurs HTTP
        soup = BeautifulSoup(response.content, "html.parser")
        # Trouver le contenu de l'article
        article_content = soup.find("div", class_="paragraph--type--content-block-text")
        if article_content:
            # Formater le texte avec des sauts de ligne entre les paragraphes
            paragraphs = article_content.find_all("p")
            formatted_content = "\n".join(paragraph.get_text(strip=True) for paragraph in paragraphs)
            return formatted_content
        else:
            return None
    except Exception as e:
        print("Error fetching article content:", e)
        return None


@app.route('/article/<int:number>')
def get_article(number):
    # Appeler la fonction de scraping pour récupérer les articles
    articles = scrape_mit_news()
    if 0 < number <= len(articles):
        # Si le numéro d'article est valide, récupérer le contenu de l'article correspondant
        article_url = articles[number - 1]["link"]
        article_content = scrape_article_content(article_url)
        if article_content:
            return jsonify({"content": article_content})
        else:
            return jsonify({"error": "Failed to retrieve article content."}), 500
    else:
        # Si le numéro d'article n'est pas valide, retourner un message d'erreur
        return jsonify({"error": f"Article number {number} not found."}), 404


# Fonction pour effectuer l'analyse de sentiment sur tous les articles
def analyze_sentiment(articles, article_texts):
    # Récupérer le texte de tous les articles
    #article_texts = [article['title'] for article in articles]
    # Initialiser le modèle SVM avec CountVectorizer pour la vectorisation
    model = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('svm', SVC(kernel='linear'))
    ])
    # Données d'entraînement pour l'analyse de sentiment (à titre d'exemple)
    train_data = [
        ("Positive article", "positive"),
        ("Negative article", "negative")
    ]
    # Entraîner le modèle
    model.fit([data[0] for data in train_data], [data[1] for data in train_data])
    # Prédire les sentiments pour chaque article
    predictions = model.predict(article_texts)
    # Créer une liste de résultats avec le titre de l'article et le sentiment prédit
    results = [{"title": articles[i]['title'], "sentiment": predictions[i]} for i in range(len(articles))]
    return results

# Route pour effectuer l'analyse de sentiment
@app.route('/ml')
def ml_analysis_all():
    # Récupérer les articles
    articles = scrape_mit_news()
    if articles:
        # Récupérer le contenu de tous les articles
        article_texts = [scrape_article_content(article['link']) for article in articles]
        # Effectuer l'analyse de sentiment
        results = analyze_sentiment(articles, article_texts)
        return jsonify(results)
    else:
        return jsonify({"error": "Failed to retrieve data from MIT News."}), 500
    
@app.route('/ml/<int:number>')
def ml_analysis_one(number):
    # Récupérer les articles
    articles = scrape_mit_news()
    if articles:
        # Vérifier la validité du numéro d'article
        if 0 < number <= len(articles):
            # Récupérer le contenu de l'article spécifié
            article_content = scrape_article_content(articles[number - 1]["link"])
            # Effectuer l'analyse de sentiment
            results = analyze_sentiment([articles[number - 1]], [article_content])
            return jsonify(results)
        else:
            return jsonify({"error": f"Article number {number} not found."}), 404
    else:
        return jsonify({"error": "Failed to retrieve data from MIT News."}), 500


if __name__ == '__main__':
    app.run(debug=True)
