from flask import Flask
import json
from collections import Counter
from scrapping import scrape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

#Root pour exécuter le script de scrapping
@app.route('/get_data')
def get_data():
   scrape()
   return "Scrapping done"

if __name__ == '__main__':
    app.run()