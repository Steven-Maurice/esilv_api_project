from flask import Flask, request, make_response
from huggingfacepapers.articles import Articles

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
    return cached_articles.preview()
    # return {"number_of_articles":len(cached_articles)}
    return ""


@app.route("/articles")
def articles():
    global cached_articles
    return cached_articles


@app.route("/article/<id>")
def article(id):
    global cached_articles
    return cached_articles.get_by_id(id).detail()


@app.route("/ml")
def ml():
    global cached_articles
    cached_articles.compute_embeddings()
    return cached_articles.details()

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
