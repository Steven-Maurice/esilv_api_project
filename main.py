from flask import Flask
from function_get_data import get_data
from function_articles import articles,article
from function_ml import ml_positive, ml_negative

app = Flask(__name__)

app.register_blueprint(get_data)
app.register_blueprint(articles)
app.register_blueprint(article)

if __name__ == '__main__':
    app.run(debug=True)