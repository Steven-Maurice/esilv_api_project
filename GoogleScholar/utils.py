# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:36:42 2024

@author: Utilisateur
"""

from scholarly import scholarly
from serpapi import GoogleSearch
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

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
        tokens = word_tokenize(abstract.lower())
        filtered_tokens = tokens[3:]
        meaningful_tokens = [token for token in filtered_tokens if token.isalpha() and token not in stop_words]
        all_tokens.extend(meaningful_tokens)

    word_counts = Counter(all_tokens)

    
    most_common_words = [word for word, count in word_counts.most_common(5)]
    combined_title = ' '.join(most_common_words)

    return combined_title
