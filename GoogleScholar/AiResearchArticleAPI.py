# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:09:31 2024

@author: Utilisateur
"""

import json
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import webbrowser
from scholarly import scholarly
from serpapi import GoogleSearch
from flask import Flask, jsonify, request
app = Flask(__name__)


# Fonction pour recuperer de la donnee sur google scholar avec serapi
# Ici le mot clef est: artificial intelligence, et on s'intéresse aux articles les plus récents
def fetch_data():
    params = {
      "api_key": "ecf38b4af810eca4f68320b7ce835dd2213be28a16b53bed9bda65e574883231",
      "engine": "google_scholar",
      "q": "artificial intelligence",
      "hl": "en",
      "scisbd": "2"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    formatted_results = []
    for i in range(0,len(results)):
        formatted_search = {
            'Number': i,
            'title': results['organic_results'][i]['title'],
            'author': results['organic_results'][i]['publication_info']['summary'],
            'abstract': results['organic_results'][i]['snippet'],
            'pub_url': results['organic_results'][i]['link']
        }
        formatted_results.append(formatted_search)
    return formatted_results

    
# Fonction pour essayer de creer un titre general à partir des abstracts des articles combinées 
# On voit que le resultat n'est pas forcement satisfaisant pour deux raison: la première c'est que le mot IA est forcément présent souvent , la seconde est la diversite des domaines d'application de l'ia
# Cette fonction s'appuit sur du NLP
def generate_combined_title(abstracts):
    stop_words = set(stopwords.words('english'))
    all_tokens = []

    for abstract in abstracts:
        # Tokeniser l'abstract et passer en minuscules
        tokens = word_tokenize(abstract.lower())
        # Ignorer les 3 premiers tokens
        filtered_tokens = tokens[3:]
        # Filtrer les tokens restants pour enlever les mots vides et les tokens non-alphabétiques
        meaningful_tokens = [token for token in filtered_tokens if token.isalpha() and token not in stop_words]
        all_tokens.extend(meaningful_tokens)

    # Compter la fréquence de chaque mot
    word_counts = Counter(all_tokens)

    # Sélectionner les mots les plus fréquents pour former un "titre" combiné
    most_common_words = [word for word, count in word_counts.most_common(5)]
    combined_title = ' '.join(most_common_words)

    return combined_title
# Premiere route pour load la data avec message de confirmation
@app.route('/get_data', methods=['GET'])
def get_data():
    formatted_results = fetch_data()
    output = "Articles with keyword Artifical Intellingence loaded"
    return output

# Deuxieme route pour avoir un apercu des articles chargés
@app.route('/articles', methods=['GET'])
def articles():
    formatted_results = fetch_data()
    return jsonify(formatted_results)

# Troisieme route pour avoir un article selectionne qui s'ouvre dans notre navigateur
@app.route('/articles/<int:number>', methods=['GET'])
def articles_number(number):
    formatted_results = fetch_data()
    url = formatted_results[number]['pub_url']
    webbrowser.open(url)
    output = "Article open in your website"
    return output

# Quatrieme route qui utilise l'algo de ML pour essayer de construire un titre pour tout les articles
@app.route('/ml',methods=['GET'])
def ml_summary():
    formatted_results=fetch_data()
    abstracts = [result['abstract'] for result in formatted_results if 'abstract' in result]
    combined_title = generate_combined_title(abstracts)
    return jsonify({"combined_title": combined_title})

#Main
if __name__ == '__main__':
   app.run(port=5000)