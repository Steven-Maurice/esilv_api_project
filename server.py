from utils.routes.articles import articles,article
from utils.functions.app import app
from utils.routes.get_data import get_data

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/articles')
def getArticles():
    return articles()

@app.route('/get_data')
def getData():
    return get_data()

@app.route('/article/<int:id>')
def getArticle(id):
    return article(id)

if __name__ == '__main__':
    app.run()