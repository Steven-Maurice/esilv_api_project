from flask import Flask, jsonify,request
from bs4 import BeautifulSoup
import requests
from textblob import TextBlob

url = 'https://deepmind.google/discover/blog/'

page = requests.get(url)

soup = BeautifulSoup(page.text,"html")


#Extraction de la liste de catégorie
soup.find('div', class_='mdc-select__menu')
dropdown_menu = soup.find('div', class_='mdc-select__menu')

# Extract all options
options = dropdown_menu.find_all('span', class_='mdc-list-item__text')

# Extract text from options
options_text = [option.get_text() for option in options]

# Print the options
print(options_text)


#Deuxième méthode pour les catégories

select_tag = soup.find('select', class_='glue-select')

# Extraire les options de la balise select
options = select_tag.find_all('option')

# Ignorer la première option qui est "All categories"
categories = [option.get_text(strip=True) for option in options[1:]]

print(categories)


def get_articles_categories():
    
    soup = BeautifulSoup(page.text, 'html.parser')

    dropdown_menu = soup.find('div', class_='mdc-select__menu')
    options = dropdown_menu.find_all('span', class_='mdc-list-item__text')
    categories = [option.get_text() for option in options]
    
    return categories
    
#Scrap utilisé pour les titres

soup.find_all("p",class_="glue-headline glue-headline--headline-5")


#Liste des urls des catégories
company="https://deepmind.google/discover/blog/?category=company"
events="https://deepmind.google/discover/blog/?category=events"
impact="https://deepmind.google/discover/blog/?category=impact"
life_at_deepmind="https://deepmind.google/discover/blog/?category=life-at-deepmind"
open_source="https://deepmind.google/discover/blog/?category=open-source"
research ="https://deepmind.google/discover/blog/?category=research"
responsibility_and_safety="https://deepmind.google/discover/blog/?category=responsibility-and-safety"

listeURL = [company,events,impact,life_at_deepmind,open_source,research,responsibility_and_safety]
print(listeURL)



#Endpoint /articles
#Méthode qui renvoie les titres d'articles par catégorie

def get_articles_titles_by_category(category_url):
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all("p", class_="glue-headline glue-headline--headline-5")
    article_titles = [article.get_text(strip=True) for article in articles]
    article_titles = article_titles[:5]
    return article_titles


get_articles_titles_by_category(company)


#Methodes pour l'API

import random 

commande = random.choice(listeURL)
response = requests.get(commande)
soupRandom = BeautifulSoup(response.text, 'html.parser')

def get_articles_titles_random():
    
    articles = soupRandom.find_all("p", class_="glue-headline glue-headline--headline-5")
    article_titles = [article.get_text(strip=True) for article in articles]
    article_titles = article_titles[:5]
    return article_titles

get_articles_titles_random()

def get_articles_published_dates_random():
    
    articles_dates = soupRandom.find_all("span", class_="glue-label gdm-card__publish-date")
    articles_publish_dates = [date.get_text(strip=True) for date in articles_dates]
    articles_publish_dates = articles_publish_dates[:5]
    
    return articles_publish_dates

def get_articles_infos_random():
    
    articles_titles = get_articles_titles_random()
    articles_dates = get_articles_published_dates_random()
    
    if len(articles_titles) != len(articles_dates):
        raise ValueError("Les listes de titres et de dates ne sont pas de la même longueur.")

    # Création d'un dictionnaire pour stocker les informations
    articles_infos = {}

    # Parcours des listes de titres et de dates
    for i in range(len(articles_titles)):
        article_title = articles_titles[i]
        article_date = articles_dates[i]
        article_number = i + 1  # Numéro de l'article

        # Création d'une clé au format "articleX" où X est le numéro de l'article
        article_key = f"article{article_number}"

        # Stockage des informations dans le dictionnaire
        articles_infos[article_key] = {
            'title': article_title,
            'publication date ': article_date
        }

    return articles_infos


###extraire url###

from urllib.parse import urljoin
def get_full_url():
  
    glue_card_links = soupRandom.find_all('a', class_='glue-card')

    # Liste pour stocker les URLs des articles
    article_urls = []

    # Boucler sur tous les liens avec la classe "glue-card" pour extraire les URLs
    for link in glue_card_links:
        href = link.get('href')
        # Vérifier si le lien contient "/discover/blog/" dans son URL
        if "/discover/blog/" in href:
            # Reformer l'URL complet en ajoutant "https://deepmind.google/" avant chaque URL
            full_url = urljoin("https://deepmind.google/", href)
            article_urls.append(full_url)
        if len(article_urls) == 5:
                break
            
    return article_urls


###Autres méthodes###

def get_articles_content_by_category(category_url):
    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all("p", class_="glue-card__description")
    article_content = [article.get_text(strip=True) for article in articles]
    return article_content

# Obtenir les URLs complets des articles
liste_urls_articles = get_full_url()
def get_articles_content_random():
    articles_content = []

    # Boucler sur chaque URL d'article
    for url_article in liste_urls_articles:
        # Effectuer une requête GET pour récupérer le contenu de l'article
        response = requests.get(url_article)
        
        # Parser le contenu de l'article avec BeautifulSoup
        soup_article = BeautifulSoup(response.text, 'html.parser')
        
        # Initialiser une variable pour stocker le contenu de l'article
        article_content = ""
        
        # Trouver tous les éléments avec l'attribut data-block-key
        datablocks = soup_article.find_all(attrs={"data-block-key": True})
        
        # Concaténer le contenu de chaque élément avec l'attribut data-block-key
        for datablock in datablocks:
            article_content += datablock.get_text(strip=True) + "\n"
        
        # Ajouter le contenu de l'article à la liste des contenus d'article
        articles_content.append(article_content)
    
    
    return articles_content

type(get_articles_content_random())

         
###API######

app = Flask(__name__)

titles_cache = []

@app.route('/getCategories')
def get_categories_api():
    categories= get_articles_categories()
    return jsonify(categories)

@app.route('/get_data')
def get_data_api():
    global titles_cache
    
    titles_cache = get_articles_titles_random()
    return jsonify(titles_cache)

@app.route('/articles')
def get_articles_infos():

    infos = get_articles_infos_random()
    
    return jsonify(infos)

@app.route('/article/<int:number>')
def get_article_content_with_number(number):
    # Vérifier si le numéro d'article est valide
    if number < 1 or number > len(liste_urls_articles):
        return "Invalid article number"
    
    article_content = []
    # Récupérer le contenu de l'article correspondant au numéro donné
    article_content = get_articles_content_random()[number - 1]  # Soustraire 1 car les numéros d'articles commencent à 1
    
    return jsonify(article_content)

@app.route('/ml')
def analyze_sentiment_total():
    article_content = []
    for i in range(len(liste_urls_articles)):
        article_content += get_articles_content_random()[i]
    article_content = ' '.join(article_content)
    
    blob = TextBlob(article_content)
    sentiment = blob.sentiment.polarity
    return jsonify(sentiment)

@app.route('/ml/<int:number>')
def analyze_sentiment(number):
    if number < 1 or number > len(liste_urls_articles):
        return "Invalid article number"
    
    article_content = get_articles_content_random()[number - 1] 
    
    blob = TextBlob(article_content)
    sentiment = blob.sentiment.polarity
    return jsonify(sentiment)


if __name__ == '__main__':
    app.run()
