from flask import Flask, jsonify, render_template, request
from bs4 import BeautifulSoup
import requests
from transformers import pipeline

arxiv_url = "http://export.arxiv.org/api/query"

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/get_data')
def get_data():
    print("Searching for papers...")
    import datetime
    today = datetime.datetime.now()

    date = today.strftime("%Y-%m-%d")
    response = requests.get('http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=lastUpdatedDate&sortOrder=descending')

    soup = BeautifulSoup(response.content, 'xml')

    entries = soup.find_all('entry')

    papers = []
    for entry in entries:
        title = entry.find('title').text
        summary = entry.find('summary').text
        authors = entry.find_all('author')
        authors = [author.find('name').text for author in authors]
        link = entry.find('id').text
        date = entry.find('published').text
        papers.append((title, summary, authors, link, date))

    html = "<html><body>"
    for paper in papers:
        html += f"<h1>{paper[0]}</h1>"
        html += f"<p>Authors: {paper[2]}</p>"
        date = paper[4].split('T')[0]
        html += f"<p>Published: {date}</p>"
        html += f"<p>{paper[1]}</p>"
        html += f"<a href={papers[3]}>{paper[3]}</a>"
    html += "</body></html>"

    headlines = []
    for paper in papers:
        headlines.append(paper[0])
    html += "</body></html>\n"
    html += "<br>"
    html += "<a href='/'>Return to Home</a>"
    with open('./templates/page.html', 'w') as file:
        file.write(html)
    return render_template("page.html", headlines=headlines)


@app.route('/articles')
def articles():
    
    print("Searching for papers...")
    import datetime
    today = datetime.datetime.now()

    date = today.strftime("%Y-%m-%d")
    response = requests.get('http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=lastUpdatedDate&sortOrder=descending')

    soup = BeautifulSoup(response.content, 'xml')

    entries = soup.find_all('entry')

    papers = []
    for entry in entries:
        title = entry.find('title').text
        summary = entry.find('summary').text
        authors = entry.find_all('author')
        authors = [author.find('name').text for author in authors]
        link = entry.find('id').text
        date = entry.find('published').text
        papers.append((title, summary, authors, link, date))

    html = "<html><body>"
    for paper in papers:
        html += f"<h1><a href='http://127.0.0.1:5000/articles/artid={paper[3].split('/')[-1]}'>{paper[0]}</a></h1>"
        html += f"<p>Authors: {paper[2]}</p>"
        date = paper[4].split('T')[0]
        html += f"<p>Published: {date}</p>"
        html += f"<p>{paper[1]}</p>"
        html += f"<a href={papers[3]}>{paper[3]}</a>\n<br>"
        html += f"<a href='http://127.0.0.1:5000/ml/artid={paper[3].split('/')[-1]}'>ID : {paper[3].split('/')[-1]}</a>\n"
    html += "</body></html>"

    headlines = []
    for paper in papers:
        headlines.append(paper[0])
    html += "</body></html>\n"
    html += "<br>"
    html += "<a href='/'>Return to Home</a>"
    with open('./templates/browsearticles.html', 'w') as file:
        file.write(html)
    return render_template("browsearticles.html", headlines=headlines)

@app.route('/articles/artid=<artid>')
def article(artid):
    
    print("Searching for papers...")
    import datetime
    today = datetime.datetime.now()
    print("artid is : " + str(artid))

    date = today.strftime("%Y-%m-%d")
    response = requests.get(f'http://export.arxiv.org/api/query?id_list={artid}')

    soup = BeautifulSoup(response.content, 'xml')
    print("response is : " + str(soup))

    

    authors = soup.find_all('author')
    authors = [author.find('name').text for author in authors]
    paper = (soup.find('entry').find('title').text, soup.find('summary').text, authors, soup.find('id').text, soup.find('published').text)
    html = "<html><body>"
    html += f"<h1>{paper[0]}</h1>"
    html += f"<p>Authors: {''.join([str(autor + ', ') for autor in paper[2]])[:-2]}</p>"
    date = paper[4].split('T')[0]
    html += f"<p>Published: {date}</p>"
    html += f"<p>{paper[1]}</p>"
    html += f"<a href={paper[3]}>{paper[3]}</a>"
    sentiment_analyzer = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment', use_fast=False)
    sentiment = sentiment_analyzer(paper[1])[0]['label']
    html += f"<p>Sentiment: {sentiment}</p>"
    html += "</body></html>"

    
    html += "</body></html>\n"
    html += "<br>"
    html += "<a href='/'>Return to Home</a>"
    with open('./templates/article.html', 'w') as file:
        file.write(html)
    return render_template("article.html", headlines=paper)

@app.route('/ml')
def ml():
    import datetime
    today = datetime.datetime.now()

    date = today.strftime("%Y-%m-%d")
    response = requests.get('http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=lastUpdatedDate&sortOrder=descending')

    soup = BeautifulSoup(response.content, 'xml')
    print("step 1")
    entries = soup.find_all('entry')

    papers = []
    for entry in entries:
        title = entry.find('title').text
        summary = entry.find('summary').text
        authors = entry.find_all('author')
        authors = [author.find('name').text for author in authors]
        link = entry.find('id').text
        date = entry.find('published').text
        papers.append((title, summary, authors, link, date))
    html = "<html><body>"
    for paper in papers:
        html += f"<h1>{paper[0]}</h1>"
        html += f"<p>Authors: {paper[2]}</p>"
        date = paper[4].split('T')[0]
        html += f"<p>Published: {date}</p>"
        html += f"<a href={papers[3]}>{paper[3]}</a>"
        sentiment_analyzer = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment', use_fast=False)
        sentiment = sentiment_analyzer(paper[1])[0]['label']
        html += f"<p>Sentiment: {sentiment}</p>"
    html += "</body></html>\n"
    html += "<br>"
    html += "<a href='/'>Return to Home</a>"
    
    with open('./templates/machinelearning.html', 'w') as file:
        file.write(html)
    return render_template("machinelearning.html", papers=papers, sentiment=sentiment)

@app.route('/ml/artid=<artid>')
def ml_number(artid):
    print("Searching for papers...")
    import datetime
    today = datetime.datetime.now()
    print("artid is : " + str(artid))

    date = today.strftime("%Y-%m-%d")
    response = requests.get(f'http://export.arxiv.org/api/query?id_list={artid}')

    soup = BeautifulSoup(response.content, 'xml')
    print("response is : " + str(soup))

    

    authors = soup.find_all('author')
    authors = [author.find('name').text for author in authors]
    paper = (soup.find('title').text, soup.find('summary').text, authors, soup.find('id').text, soup.find('published').text)
    html = "<html><body>"
    html += f"<h1>{paper[0]}</h1>"
    html += f"<p>Authors: {''.join([str(autor + ', ') for autor in paper[2]])[:-2]}</p>"
    date = paper[4].split('T')[0]
    html += f"<p>Published: {date}</p>"
    html += f"<p>{paper[1]}</p>"
    html += f"<a href={paper[3]}>{paper[3]}</a>"
    sentiment_analyzer = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment', use_fast=False)
    sentiment = sentiment_analyzer(paper[1])[0]['label']
    html += f"<p>Sentiment: {sentiment}</p>"
    html += "</body></html>"

    
    html += "</body></html>\n"
    html += "<br>"
    html += "<a href='/'>Return to Home</a>"
    with open('./templates/article.html', 'w') as file:
        file.write(html)
    return render_template("article.html", headlines=paper)

if __name__ == '__main__':
    app.run(debug=True)
