# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from flask import Flask, jsonify
from functions import arxiv_data,get_articles,ml_sentiments


##########
app = Flask(__name__)
app.config["DEBUG"] = True


#root by default
@app.route('/', methods=['GET'])
def home():
   return "<h1>Projet API</h1><p>Cette page est la présentation de mon API</p>"


#1st endpoint : Fetches a list of articles from the site (5 articles).
@app.route('/get_data',methods=['GET'])
def get_data():
  data = arxiv_data("all:AI") #call the arxiv_data function from functions.py
  path = '{http://www.w3.org/2005/Atom}'
  list_of_articles = []
  for entry in data.findall(path+'entry'):
    title= entry.find(path+'title').text
    link = entry.find(path+'id').text
    list_of_articles.append({'Title':f'{title}','Link':f'{link}'})
  return jsonify(list_of_articles)

#2nd endpoint : Displays information about the articles, including the article number, title, publication date, etc., but not the content itself.
@app.route('/articles',methods=['GET'])
def articles():
  data = arxiv_data("all:AI")
  path = '{http://www.w3.org/2005/Atom}'
  articles = []
  for entry in data.findall(path+'entry'):
    title= entry.find(path+'title').text
    link = entry.find(path+'id').text
    author = entry.find(path+'author').find(path+'name').text
    date = entry.find(path+'published').text[0:10]
    id = link[21:]
    urlpdf = f"http://arxiv.org/pdf/{id}"
    articles.append({'Title':f'{title}','Date': f'{date}','Id': f'{id}','Link': f'{link}','Author': f'{author}','Pdf': f'{urlpdf}'})
  return jsonify(articles)

#3rd endpoint : Accesses the content of a specified article.
@app.route('/article/<int:number>',methods=['GET'])
def specified_article(number):
  articles = get_articles()
  if (number >=1 and number <= len(articles)):
    specified = articles[number-1]
    return jsonify(specified)
  else:
    return jsonify({'error': 'Number out of range.'}),404

#4th endpoint : Machine Learning script
@app.route('/ml', methods=['GET'])
def ml():
  articles = get_articles()
  sentiments = []
  
  for article in articles:
    sentiment = ml_sentiments(article[6])
    sentiments.append({'id': article[2],'title': article[0],'sentiment':f'{sentiment}'})

  return jsonify(sentiments)

#5th endpoint : Accesses articles by author filter keyword
@app.route('/author/<keyword>',methods=['GET'])
def author(keyword):
  data = arxiv_data(f'au:{keyword}')
  path = '{http://www.w3.org/2005/Atom}'
  articles = []
  for entry in data.findall(path+'entry'):
    title= entry.find(path+'title').text
    link = entry.find(path+'id').text
    author = entry.find(path+'author').find(path+'name').text
    date = entry.find(path+'published').text[0:10]
    urlpdf = f"http://arxiv.org/pdf/{id}"
    articles.append({'Author': f'{author}','Title':f'{title}','Date': f'{date}','Link': f'{link}','Pdf': f'{urlpdf}'})
  return jsonify(articles)

#6th endpoint : Accesses articles by keyword filter (search keyword in abstract)
@app.route('/summary/<keyword>',methods=['GET'])
def summary(keyword):
  data = arxiv_data(f'abs:{keyword}')
  path = '{http://www.w3.org/2005/Atom}'
  articles = []
  for entry in data.findall(path+'entry'):
    title= entry.find(path+'title').text
    link = entry.find(path+'id').text
    author = entry.find(path+'author').find(path+'name').text
    date = entry.find(path+'published').text[0:10]
    urlpdf = f"http://arxiv.org/pdf/{id}"
    summary = entry.find(path+'summary').text
    articles.append({'Author': f'{author}','Title':f'{title}','Date': f'{date}','Link': f'{link}','Pdf': f'{urlpdf}','Summary':f'{summary}'})
  return jsonify(articles)


if __name__ == '__main__':
    app.run(port=5000)
