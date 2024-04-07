from flask import Flask, request, jsonify, render_template_string, redirect, render_template
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import yake

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        if 'article_number' in request.form:
            article_number = request.form.get('article_number')
            if article_number:
                return redirect(f'/article/{article_number}')
        elif 'get_data' in request.form:
            return redirect('/get_data')
        elif 'articles' in request.form:
            return redirect('/articles')
        elif 'ml' in request.form:
            return redirect('/ml')
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Accueil</title>
        <style>
            body { font-family: Verdana, sans-serif; margin: 40px; background-color: #f4f4f9; color: #333; }
            h1 { color: rgb(250, 99, 0); text-align: center; }
            nav ul { list-style-type: none; padding: 0; }
            nav ul li { display: inline; margin-right: 10px; }
            button { background-color: darkorange; border: none; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 5px; }
            input[type="number"] { padding: 10px; margin: 4px; }
            .form-style { margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>Bienvenue sur le site de Quentin, Camille et Alix!</h1>
        <nav>
            <ul>
                <li><form action="/" method="post"><button name="get_data">Montrer une liste d'articles du site</button></form></li>
                <li><form action="/" method="post"><button name="articles">Afficher les informations a propos des articles</button></form></li>
                <li><form action="/" method="post"><button name="ml">Extraire les mots cles des articles</button></form></li>
            </ul>
        </nav>
        <div class="form-style">
            <h2>Voir les détails d'un article</h2>
            <form action="/" method="post">
                <input type="number" name="article_number" min="1" placeholder="Numéro d'article">
                <button type="submit">Voir cet article en particulier</button>
            </form>
        </div>
    </body>
    </html>
    ''')


@app.route('/get_data')
def get_data():
    api_key = "c20aa73bf54d4eff8de2627c71956efe"
    url = "https://newsapi.org/v2/everything"
    parameters = {
        "q": "intelligence artificielle",
        "pageSize": 5,
        "apiKey": api_key,
        "language": "fr"
    }
    
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        articles = response.json()['articles']
        articles_html = '<h1>Articles sur l\'Intelligence Artificielle</h1>'
        for article in articles:
            articles_html += f"<div><h2>{article['title']}</h2><p><a href='{article['url']}' style='text-decoration: none;'><button>Lire l'article</button></a></p></div>"
        return render_template_string('''
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <title>Articles sur l'IA</title>
        </head>
        <body>
            {{ articles_html | safe }}
        </body>
        </html>
        ''', articles_html=articles_html)
    else:
        return "Erreur lors de la récupération des articles"

@app.route('/articles')
def articles():
    api_key = "c20aa73bf54d4eff8de2627c71956efe"  
    url = "https://newsapi.org/v2/everything"
    parameters = {
        "q": "intelligence artificielle",  
        "pageSize": 5,
        "apiKey": api_key,
        "language": "fr"
    }
   
    response = requests.get(url, params=parameters)
   
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        articles_details = "<h1>Articles sur l'Intelligence Artificielle</h1>"
        for index, article in enumerate(articles, start=1):
            title = article.get('title', 'Titre non disponible')
            published_at = article.get('publishedAt', 'Date non disponible')
            source_name = article.get('source', {}).get('name', 'Source non disponible')
            article_url = article.get('url', 'URL non disponible')
           
            if published_at != 'Date non disponible':
                published_at = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%d %B %Y, %H:%M")
               
            articles_details += f"<p>Article #{index}: <b>Titre:</b> {title}, <b>Date de publication:</b> {published_at}, <b>Source:</b> {source_name}, <b>URL:</b> <a href='{article_url}'>{article_url}</a></p>"
        return articles_details
    else:
        return "Erreur lors de la récupération des articles"


@app.route('/article/<int:number>')
def get_article(number):
    api_key = "c20aa73bf54d4eff8de2627c71956efe"
    url = "https://newsapi.org/v2/everything"
    parameters = {
        "q": "intelligence artificielle",
        "pageSize": 10,  
        "apiKey": api_key,
        "language": "fr"
    }
    
    response = requests.get(url, params=parameters)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        
        if number - 1 < len(articles):
            article = articles[number - 1]  
            article_url = article.get('url', None)
            
            if article_url:
                return redirect(article_url)  
            else:
                return "URL de l'article non disponible", 404
        else:
            return "Numéro d'article non valide ou hors de portée", 404
    else:
        return "Erreur lors de la récupération des articles depuis l'API NewsAPI", 500


@app.route('/ml', methods=['GET', 'POST'])
def ml():
    api_key = "c20aa73bf54d4eff8de2627c71956efe"
    url = "https://newsapi.org/v2/everything"
    parameters = {
        "q": "intelligence artificielle",
        "pageSize": 10,
        "apiKey": api_key,
        "language": "fr"
    }

    response = requests.get(url, params=parameters)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        kw_extractor = yake.KeywordExtractor(lan="fr", top=5) 
        
        used_keywords = set()  
        articles_details = "<h1>Mots-clé principaux pour chaque article sur l'Intelligence Artificielle</h1>"
        
        for index, article in enumerate(articles, start=1):
            text = article.get('content', '')
            keywords = kw_extractor.extract_keywords(text)
            
            unique_keywords = []
            for keyword, score in keywords:
                if keyword not in used_keywords:
                    used_keywords.add(keyword)
                    unique_keywords.append(f"{keyword} ({score:.2f})")
                    if len(unique_keywords) == 5:
                        break
            
            if unique_keywords:
                keywords_str = ', '.join(unique_keywords)
                articles_details += f"<p>Article #{index}: <b>Titre:</b> {article.get('title', 'Titre non disponible')}, <b>Mots-clés:</b> {keywords_str}</p>"
            else:
                articles_details += f"<p>Article #{index}: <b>Titre:</b> {article.get('title', 'Titre non disponible')}, <b>Mots-clés:</b> Aucun mot-clé unique trouvé.</p>"
        
        return articles_details
    else:
        return "Erreur lors de la récupération des articles"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
