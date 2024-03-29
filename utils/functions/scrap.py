import requests
from bs4 import BeautifulSoup

from utils.functions.app import printLog

def getArticles(url):
    """
    Scrap the articles from the given URL
    """
    # get the HTML content of the page
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # get the articles that have this class "blog-cms-item w-dyn-item" and role "listitem"
    articles = soup.find_all('div', class_='blog-cms-item w-dyn-item', role='listitem')
    
    # extract the data
    data = []
    id = 0
    for article in articles:
        # title
        title = article.find('p', class_='title-publi').text
        # date
        date = article.find('div', class_='news-cms1-item-date').text.strip()
        # link
        link = article.find('a')['href']
        # image
        image = article.find('img')['src']
        # description
        description = article.find('p', class_='text-line-limit').text
        # tag. We did a [1] since there is a hidden tag that we don't want
        tag = article.find_all('div', class_='news-cms1-item-text-tag')[1].find('div').text.strip()

        data.append({
            'id': id,
            'title': title,
            'date': date,
            'link': link,
            'image': image,
            'description': description,
            'tag': tag
        })
        
        id += 1

    return data
