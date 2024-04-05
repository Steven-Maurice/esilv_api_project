from flask import Flask, request
import requests
from bs4 import BeautifulSoup

DEEPMIND_URL = "https://deepmind.google/discover/blog"
app = Flask(__name__)

def fetch_articles(article_number):
    articles_data = []
    article_counter = 1
    page_number = 1
    blog_end = False
    while len(articles_data) < article_number:
        url = f"{DEEPMIND_URL}?page={page_number}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        list_articles = soup.findAll('ul', {'class': 'cards'})
        articles = list_articles[0].findAll('li', {'class': 'glue-grid__col'})
        # empêche de dépasser le nombre d'article demandé
        if len(articles) < 12:
            blog_end = True
        if len(articles_data) + len(articles) > article_number:
            article_rest = article_number - len(articles_data)
        else:
            article_rest = len(articles)
        for article in articles[:article_rest]:  # Limiter le nombre d'articles
            # Extraction des informations de l'article
            label = article.find('p', {'class': 'glue-label'}).text.strip()
            title = article.find('p', {'class': 'glue-headline'}).text.strip()
            description = article.find('p', {'class': 'glue-card__description'}).text.strip()
            link = article.find('a')['href'].strip()
            date = article.find('time')['datetime'].strip()
            # Ajout à la liste articles_data
            articles_data.append({
                "article_number": article_counter,
                "label": label,
                "title": title,
                "description": description,
                "link": link,
                "date": date
            })
            article_counter += 1
        # blog_end permet d'arreter la boucle si il n'y a plus d'article disponible
        if blog_end:
            break
        page_number += 1
    return articles_data

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/search')
def search():
    # Récupérer le nombre d'articles à afficher de la requête, 10 par défaut
    article_number = request.args.get('article_number', default=10, type=int)
    
    # Récupérer les données des articles
    articles = fetch_articles(article_number)
    
    # Transformer les données en chaîne pour l'affichage
    articles_str = ""
    for article in articles:
        articles_str += f"Titre: {article['title']}\n"
    
    return articles_str

@app.route('/articles')
def articles():
    # Récupérer le nombre d'articles à afficher de la requête, 10 par défaut
    article_number = request.args.get('article_number', default=10, type=int)
    
    # Récupérer les données des articles
    articles = fetch_articles(article_number)
    
    # Transformer les données en chaîne pour l'affichage
    articles_str = ""
    for article in articles:
        articles_str += f"Article {article['article_number']} Label: {article['label']}, Titre: {article['title']}, Description: {article['description']}, Date: {article['date']}\n\n"
    return articles_str

# @app.route('/article/<number>')
# def articles_number():


if __name__ == '__main__':
    app.run()