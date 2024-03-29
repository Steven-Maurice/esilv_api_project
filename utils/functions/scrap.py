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
            'title': title,
            'date': date,
            'link': link,
            'image': image,
            'description': description,
            'tag': tag
        })
        
    return data

def getArticle(URL):
    """
    Scrap the article from the given URL
    """
    
    article = requests.get(URL)
    soup = BeautifulSoup(article.content, 'html.parser')
    
    # Extracting author's information
    author_div = soup.find('div', class_='div-block-16')
    author_name = author_div.find('h6').text
    author_position = author_div.find('div', class_='text-block-6').text
    author_image = soup.find('img', class_='image-439')['src']
    
    # Extracting article content
    article_content = soup.find('div', class_='text-rich-text w-richtext')
    
    return {
        'title': soup.find('h1', class_='h3-32-mobile').text,
        'description': soup.find('p', class_='subtitle-1 blog').text,
        'date': soup.find('p', class_='paragraph-16').text,
        'author': {
            'name': author_name,
            'position': author_position,
            'image': author_image
        },
        'article': str(article_content)
    }
