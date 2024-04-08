import sys
sys.path.append('..')
from utils.functions.scrap import getArticles, getArticle
from utils.functions.app import app, printLog

URL = "https://www.craft.ai/"

def articles():
    page = 1
    isScrapped = False
    articles = []
    while not isScrapped:
        data = getArticles(URL+ 'blog?ad82156a_page='+str(page))
        articles += data
        if len(data) == 0:
            isScrapped = True
        else:
            page += 1
    for i, article in enumerate(articles):
        article['id'] = i
    return articles

def article(index):
    data = articles()
    if index >= len(data):
        return {'error': 'Index out of range'}
    article = getArticle(URL+data[index]['link'])
    return article