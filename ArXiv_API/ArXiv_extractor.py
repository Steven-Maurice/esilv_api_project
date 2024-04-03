print("Hello world")

import requests
from bs4 import BeautifulSoup

def fetch_article_details(entry):
    article = {}
    article['id'] = entry.find('id').text
    article['title'] = entry.find('title').text.strip()
    article['published_date'] = entry.find('published').text
    article['updated_date'] = entry.find('updated').text
    article['summary'] = entry.find('summary').text.strip()
    
    authors = []
    for author_tag in entry.find_all('author'):
        authors.append(author_tag.find('name').text)
    article['authors'] = authors
    
    article['doi'] = entry.find('arxiv:doi').text
    
    article['comment'] = entry.find('arxiv:comment').text
    article['journal_ref'] = entry.find('arxiv:journal_ref').text
    
    article['pdf_link'] = entry.find('link', title='pdf')['href']
    article['arxiv_link'] = entry.find('link', rel='alternate')['href']
    
    return article

def fetch_articles(query, max_results=10):
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
max_results = 1
articles = fetch_articles(query, max_results)

for article in articles:
    print("Titre:", article['title'])
    print("Date de publication:", article['published_date'])
    print("Auteurs:", ", ".join(article['authors']))
    print("Résumé:", article['summary'])
    print("DOI:", article['doi'])
    print("Commentaire:", article['comment'])
    print("Journal de référence:", article['journal_ref'])
    print("Lien PDF:", article['pdf_link'])
    print("Lien arXiv:", article['arxiv_link'])
