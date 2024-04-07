from flask import Flask, render_template
import openai,jsonify,requests
from scrape_info import scrape_article,findUrlHref

app = Flask(__name__)
url_blog="https://blog-ia.com"

articles = []
urls=findUrlHref(url_blog)
for url in urls:
    article_data = scrape_article(url)
    if article_data:
        articles.append(article_data)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/get_data')
def index():
    return render_template('get_data.html', articles=articles)
@app.route('/article/<int:article_id>')
def article(article_id):
  

  
    article = articles[article_id - 1] 
    print(article)
    return render_template('article.html', article=article)

@app.route('/machine_learning')
def test_article():

    return render_template('ml.html')



    

if __name__ == '__main__':
    app.run()
