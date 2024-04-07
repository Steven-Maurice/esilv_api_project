
from flask import Flask, jsonify, request
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from transformers import pipeline
import openai
import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
app = Flask(__name__)


articles_data = []
# Charger le pipeline de résumé
sentiment_analysis = pipeline("sentiment-analysis")
summarizer = pipeline("summarization")
ner = pipeline("ner")


NEWS_API_KEY = 'b795726f8b0b4da3ab52350844a3a901'
NEWS_API_URL = 'https://newsapi.org/v2/everything'

def fetch_articles():
    articles_data.clear()
    
    params = {
        'q': 'AI', 
        'pageSize': 5,
        'apiKey': NEWS_API_KEY
    }

    # Make the request to the News API
    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code == 200:
        news_data = response.json()
        for idx, article in enumerate(news_data['articles'], start=1):
           
            pub_date = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            formatted_pub_date = datetime.strftime(pub_date, '%Y-%m-%d %H:%M:%S')
            articles_data.append({
                "id": idx,
                "title": article['title'],
                "publication_date": formatted_pub_date,
                "url": article['url'],
                "content": article['content'] 
            })

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/get_data', methods=['GET'])
def get_data():
    # Fetch and store article data using News API
    fetch_articles()
    return jsonify({"success": True, "message": "Data fetched successfully", "articles": articles_data})

@app.route('/articles', methods=['GET'])
def articles():
    # Return a list of articles without the content, if desired
    articles_summary = [{"id": article["id"], "title": article["title"], "publication_date": article["publication_date"]} for article in articles_data]
    return jsonify(articles_summary)

@app.route('/article/<int:number>', methods=['GET'])
def article(number):
    # Find and return the article with the given ID
    article = next((item for item in articles_data if item["id"] == number), None)
    if article:
        return jsonify(article)
    else:
        return jsonify({"error": "Article not found"}), 404



#Fonctions utiles pour la root /ml

def fetch_full_article_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # L'exemple utilise 'article', mais tu devras adapter ce sélecteur
        article_content = soup.find('article')
        
        if article_content:
            return article_content.get_text(strip=True)
        else:
            return "Content not found or different HTML structure."
    else:
        return "Failed to retrieve the webpage."


#analyse sur les articles debut ml

def analyze_trends(text):
    words = word_tokenize(text.lower())  # Tokenize le texte et le convertit en minuscules
    filtered_words = [word for word in words if word.isalnum()]  # Enlève la ponctuation
    stop_words = set(stopwords.words('english'))  # Obtient les stopwords en anglais
    filtered_words = [word for word in filtered_words if not word in stop_words]  # Enlève les stopwords

    # Compte et retourne les mots les plus communs
    word_counts = Counter(filtered_words)
    most_common_words = word_counts.most_common(10)  # Obtient les 10 mots les plus fréquents
    return most_common_words

def clean_entity(entity):
    # Retire les caractères spéciaux des entités
    return entity.lstrip('#').lstrip('@')

def extract_entities(article_content):
    entities = ner(article_content)
    cleaned_entities = {clean_entity(entity["word"]): entity["entity"] for entity in entities}
    return cleaned_entities


@app.route('/ml', methods=['GET'])
@app.route('/ml/<int:number>', methods=['GET'])

def ml_analysis(number=None):
    if number is not None:
        article = next((item for item in articles_data if item["id"] == number), None)
        if article:
            full_content = fetch_full_article_content(article['url'])
            if full_content and not full_content.startswith("Failed"):
                # Prendre les premiers 512 tokens pour éviter de dépasser la capacité du modèle
                tokens = word_tokenize(full_content)[:512]
                truncated_content = " ".join(tokens)
                #Va analyser les mots les plus utilisés
                trends = analyze_trends(full_content)
                entities = extract_entities(full_content)

                # Générer le résumé avec des paramètres ajustés pour éviter les erreurs
                try:
                    summary = summarizer(truncated_content, max_length=100, min_length=25, do_sample=False)[0]["summary_text"]
                except Exception as e:
                    return jsonify({"error": f"Erreur de génération du résumé : {str(e)}"})

                return jsonify({"id": number, "summary": summary, "trends": trends, "entities": entities})
            else:
                return jsonify({"error": "Impossible de récupérer le contenu complet."}), 404
        else:
            return jsonify({"error": "Article non trouvé."}), 404
    else:
        return jsonify({"error": "Veuillez spécifier un numéro d'article."}), 400
    
if __name__ == '__main__':
    app.run(debug=True)
