# 1. _getdata

# Rainie0000: Yufei
from os import abort
from flask import Flask, jsonify, redirect # type: ignore
import requests # type: ignore
import xml.etree.ElementTree as ET


app = Flask(__name__)

def retrieve_articles():
    url = 'http://export.arxiv.org/api/query?search_query=cat:cs.CV&max_results=25'
    response = requests.get(url)
    response_xml = ET.fromstring(response.content)

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

    # Récupérez les 25 premiers articles
    five_articles = articles[:25]

    # Retournez les articles en tant que réponse JSON
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

if __name__ == '__main__':
    app.run()
    
    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