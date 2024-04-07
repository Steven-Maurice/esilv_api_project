# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 00:04:21 2024

@author: Invite1
"""

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


#On récupère des titres d'articles dans une catégorie au hasard et on renvoie une liste de 5 articles de cette catégorie
import random 
def get_articles_titles_random():
    commande = random.choice(listeURL)
    response = requests.get(commande)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all("p", class_="glue-headline glue-headline--headline-5")
    article_titles = [article.get_text(strip=True) for article in articles]
    article_titles = article_titles[:5]
    return article_titles

get_articles_titles_random()



def get_articles_content_by_category(category_url):
    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all("p", class_="glue-card__description")
    article_content = [article.get_text(strip=True) for article in articles]
    return article_content


#Test méthode
get_articles_content_by_category(company)

"""
def get_articles_publication_date():
    

def get_infos_articles():
     
    titles=get_articles_titles_random()
    publication_date = 
"""

###API######

app = Flask(__name__)


@app.route('/getCategories')
def get_categories_api():
    categories= get_articles_categories()
    return jsonify(categories)

@app.route('/get_data')
def get_data_api():
    titles = get_articles_titles_random()
    return jsonify(titles)

@app.route('/ml')
def analyze_sentiment():
    article_content = get_articles_content_by_category(company)
    sentiment=[]
    for i in article_content:
        blob = TextBlob(i)
        sentiment.append(blob.sentiment.polarity)
    return jsonify(sentiment)


if __name__ == '__main__':
    app.run()

    