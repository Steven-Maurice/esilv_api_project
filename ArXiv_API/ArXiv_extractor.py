

from os import abort
from flask import Flask, jsonify, redirect, render_template
import json
import requests 
import xml.etree.ElementTree as ET
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Rainie0000: Yufei Li

# _getdata

# création de l'instance de Flask
app = Flask(__name__)

# Je récupère les articles à partir de l'API ArXiv
# J'ai initialement pris 5 articles mais finalement on décide de prendre 25 articles
# le code est comme avant mais avec "25" au lieu de "5" que j'ai mis
def retrieve_articles():
    url = 'http://export.arxiv.org/api/query?search_query=cat:cs.CV&max_results=25'
    response = requests.get(url)
    response_xml = ET.fromstring(response.content)

# J'extrais quelques informations de chaque article
    articles = []
    for entry in response_xml.iter('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        author = entry.find('{http://www.w3.org/2005/Atom}author/{http://www.w3.org/2005/Atom}name').text
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
        published = entry.find('{http://www.w3.org/2005/Atom}published').text  # Récupérer la date de publication
        id = entry.find('{http://www.w3.org/2005/Atom}id').text
        link = entry.find('{http://www.w3.org/2005/Atom}link').attrib['href']
        


        article = {
            'title': title,
            'author': author,
            'published': published,
            'summary': summary,
            'id': id,
            'link': link
        }
        articles.append(article)

    return articles


@app.route('/get_data')
def get_data():
    articles = retrieve_articles()


    # On récupère les 25 premiers articles

    five_articles = articles[:25]

    # On retourne les articles en tant que réponse JSON
    return jsonify(five_articles)




# valentinf75 : Valentin Fried

@app.route('/articles')
def articles():
    articles = retrieve_articles()
    # Transformer les articles pour n'inclure que les informations demandées sans le résumé
    articles_info = [{
        'number': i+1,
        'title': article['title'],
        'author': article['author'],
        'published': article['published']
    } for i, article in enumerate(articles)]
    
    return jsonify(articles_info)

# Ici si on veut avoir accès à un article, on remplace <int:number> par son numéro 
# par exemple "3" pour le troisième article
@app.route('/articles/<int:number>')
# def article(number):
#     articles = retrieve_articles()
#     if 1 <= number <= len(articles):
#         return jsonify(articles[number-1])  # Les indices de liste commencent à 0
#     else:
#         abort(404)  # Si l'article n'existe pas, renvoie une erreur 404
def article(number):
    articles = retrieve_articles()
    if 1 <= number <= len(articles):
        article_link = articles[number-1]['link']
        return redirect(article_link)  # Rediriger l'utilisateur vers le lien de l'article
    else:
        abort(404)  # Si l'article n'existe pas, renvoie une erreur 404




# Rainie0000 : Yufei Li

# 4. /ml 

# Ici j'utilise des elements de machine learning 
# comme TfidfVectorizer,Cosine Similarity, perform_recommendation()

# Idée est que j'extrais 100 articles 
# je donne un mot clé et je veux qu'on me 
# recommende l'article (parmi les 100) qui contient plus probablement les éléments 
# qui m'intéressent

def retrieve_4_articles(recommendation):

    recommendation_formatted = recommendation.replace(' ', '+')
    url = f'http://export.arxiv.org/api/query?search_query=all:{recommendation_formatted}&max_results=100'
    response = requests.get(url)
    response_xml = ET.fromstring(response.content)

    articles_4 = []
    for entry in response_xml.findall('{http://www.w3.org/2005/Atom}entry'):
        article = {}

        # Extraction des informations de chaque article
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
        link = entry.find('{http://www.w3.org/2005/Atom}link').attrib['href']

        article['title'] = title
        article['summary'] = summary
        article['link'] = link

        articles_4.append(article)

    return articles_4



def prepare_vector_space(recommendation):
    articles = retrieve_4_articles(recommendation)
    corpus = [article['summary'] for article in articles]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    return articles, vectorizer, X

@app.route('/ml/<string:recommendation>')
def recommend_article(recommendation):
    articles, vectorizer, X = prepare_vector_space(recommendation)
    top_n = 5  # Nombre d'articles à recommander
    recommended_articles = perform_recommendation(recommendation, vectorizer, X, articles, top_n)
    
    pretty_json = json.dumps(recommended_articles, indent=4)

    
    # Retourne la liste des articles recommandés sous forme de JSON
    return render_template('pretty_json.html', json_data=pretty_json)

def perform_recommendation(content, vectorizer, X, articles, top_n):
    content_vector = vectorizer.transform([content])
    similarities = cosine_similarity(content_vector, X).flatten()

    # Trouve les indices des top_n articles les plus similaires
    recommended_article_indices = similarities.argsort()[-top_n:][::-1]

    # Récupère et retourne les articles recommandés
    return [articles[i] for i in recommended_article_indices]


if __name__ == '__main__':
    app.run()
