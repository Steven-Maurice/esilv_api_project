import requests
from bs4 import BeautifulSoup

page_number = 1
# URL du blog DeepMind
url = f"https://deepmind.google/discover/blog?page={page_number}"

# Envoyer une requête HTTP pour obtenir le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Recherche de tous les éléments qui contiennent les articles
# Cette étape dépend fortement de la structure de la page et peut nécessiter des ajustements
list_articles = soup.findAll('ul', {'class': 'cards'})
articles = list_articles[0].findAll('li', {'class': 'glue-grid__col'})
for article in articles:
    # Extraction du label
    label = article.find('p', {'class': 'glue-label'}).text.strip()

    # Extraction du titre de l'article
    title = article.find('p', {'class': 'glue-headline'}).text.strip()
    
    # Extraction de l'URL de l'article
    link = article.find('a')['href'].strip()
    
    # Extraction de la date de publication
    date = article.find('time')['datetime'].strip()
    
    print(f"Label: {label}, Titre: {title}, Lien: {link}, Date: {date}")