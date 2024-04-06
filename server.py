from flask import Flask, render_template
import openai,jsonify,requests
from scrape_info import scrape_article

app = Flask(__name__)
url1="https://blog-ia.com/sora-open-ai/"
url2="https://blog-ia.com/ai-act-europe/"
url3="https://blog-ia.com/lintelligence-artificielle-fait-debat-dans-le-monde-de-lart/"
url4="https://blog-ia.com/clonage-de-voix-ia-transformez-votre-voix-avec-lintelligence-artificielle/"
url5="https://blog-ia.com/les-investissements-mondiaux-dans-lintelligence-artificielle/"
urls = [url1, url2, url3, url4, url5]

articles = []
for url in urls:
    article_data = scrape_article(url)
    if article_data:
        articles.append(article_data)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/get_data')
def index():
    return render_template('index.html', articles=articles)
@app.route('/article/<int:article_id>')
def article(article_id):
  

  
    article = articles[article_id - 1] 
    return render_template('article.html', article=article)

@app.route('/machine_learning')
def test_article():

    return render_template('ml.html')



    

if __name__ == '__main__':
    app.run()
