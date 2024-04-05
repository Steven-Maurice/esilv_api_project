import requests
from bs4 import BeautifulSoup

# URL d'un blog DeepMind
url = f"https://deepmind.google/discover/blog/sima-generalist-ai-agent-for-3d-virtual-environments/"

# Envoyer une requête HTTP pour obtenir le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Recherche de tous les éléments qui contiennent les articles
main = soup.find('main')
title = main.find('h1', {'class': 'article-cover__title'})
p_elements_with_data_block_key = main.findAll(lambda tag: tag.name == 'p' and tag.has_attr('data-block-key'))

for p in p_elements_with_data_block_key:
    print(title.text.strip())
    print(p.text.strip())