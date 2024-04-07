from flask import Flask
import requests
from flask import jsonify
from all_articles_endpoints import articles_blueprint
from targeted_article_endpoint import article_blueprint

#we initialize the Flask instance with the original route.
app = Flask(__name__)
app.config['DEBUG']=True
@app.route('/')
def index():
    return 'Hello, World!'

app.register_blueprint(articles_blueprint)
app.register_blueprint(article_blueprint)

if __name__ == '__main__':
    app.run()