from flask import Flask, render_template
from scrape_info import scrape_article,findUrlHref
from sentiment_analysis import graph

app = Flask(__name__)
# url de notre blog que l'on va scrapper
url_blog="https://blog-ia.com"

articles = []
urls=findUrlHref(url_blog)
# on va alors scrapper le titre, la date, l'auteur et le content avec la fonction scrape_article tout les urls récupéré
for url in urls:
    article_data = scrape_article(url)
    if article_data:
        articles.append(article_data)

# on définit la prémiere root
@app.route('/')
def home():
    return render_template('home.html')

# on définit la seconde root qui donnera accès à tout les articles
@app.route('/get_data')
def index():
    return render_template('get_data.html', articles=articles)

# on définit la root qui donne accès à l'artilce en detail
@app.route('/article/<int:article_id>')
def article(article_id):
  
    article = articles[article_id - 1] 
    print(article)
    return render_template('article.html', article=article)

# on définit la root qui pointera sur une du sentiment analysis
@app.route('/machine_learning')
def sentiment_analysis():
    plot_bytes = graph("https://blog-ia.com")
    graph("https://blog-ia.com")
    return render_template('ml.html',plot=plot_bytes) 

if __name__ == '__main__':
    app.run()
