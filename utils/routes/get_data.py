import sys
import random

from flask import jsonify

from utils.functions.scrap import getArticles
from utils.routes.articles import URL, articles
sys.path.append('..')

def get_data():
    articles = getArticles(URL+ 'blog')
    random.shuffle(articles)
    randomArticles = articles[:5]
    return jsonify(sorted(randomArticles, key=lambda x: x['id']))
