import sys
import random

from utils.routes.articles import URL, articles
sys.path.append('..')

def get_data():
    data = articles()
    random.shuffle(data)
    randomArticles = data[:5]
    return sorted(randomArticles, key=lambda x: x['id'])
