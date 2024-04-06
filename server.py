from flask import Flask, jsonify
import requests
import xml.etree.ElementTree as ET

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

if __name__ == '__main__':
    app.run(debug=True)
