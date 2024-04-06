from flask import Flask, jsonify
import requests
import xml.etree.ElementTree as ET
import re
from collections import Counter

app = Flask(__name__)

# Variable globale pour stocker les données des articles
articles_data = []

ARXIV_API_URL = "http://export.arxiv.org/api/query?"

def fetch_and_store_articles():
    query = 'cat:cs.AI'  # Recherche d'articles sur l'intelligence artificielle
    max_results = 5
    response = requests.get(f"{ARXIV_API_URL}search_query={query}&start=0&max_results={max_results}")
    root = ET.fromstring(response.text)
    ns = {'default': 'http://www.w3.org/2005/Atom'}

    articles_data.clear()  # Nettoie la liste existante avant de la remplir à nouveau

    for entry in root.findall('default:entry', ns):
        article = {
            'id': entry.find('default:id', ns).text.split('/')[-1],  # Extrait le numéro de l'article
            'title': entry.find('default:title', ns).text,
            'published': entry.find('default:published', ns).text,
            'authors': [author.find('default:name', ns).text for author in entry.findall('default:author', ns)],
            'summary': entry.find('default:summary', ns).text.strip(),  # Récupère et nettoie le résumé
            'url': entry.find('default:link[@title="pdf"]', ns).attrib['href'] if entry.find('default:link[@title="pdf"]', ns) is not None else entry.find('default:id', ns).text
        }
        articles_data.append(article)

@app.route('/get_data', methods=['GET'])
def get_data():
    fetch_and_store_articles()
    return jsonify({'message': 'Articles fetched successfully'})

@app.route('/articles', methods=['GET'])
def articles():
    # Formate et retourne les données d'article extraites, sans inclure le résumé
    formatted_articles = [
        {
            'Article Number': article['id'],
            'Title': article['title'],
            'Publication Date': article['published'],
            'Authors': article['authors'],
            'URL': article['url']
        } for article in articles_data
    ]
    return jsonify(formatted_articles)

@app.route('/article/<number>', methods=['GET'])
def article(number):
    # Trouve et retourne uniquement le résumé et l'URL d'un article spécifique par son ID
    article = next((item for item in articles_data if item['id'] == number), None)
    if article:
        return jsonify({
            'Summary': article['summary'],  # Affiche uniquement le résumé de l'article
            'URL': article['url']  # Inclut également l'URL de l'article
        })
    else:
        return jsonify({'message': 'Article not found'}), 404

def get_main_keyword(summary):
    # Liste simplifiée des mots courants à exclure
    stop_words = set(['the', 'and', 'in', 'of', 'to', 'a', 'with', 'for', 'on', 'as', 'is', 'are', 'by', 'that', 'this', 'it', 'an', 'be', 'from', 'which', 'or', 'at', 'not'])
    words = re.findall(r'\b\w+\b', summary.lower())
    
    # Filtrer les stop words et compter la fréquence des mots restants
    word_counts = Counter([word for word in words if word not in stop_words])
    
    if word_counts:
        # Sélectionnez le mot le plus fréquent
        main_keyword, _ = word_counts.most_common(1)[0]
        return main_keyword
    return None

@app.route('/ml/<article_id>', methods=['GET'])
def recommend_based_on_keyword(article_id):
    # Trouvez l'article cible par ID
    target_article = next((article for article in articles_data if article['id'] == article_id), None)
    if not target_article:
        return jsonify({'message': 'Article not found'}), 404
    
    main_keyword = get_main_keyword(target_article['summary'])
    if not main_keyword:
        return jsonify({'message': 'No main keyword found for the target article'}), 404
    
    # Recherchez d'autres articles contenant le mot-clé principal
    recommended_articles = [
        article for article in articles_data
        if main_keyword in article['summary'].lower() and article['id'] != article_id
    ]
    
    # Retournez les articles recommandés (vous pouvez choisir de retourner l'ID, le titre, etc.)
    return jsonify([{'id': art['id'], 'title': art['title']} for art in recommended_articles])


@app.route('/search_by_keyword/<keyword>', methods=['GET']) #2ème fonction de ML en plus
def search_by_keyword(keyword):
    keyword = keyword.lower()  # Convertir le mot-clé en minuscules pour une recherche insensible à la casse
    # Filtrer les articles contenant le mot-clé dans leur résumé
    filtered_articles = [
        {'id': article['id'], 'title': article['title']}
        for article in articles_data
        if keyword in article['summary'].lower()
    ]

    if filtered_articles:
        return jsonify(filtered_articles)
    else:
        return jsonify({'message': 'No articles found containing the keyword'}), 404

if __name__ == '__main__':
    app.run(debug=True)
