from flask import Flask
from huggingfacepapers import fetch

app = Flask(__name__)
cached_articles = []

@app.route('/')
def index():
    return 'Hello, World!' 

@app.route('/get_data')
def get_data():
    global cached_articles
    cached_articles = fetch.articles()
    return cached_articles
    return {"number_of_articles":len(cached_articles)}  

@app.route("/articles")
def articles():
    global cached_articles 
    return cached_articles

if __name__ == '__main__':
    app.run()