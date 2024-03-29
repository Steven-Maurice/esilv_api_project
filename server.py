from utils.routes.articles import articles,article
from utils.functions.app import app

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/articles')
def get():
    return articles()

@app.route('/article/<int:id>')
def getArticle(id):
    return article(id)

if __name__ == '__main__':
    app.run()