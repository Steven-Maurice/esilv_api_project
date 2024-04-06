import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extraire le titre de l'article
        title = soup.find('h1').text
        
        # Extraire la date de publication de l'article (si disponible)
        date_published = None
        
        # Essayer de trouver la date de publication dans une balise <time>
        time_tag = soup.find('time')
        if time_tag and 'datetime' in time_tag.attrs:
            date_published = time_tag['datetime']
        
      
        
        # Extraire le contenu de l'article
        content = ''
        
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            content += p.text + '\n'
          # Extraire l'auteur de l'article
        author = None
        author_tag = soup.find('span', class_='author')
        if author_tag:
            author = author_tag.text.strip()
        return {
            'title': title,
            'date_published': date_published,
            'content': content,
            'author': author
        }
    else:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        return None
# Test de la fonction avec une URL spécifique
urlBlogWithAllArticle="https://blog-ia.com"
url1="https://blog-ia.com/sora-open-ai/"
url2="https://blog-ia.com/ai-act-europe/"
url3="https://blog-ia.com/lintelligence-artificielle-fait-debat-dans-le-monde-de-lart/"
url4="https://blog-ia.com/clonage-de-voix-ia-transformez-votre-voix-avec-lintelligence-artificielle/"
url5="https://blog-ia.com/les-investissements-mondiaux-dans-lintelligence-artificielle/"
urls = [url1, url2, url3, url4, url5]

def findUrlHref():
    response = requests.get(urlBlogWithAllArticle)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)

        all_a_tags = soup.find_all('a', href=True)  # Find all <a> tags with href attribute
        for tag in all_a_tags:
            print(tag['href'])  # Print the href attribute of each <a> tag


# for url in urls:
#     article_data = scrape_article(url)
#     if article_data:
#        # print("Titre:", article_data['title'])
#        # print("Date de publication:", article_data['date_published'])
#        # print("Auteur:", article_data['author'])
#        # print("Contenu:", article_data['content'])
#        print()
#     else:
#         print("Erreur lors de la récupération des données de l'article.")

findUrlHref()