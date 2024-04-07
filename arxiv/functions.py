# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 01:56:47 2024

@author: remid
"""
#!pip install vaderSentiment

import requests
from xml.etree import ElementTree #pour lire les données de l'api arxiv car je n'arrive pas à convertir les données en json
import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

url = 'https://export.arxiv.org/api/query'

#stock the data in a 
def arxiv_data(search_query,nb_results=8):
  params = {
      'search_query': search_query,
      'max_results': nb_results
  }
  answer = requests.get(url,params=params)
  if answer.status_code == 200:
    return ElementTree.fromstring(answer.content) #returns feed (we can find every information inside of the feed)
  else:
    return []




#function that take the information from each article
def get_articles():
  articles = []
  data = arxiv_data("all:AI") #fetch 5 articles from the specified category
  path = '{http://www.w3.org/2005/Atom}'
  for entry in data.findall(path+'entry'): #feed contains child <entry> elements with each <entry> representing an article
    title = entry.find(path+'title').text
    summary = entry.find(path+'summary').text
    author = entry.find(path+'author').find(path+'name').text
    date = entry.find(path+'published').text[0:10]
    link = entry.find(path+'id').text
    id = link[21:]
    urlpdf = f"http://arxiv.org/pdf/{id}"

    articles.append([title, date, id, link, author, urlpdf, summary])

  for article in articles:
    article[1] = datetime.datetime.strptime(article[1], '%Y-%m-%d')
  articles.sort(key=lambda x: x[1], reverse = True)
  return articles

#function that classify a sentence into positive/negative/neutral
def ml_sentiments(text):
  analyzer = SentimentIntensityAnalyzer()
  sentiment_dict = analyzer.polarity_scores(text)
  if sentiment_dict['compound']>= 0.05:
    return 'positive'
  elif sentiment_dict['compound'] <= -0.05 :
    return 'negative'
  else:
    return 'neutral'
