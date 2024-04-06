# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:02:41 2024

@author: danie
"""

from flask import Flask, jsonify, json
import requests
from bs4 import BeautifulSoup
import re 


n = 5 #int(input("Entrez le nombre d'articles à récupérer : "))


def scrap_me(n):
    url = "https://www.actuia.com/"
    response = requests.get(url)

    articles_data = []  # Liste pour stocker les données de chaque article

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Récupération des URLs des articles
        article_links = soup.find_all('a', {'class': 'td-image-wrap', 'rel': 'bookmark'})[:n]

        # Pour chaque URL d'article, récupération des auteurs, des titres, des dates et de l'URL
        for i, link in enumerate(article_links, 1):
            article_url = link.get('href')
            #print("URL de l'article :", article_url)

            article_data = {"URL": article_url, "Numéro": i}  # Dictionnaire pour stocker les données de l'article avec l'URL et le numéro

            # Récupération des informations de l'article
            article_response = requests.get(article_url)
            if article_response.ok:
                article_soup = BeautifulSoup(article_response.text, 'html.parser')

                # Extraction du titre à partir des deux types de balises
                title_element_1 = article_soup.find('h1', {'class': 'tdb-title-text'})
                title_element_2 = article_soup.find('h1', {'class': 'entry-title'})
            
                if title_element_1:
                    title = title_element_1.text.strip()
                elif title_element_2:
                    title = title_element_2.text.strip()
                else:
                    title = "Titre non trouvé"

                article_data["Titre"] = title

                # Extraction des auteurs
                author_elements = article_soup.find_all('span', {'class': 'td-post-author-name'})
                authors = set([author.text.strip() for author in author_elements])
                if authors:
                    article_data["Auteurs"] = authors
                else:
                    article_data["Auteurs"] = ["Auteur(s) non trouvé(s)."]

                # Extraction des dates
                date_element_1 = article_soup.find('div', {'class': 'entry-meta'})
                date_element_2 = article_soup.find('time', {'class': 'entry-date updated td-module-date'})
            
                if date_element_1:
                    date_span = date_element_1.find('span')
                    date = date_span.text.strip() if date_span else "Date non trouvée"
                elif date_element_2:
                    date = date_element_2['datetime'].split("T")[0]
                else:
                    date = "Date non trouvée"

                article_data["Date"] = date
                
                # Ajouter les données de l'article à la liste
                articles_data.append(article_data)
                
            else:
                print("La requête pour l'article a échoué.")


    else:
        print("La requête a échoué.")

    # Afficher les données de tous les articles
    return articles_data

articles_data = scrap_me(n)
#print(articles_data)


def scrapping_content(url):
    article_data = {}  # Initialiser le dictionnaire pour stocker les données de l'article

    article_response = requests.get(url)
    if article_response.ok:
       article_soup = BeautifulSoup(article_response.text, 'html.parser')

       # Trouver les balises contenant le contenu de l'article
       article_paragraphs = article_soup.find_all('p')

       # Concaténer le texte de chaque paragraphe pour former le contenu de l'article
       article_content = "\n".join(paragraph.text.strip() for paragraph in article_paragraphs)

       # Supprimer les caractères de saut de ligne et les éléments indésirables
       article_content_cleaned = article_content.replace('\n', '').replace('\xa0', '').replace('\r', '')

       # Ajouter l'URL et le contenu de l'article au dictionnaire
       article_data[url] = article_content_cleaned

    else:
       print("La requête pour l'article a échoué.")

    return(article_data)

"""
for article in articles_data:
    url = article["URL"]
    print(f"Contenu de l'article {article['Titre']}:")
    print(scrapping_content(url))
    print()

"""


#print(articles_data[0]['URL'])

#print(scrapping_content(articles_data[0]['URL']))


def research_keyword(word, article_data):
    word=str(word)
    matching_articles = []


    for article in article_data:
        url = article["URL"]
        content_dict = scrapping_content(url)
        content = list(content_dict.values())[0] 

        if word.lower() in content.lower():
            matching_articles.append(article)

    return matching_articles














# APIIIIIIIIIIIIIIIIIIIIIIIIII
app = Flask(__name__)

#def recup_articles():
#    return 0


@app.route("/")
def home():
    return "Bienvenue dans notre API AlmightIA"

@app.route("/get_data")
def get_data():
    # Créer une liste pour stocker les titres, les URL et les numéros des articles
    articles_info = []
    for article in articles_data:
        article_info = {"Numero": article["Numéro"], "Titre": article["Titre"], "URL": article["URL"]}
        articles_info.append(article_info)

    # Retourner les données au format JSON avec ensure_ascii=False pour ne pas échapper les caractères spéciaux
    return jsonify(articles_info)


@app.route("/articles")
def get_articles():
    # Créer une liste pour stocker les titres, les URL et les numéros des articles
    articles_info = []
    for article in articles_data:
        article_info = {"Numero": article["Numéro"], "Titre": article["Titre"],"Auteur(s)": list(article["Auteurs"]),"Date de publication": article["Date"], "URL": article["URL"]}
        articles_info.append(article_info)

    # Retourner les données au format JSON avec ensure_ascii=False pour ne pas échapper les caractères spéciaux
    return jsonify(articles_info)



@app.route("/articles/<number>")
def get_content(number):
    nb = int(number)
    dico = articles_data[nb-1]
    url = articles_data[nb-1]['URL']
    titre = articles_data[nb-1]['Titre']
    auteur = articles_data[nb-1]['Auteurs']
    date = articles_data[nb-1]['Date']
    content = scrapping_content(articles_data[nb-1]['URL'])
    display_me = {'Titre' : titre, 'Contenu' : content, "Auteur(s)": auteur, "Date de publication": date}
    return jsonify(display_me)


if __name__ == "__main__":
    app.run(debug=True)
