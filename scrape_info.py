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
    
def findUrlHref(base_url):
    unique_urls = set()  # Utilisation d'un ensemble pour stocker les URL uniques

    page_num = 1
    while True:
        page_url = f"{base_url}/blog/page/{page_num}"
        
        response = requests.get(page_url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            all_a_tags = soup.find_all('a', href=True)  # Trouver tous les <a> tags avec l'attribut href
            
            # Filtrer les deux premiers et le dernier lien
            filtered_a_tags = all_a_tags[2:-1] if len(all_a_tags) > 3 else all_a_tags
            
            # Récupérer les href attributs et ajouter à l'ensemble
            page_urls = [tag['href'] for tag in filtered_a_tags]
            unique_urls.update(page_urls)
            
            # Vérifier s'il y a une page suivante
            next_page_link = soup.find('a', class_='next page-numbers')
            if not next_page_link:
                break  # Sortir de la boucle s'il n'y a pas de lien vers la page suivante
            
            page_num += 1  # Passer à la page suivante

    return list(unique_urls)  # Convertir l'ensemble en liste pour obtenir des URL uniques

