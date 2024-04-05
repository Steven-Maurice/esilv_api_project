# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:25:01 2024

@author: danie
"""

from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

url = "https://www.actuia.com/"

response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')  # Utilisez 'html.parser' pour analyser du HTML
    
    #pour extraire les auteurs
    auteur_spans = soup.find_all('span', {'class': 'td-post-author-name'})  # Utilisez find_all() au lieu de findall()
    if auteur_spans:
        for auteur_span in auteur_spans:
            auteur = auteur_span.get_text(strip=True)
            print(auteur)
    else:
        print("Auteur non trouvé.")
    
    #pour extraire les titres
    titles = soup.find_all('h3', {'class': 'entry-title td-module-title'})  # Trouvez toutes les balises <h3> avec la classe spécifiée
    if titles:
        for title in titles:
            titre = title.text.strip()  # Récupérez le texte du titre et supprimez les espaces indésirables
            #print(titre)
    else:
        print("Titres non trouvés.")
        
    #pour récupérer les url
    links = soup.find_all('h3', {'class': 'entry-title td-module-title'})  # Trouvez toutes les balises <h3> avec la classe spécifiée
    if links:
        for link in links:
            a_tag = link.find('a')  # Trouvez la balise <a> à l'intérieur de la balise <h3>
            url = a_tag['href']  # Obtenez la valeur de l'attribut 'href'
            print(url)
    else:
        print("Liens non trouvés.")
        
else:
    print("La requête a échoué.")

    


"""
if response.ok:
    soup = BeautifulSoup(response.content, 'xml')  # 'xml' spécifie que le contenu est au format XML
    xml_content = soup.prettify()  # Utilisez prettify() pour formater le XML de manière lisible
    print(xml_content)
else:
    print("La requête a échoué.")
"""

"""
if response.ok: 
    soup = BeautifulSoup(response.text, 'xml')
    auteur_span = soup.find('span', {'class': 'td-post-author-name'})
    if auteur_span:
        auteur = auteur_span.get_text(strip=True)
        print(auteur)
    else:
        print("Auteur non trouvé.")
else:
    print("La requête a échoué.")
"""