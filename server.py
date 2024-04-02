from flask import Flask
import json
from collections import Counter
from scrapping import scrape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'
#nathan' comment
#Root pour exécuter le script de scrapping
@app.route('/get_data')
def get_data():
   scrape()
   return "Scrapping done"

def add_article_numbers(data):
    for i, article in enumerate(data, start=1):
        article['article_number'] = i
    return data

#Root pour récupérer le nombre d'articles dans ma BDD, cad la longeur du json   
@app.route('/nb_articles')  
def get_nb_articles():
    
    with open('articles.json') as json_file:
        data = json.load(json_file)
    
    return {'Number of articles': len(data)}

#Root pour récupérer la répartition entre les catégories d'article avec l'outil Counter, très pratique en python récupérer le nombre d'occurence
@app.route('/categories')
def get_categories_count():

   with open('articles.json') as f:
      data = json.load(f)

   categories = Counter()  
   for article in data:
      categories[article['category']] += 1

   return {'categories': dict(categories)}

@app.route('/categories/<string:category>')
def get_category_articles(category):
    with open('articles.json') as f:
        data = json.load(f)
        data_with_numbers = add_article_numbers(data)

    articles_in_category = [article for article in data_with_numbers if article['category'] == category]

    if articles_in_category:
        return {'articles_in_category': articles_in_category}
    else:
        return {'error': 'Category not found'}, 404

#Root pour récupérer tous les url des articles
@app.route('/url')
def get_articles_urls():

   with open('articles.json') as f:
      data = json.load(f)

   urls = [article['url'] for article in data]

   return {'url des articles': urls}

#Root pour donner les infos selon un certain URL
@app.route('/url/<path:url>')
def get_article_info(url):
    with open('articles.json') as f:
        data = json.load(f)

    for article in data:
        if article['url'] == url:
            return article

    return {'error': 'Article not found for the given URL'}, 404

#Root pour récupérer les titres des articles
@app.route('/title')
def get_title():

   with open('articles.json') as f:
      data = json.load(f)

   title= [article['title'] for article in data]

   return {'Title of the articles': title}


#Root pour afficher toutes les infos des articles
@app.route('/articles')
def get_info():

   with open('articles.json') as f:
      data = json.load(f)

   articles_info = []  # Pour stocker les informations des articles

   for i, article in enumerate(data, start=1):
        numero=i
        category = article.get('category', 'N/A')
        title = article.get('title', 'N/A')
        url = article.get('url', 'N/A')
        publication_date = article.get('date', 'N/A')
        #article_info=f"Article number:{i} named {title} was published the {publication_date} and belongs to the category {category}. Its url is {url}"
        article_info = {
            'Numero of article':i,
            'category': category,
            'title': title,
            'url': url,
            'publication_date': publication_date
        }
        articles_info.append(article_info)
   

   return {'Informations of the articles': articles_info}


@app.route('/article/<int:number>')
def get_article_description(number):
    with open('articles.json') as f:
        data = json.load(f)
        data_with_numbers = add_article_numbers(data)
    
    if number > 0 and number <= len(data_with_numbers):
        article = data_with_numbers[number - 1]
        return {'Publication_Date':article['date'],'Title':article['title'],'Category':article['category'],'Description': article['description']}
    else:
        return {'error': 'Article number out of range'}, 404



if __name__ == '__main__':
    app.run()

