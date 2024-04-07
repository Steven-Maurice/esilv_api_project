from flask import Flask
from getdata import get_data
from articles import articles_blueprint
from ml import ml_blueprint 

app = Flask(__name__)

app.register_blueprint(getdata)
app.register_blueprint(articles_blueprint, url_prefix='/articles') 
app.register_blueprint(ml_blueprint, url_prefix='/ml')  

if __name__ == '__main__':
    app.run(debug=True)