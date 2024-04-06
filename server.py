from flask import Flask, request
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Charger le pipeline de résumé avec le modèle pré-entraîné 'facebook/bart-large-cnn'
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

DEEPMIND_URL = "https://deepmind.google"
app = Flask(__name__)

def fetch_articles(article_number):
    articles_data = []
    article_counter = 1
    page_number = 1
    blog_end = False
    while len(articles_data) < article_number:
        url = f"{DEEPMIND_URL}/discover/blog?page={page_number}"
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
            date = article.find('time')['datetime'].strip()
            # Ajout à la liste articles_data
            articles_data.append({
                "article_number": article_counter,
                "label": label,
                "title": title,
                "description": description,
                "date": date
            })
            article_counter += 1
        # blog_end permet d'arreter la boucle si il n'y a plus d'article disponible
        if blog_end:
            break
        page_number += 1
    return articles_data

def find_blog(number_article):
    # Il a 12 articles par page
    page = number_article // 12
    index = number_article % 12
    url = f"{DEEPMIND_URL}?page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    list_articles = soup.findAll('ul', {'class': 'cards'})
    articles = list_articles[0].findAll('li', {'class': 'glue-grid__col'})
    article = articles[index - 1]
    # On récupère le lien de l'article
    link = article.find('a')['href'].strip()
    return link

def scrap_content(link):
    blog_url = f"{DEEPMIND_URL}{link}"
    blog_response = requests.get(blog_url)
    blog_soup = BeautifulSoup(blog_response.text, 'html.parser')
    # On extrait tout les paragraphes de l'article
    main = blog_soup.find('main')
    title = main.find('h1', {'class': 'article-cover__title'})
    p_elements_with_data_block_key = main.findAll(lambda tag: tag.name == 'p' and tag.has_attr('data-block-key'))
    return (title, p_elements_with_data_block_key)

def resume(text):
    max_chars = 4096  # Nombre approximatif de caractères pour rester sous la limite de tokens
    len_list = len(text) // max_chars
    divide_text_list = [text[max_chars*(i):max_chars*(i+1)] for i in range(len_list)]
    divide_text_list.append(text[max_chars*(len_list):])
    summary = ""
    # Générer le résumé
    for i in range(len(divide_text_list)):
        summarization = summarizer(divide_text_list[i], max_length=256, min_length=32, do_sample=False)
        summary += summarization[0]["summary_text"]
    return summary

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

@app.route('/article/<number>')
def articles_number(number):
    link = find_blog(int(number))
    (title, p_elements_with_data_block_key) = scrap_content(link)
    # Transformer les données en chaîne pour l'affichage
    blog_str = ""
    blog_str += f"{title.text.strip()}\n\n"
    for p in p_elements_with_data_block_key:
        blog_str += f"{p.text.strip()}\n\n"
    return blog_str

# Cette requête peux prendre un certain temps en fonction de la puissance de l'ordinateur
@app.route('/ml/<number>')
def resume_article(number):
    link = find_blog(int(number))
    (title, p_elements_with_data_block_key) = scrap_content(link)
    # Transformer les données en chaîne pour le traîtement
    blog_str = ""
    blog_str += f"{title.text.strip()}\n"
    for p in p_elements_with_data_block_key:
        blog_str += f"{p.text.strip()}\n"
    return resume(blog_str) + "\n"

if __name__ == '__main__':
    app.run()