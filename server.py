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

#Root pour récupérer tous les url des articles
@app.route('/url')
def get_articles_urls():

   with open('articles.json') as f:
      data = json.load(f)

   urls = [article['url'] for article in data]

   return {'url des articles': urls}

if __name__ == '__main__':
    app.run()

