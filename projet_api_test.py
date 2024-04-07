# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:02:41 2024

@author: danie
"""

from flask import Flask, jsonify, json, request
import requests
from bs4 import BeautifulSoup
import re 


n = 15 #int(input("Entrez le nombre d'articles à récupérer : "))

def articles_dispo():
    site = "https://www.actuia.com/"
    response = requests.get(site)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        article_links = soup.find_all('a', {'class': 'td-image-wrap', 'rel': 'bookmark'})
        num_urls = len(article_links)
        return num_urls

nb_articles = articles_dispo()

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
                
                
                #Ajout d'un avis neutre 
                article_data["Avis"] = "NEUTRE"
                
                # Ajouter les données de l'article à la liste
                articles_data.append(article_data)
                
                
            else:
                print("La requête pour l'article a échoué.")


    else:
        print("La requête a échoué.")

    # Afficher les données de tous les articles
    return articles_data

articles_data = scrap_me(n)

articles_data_sans_bug = [article for article in articles_data if article['Numéro'] not in [3, 4]]

print(articles_data)


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




def analyse_sentiments(texte):
    sentiments = {
    "innovant": 2, "révolutionnaire": 3, "avancé": 2, "pionnier": 2, "disruptif": 2,
    "prometteur": 2, "visionnaire": 3, "progressif": 2, "futuriste": 2, "numérique": 1,
    "intelligent": 2, "automatisé": 2, "efficace": 2, "performant": 2, "sécurisé": 2,
    "évolutif": 2, "adaptatif": 2, "optimisé": 2, "agile": 2, "convivial": 2,
    "convaincant": 2, "inspirant": 2, "stimulant": 2, "réactif": 1, "transparent": 2,
    "intuitif": 2, "efficience": 2, "dynamique": 2, "réalité virtuelle": 2,
    "réalité augmentée": 2, "blockchain": 2, "cryptographie": 2, "cybersécurité": 2,
    "big data": 2, "analyse de données": 2, "cloud computing": 2, "IoT": 2,
    "internet des objets": 2, "apprentissage automatique": 2, "deep learning": 2,
    "réseaux de neurones": 2, "traitement du langage naturel": 2, "robotique": 2,
    "automatisation": 2, "IA": 2, "intelligence artificielle": 2,
    "technologie de pointe": 2, "réseau neuronal convolutif": 2, "génie logiciel": 2,
    "analyse prédictive": 2, "modélisation informatique": 2, "système expert": 2,
    "véhicules autonomes": 2, "smart city": 2, "industrie 4.0": 2, "cybernétique": 2,
    "électronique": 1, "réseau sans fil": 2, "Internet": 1, "télécommunication": 1,
    "système d'exploitation": 1, "interface utilisateur": 1, "interface graphique": 1,
    "programmation": 1, "code source": 1, "développement logiciel": 1,
    "architecture informatique": 1, "informatique quantique": 3, "systèmes embarqués": 2,
    "technologie médicale": 2, "analytique prédictive": 2, "capteurs intelligents": 2,
    "expérience utilisateur": 2, "bioinformatique": 2, "technologie spatiale": 2,
    "innovation disruptive": 2, "cybernétique": 2, "nanotechnologie": 2, "interface cerveau-ordinateur": 2,
    "cybernétique": 2, "informatique biomédicale": 2, "technologie de l'information": 2,
    "architecture logicielle": 2, "développement d'applications": 2, "réalité mixte": 2,
    "robotique avancée": 2, "technologie émergente": 2, "analyse de données volumineuses": 2,
    "technologie disruptive": 2, "technologie intelligente": 2, "cloud hybride": 2,
    "ingénierie informatique": 2, "systèmes informatiques distribués": 2,
    "informatique en nuage": 2, "cyberdéfense": 2, "crypto-monnaie": 2, "méga-données": 2,
    "infonuagique": 2, "internet de tout": 2, "sécurité informatique": 2, "technologie verte": 2,
    "téléinformatique": 2, "analytique des données": 2, "informatique décisionnelle": 2,
    "technologie blockchain": 2, "systèmes d'information": 2
   }

    score = 0

    for mot in texte.split():  # Utilisation de split() sur la variable texte
        if mot.lower() in sentiments:
            score += sentiments[mot.lower()]
    if score > 0:
        return ("C'est une nouvelle favorable.")
    else:
        return ("C'est une nouvelle défavorable.")







# APIIIIIIIIIIIIIIIIIIIIIIIIII
app = Flask(__name__)

#def recup_articles():
#    return 0


@app.route("/")
def home():
    articles_dispo()
    return f"Bienvenue dans notre API AlmightIA et ses {nb_articles} articles à votre disposition"

@app.route("/get_data")
def get_data():
    # Créer une liste pour stocker les titres, les URL et les numéros des articles
    articles_info = []
    for article in articles_data:
        article_info = {"Numero": article["Numéro"], "Titre": article["Titre"], "URL": article["URL"]}
        articles_info.append(article_info)

    # Retourner les données au format JSON avec ensure_ascii=False pour ne pas échapper les caractères spéciaux
    return jsonify(articles_info)


@app.route("/get_data/keyword/<word>")
def keyword(word):
    matching_articles = research_keyword(word, articles_data_sans_bug)
    return jsonify(matching_articles)






@app.route("/articles")
def get_articles():
    # Créer une liste pour stocker les titres, les URL et les numéros des articles
    articles_info = []
    for article in articles_data:
        article_info = {"Numero": article["Numéro"], "Titre": article["Titre"],"Auteur(s)": list(article["Auteurs"]),"Date de publication": article["Date"], "Votre avis" : article["Avis"],  "URL": article["URL"]}
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

@app.route("/articles/<number>/ml")
def analyze_me(number):
    nb = int(number)
    dico = articles_data[nb-1]
    url = articles_data[nb-1]['URL']
    titre = articles_data[nb-1]['Titre']
    auteur = articles_data[nb-1]['Auteurs']
    date = articles_data[nb-1]['Date']
    content = scrapping_content(articles_data[nb-1]['URL'])
    display_me = {'Titre' : titre, 'Analyse sentiment' : analyse_sentiments(content[str(url)]), "Auteur(s)": auteur, "Date de publication": date}
    return jsonify(display_me)



@app.route("/articles/liked")
def get_liked_articles():
    liked_articles = [article for article in articles_data if article["Avis"] == "LIKE"]
    return jsonify(liked_articles)

@app.route("/articles/disliked")
def get_disliked_articles():
    disliked_articles = [article for article in articles_data if article["Avis"] == "DISLIKE"]
    return jsonify(disliked_articles)


@app.route("/articles/<number>/like")
def like_article(number):
    nb = int(number)
    # Vérifier si l'article avec l'ID spécifié existe
    if nb <= len(articles_data):
        # Mettre à jour l'article correspondant avec un like
        articles_data[nb - 1]["Avis"] = "LIKE"
        return jsonify({"message": "Article liked successfully."})
    else:
        return jsonify({"error": "Article not found."}), 404

@app.route("/articles/<number>/dislike")
def dislike_article(number):
    nb = int(number)
    # Vérifier si l'article avec l'ID spécifié existe
    if nb <= len(articles_data):
        # Mettre à jour l'article correspondant avec un dislike
        articles_data[nb - 1]["Avis"] = "DISLIKE"
        return jsonify({"message": "Article disliked successfully."})
    else:
        return jsonify({"error": "Article not found."}), 404


"""
@app.route("/articles/<nb>/comment", methods=["POST"])
def add_comment(nb):
    number = int(nb)
    
    # Vérifier si la méthode est POST
    if request.method == "POST":
        # Récupérer le commentaire depuis la requête
        comment_text = request.form.get("Comment")
        
        # Vérifier si un commentaire a été saisi
        if comment_text:
            # Trouver l'article correspondant au numéro
            article = next((article for article in articles_data if article["Numéro"] == number), None)
            
            if article:
                # Ajouter le commentaire à la liste des commentaires de l'article
                article.setdefault("Commentaires", []).append(comment_text)
                return jsonify({"message": "Commentaire ajouté avec succès."}), 200
            else:
                return jsonify({"error": "Article non trouvé."}), 404

"""

if __name__ == "__main__":
    app.run(debug=True)