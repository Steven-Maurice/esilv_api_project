# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:35:46 2024

@author: Utilisateur
"""
from flask import jsonify, request
import webbrowser
from utils import fetch_data, generate_combined_title
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def init_app(app):
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
     
    # Route pour avoir les auteurs d'un article
    @app.route('/authors/<int:number>', methods=['GET'])
    def list_authors2(number):
        formatted_results = fetch_data()
        authors_list = []
        author_str = formatted_results[number]['author']
        authors = [author.strip() for author in author_str.replace("and", ",").split(",")]
        authors_list.extend(authors)
        return jsonify(authors_list)

    # Route pour avoir les auteurs des articles et leur nombre de publication   
    @app.route('/authors', methods=['GET'])
    def list_authors():
        formatted_results = fetch_data()
        authors_list = []
        for article in formatted_results:
            authors_str = article['author']
            authors = [author.strip() for author in authors_str.replace("and", ",").split(",")]
            authors_list.extend(authors)
        

        authors_count = Counter(authors_list)
        results_list = [{"author": author, "publications": count} for author, count in authors_count.items()]
        
        return jsonify(results_list)

    # Route pour avoir des articles en fonction d'un keyword
    @app.route('/search/<keyword>', methods=['GET'])
    def search_articles(keyword):
        keyword = keyword.lower()
        formatted_results = fetch_data()
        filtered_results = [article for article in formatted_results if keyword in article['title'].lower() or keyword in article['abstract'].lower()]

        return jsonify(filtered_results)


    # Route pour avoir des statistiques de fréquence de mots
    @app.route('/statistics', methods=['GET'])
    def statistics():
        formatted_results = fetch_data()
        total_articles = len(formatted_results)
     
        authors = [article['author'] for article in formatted_results]
        author_counts = Counter(authors)
     
        stop_words = set(stopwords.words('english'))
        titles = ' '.join([article['title'].lower() for article in formatted_results])
        abstracts = ' '.join([article['abstract'].lower() for article in formatted_results])
     
        title_tokens = [word for word in word_tokenize(titles) if word.isalpha() and word not in stop_words]
        abstract_tokens = [word for word in word_tokenize(abstracts) if word.isalpha() and word not in stop_words]
     
        title_word_counts = Counter(title_tokens).most_common(5)
        abstract_word_counts = Counter(abstract_tokens).most_common(5)
     
        return jsonify({
            "total_articles": total_articles,
            "articles_per_author": author_counts,
            "frequent_words_in_titles": title_word_counts,
            "frequent_words_in_abstracts": abstract_word_counts
        })

