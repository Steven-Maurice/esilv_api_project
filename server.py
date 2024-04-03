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
summarizer = pipeline("summarization")

# Replace 'YOUR_API_KEY_HERE' with your actual News API key
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






def analyze_trends(text):
    words = word_tokenize(text.lower())  # Tokenize le texte et le convertit en minuscules
    filtered_words = [word for word in words if word.isalnum()]  # Enlève la ponctuation
    stop_words = set(stopwords.words('english'))  # Obtient les stopwords en anglais
    filtered_words = [word for word in filtered_words if not word in stop_words]  # Enlève les stopwords

    # Compte et retourne les mots les plus communs
    word_counts = Counter(filtered_words)
    most_common_words = word_counts.most_common(10)  # Obtient les 10 mots les plus fréquents
    return most_common_words

@app.route('/ml', methods=['GET'])
@app.route('/ml/<int:number>', methods=['GET'])
def ml_analysis(number=None):
    if number:
        # Trouve l'article par son ID et effectue l'analyse sur cet article
        article = next((item for item in articles_data if item["id"] == number), None)
        if article:
            full_content = fetch_full_article_content(article['url'])
            if not full_content.startswith("Failed"):
                trends = analyze_trends(full_content)
                return jsonify({"id": number, "trends": trends})
            else:
                return jsonify({"error": "Failed to fetch full content"}), 404
        else:
            return jsonify({"error": "Article not found"}), 404
    else:
        # Effectue l'analyse sur tous les articles
        all_trends = []
        for article in articles_data:
            full_content = fetch_full_article_content(article['url'])
            if not full_content.startswith("Failed"):
                trends = analyze_trends(full_content)
                all_trends.append({"id": article["id"], "trends": trends})
        return jsonify({"all_trends": all_trends})

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

def generate_summary(text):
    response = openai.Completion.create(
      engine='text-embedding-ada-002',  # Assure-toi d'utiliser le dernier modèle disponible
      prompt="Résume cet article: \n\n" + text,
      temperature=0.5,
      max_tokens=150,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return response.choices[0].text.strip()

@app.route('/summarize/<int:number>', methods=['GET'])
def summarize_article(number):
    # Recherche l'article par son ID pour obtenir son URL
    article = next((item for item in articles_data if item["id"] == number), None)
    if article:
        # Récupère le contenu complet de l'article via son URL
        full_content = fetch_full_article_content(article['url'])
        
        # Si le contenu a été trouvé, génère un résumé
        if full_content and not full_content.startswith("Failed"):
            summary = generate_summary(full_content)
            return jsonify({"id": number, "summary": summary})
        else:
            return jsonify({"error": "Failed to fetch full content or article content is empty"}), 404
    else:
        return jsonify({"error": "Article not found"}), 404
if __name__ == '__main__':
    app.run(debug=True)
