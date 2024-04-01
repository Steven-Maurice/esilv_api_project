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

if __name__ == '__main__':
    app.run()

