import sys
sys.path.append('..')
from flask import jsonify
from utils.functions.scrap import getArticles, getArticle
from utils.functions.app import app, printLog

URL = "https://www.craft.ai/"

def articles():
    data = getArticles(URL+ 'blog')
    return jsonify(data)

def article(index):
    data = getArticles(URL+'blog')
    if index >= len(data):
        return jsonify({'error': 'Index out of range'})
    article = getArticle(URL+data[index]['link'])
    return jsonify(article)