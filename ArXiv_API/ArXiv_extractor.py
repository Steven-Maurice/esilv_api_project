print("Hello world")

import requests
from bs4 import BeautifulSoup

def fetch_article_details(entry):
    article = {}
    article['title'] = entry.find('title').text.strip() if entry.find('title') is not None else ""
    article['published_date'] = entry.find('published').text if entry.find('published') is not None else ""
    
    authors = []
    for author_tag in entry.find_all('author'):
        authors.append(author_tag.find('name').text if author_tag.find('name') is not None else "")
    article['authors'] = authors
    
    return article

def fetch_articles(query, max_results=5):
    url = f"http://export.arxiv.org/api/query?search_query={query}&max_results={max_results}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('entry')
        
        articles = []
        for entry in entries:
            article = fetch_article_details(entry)
            articles.append(article)
        
        return articles
    else:
        print("Erreur lors de la récupération des articles:", response.status_code)
        return []

query = "all:electron"
max_results = 5
articles = fetch_articles(query, max_results)

for article in articles:
    print("Titre:", article['title'])
    print("Date de publication:", article['published_date'])
    print("Auteurs:", ", ".join(article['authors']))
    print()