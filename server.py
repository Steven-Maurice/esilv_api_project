from flask import Flask
from mit_ai_blog.routes import index, get_data, get_articles, get_article, ml_analysis_all, ml_analysis_one

app = Flask(__name__)

@app.route('/')
def index_route():
    return index()

@app.route('/get_data')
def get_data_route():
    return get_data()

@app.route('/articles')
def get_articles_route():
    return get_articles()

@app.route('/article/<int:number>')
def get_article_route(number):
    return get_article(number)

@app.route('/ml')
def ml_analysis_all_route():
    return ml_analysis_all()

@app.route('/ml/<int:number>')
def ml_analysis_one_route(number):
    return ml_analysis_one(number)

if __name__ == '__main__':
    app.run()
