from flask import Flask, request, make_response
from huggingfacepapers.articles import Articles
import time


app = Flask(__name__)

cached_articles = Articles()


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/get_data")
def get_data():
    global cached_articles
    start = request.args.get("start")
    end = request.args.get("end")
    cached_articles.loadArticles(start, end)
    return {"number_of_articles":len(cached_articles.articles)}


@app.route("/articles")
def articles():
    global cached_articles
    return cached_articles.details()


@app.route("/article/<id>")
def article(id):
    global cached_articles
    return cached_articles.get_by_id(id).detail()


@app.route("/ml")
def ml():
    global cached_articles
    start_time = time.time()
    cached_articles.compute_embeddings()
    end_time = time.time()
    return {"message":f"{len(cached_articles.articles)} embeddings computed in {round(end_time-start_time, 2)} seconds"}

@app.route("/ml/<id>")
def ml_article(id):
    global cached_articles
    article = cached_articles.get_by_id(id)
    article.compute_embedding(cached_articles.sentenceTransformerModel)
    return article.embedding


@app.route("/ml/search")
def search():
    global cached_articles
    query = request.args.get("query")
    return cached_articles.get_by_query(query)

@app.route("/ml/2d_viz")
def viz():
    global cached_article
    response = make_response(cached_articles.viz())
    response.headers.set('Content-Type', 'image/jpeg')
    return response

if __name__ == "__main__":
    app.run()
