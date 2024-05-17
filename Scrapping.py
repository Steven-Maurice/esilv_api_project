import requests
from bs4 import BeautifulSoup
from datetime import datetime

def display_X_article(num_articles=3):  
    url = 'https://paperswithcode.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='row infinite-item item paper-card')
        articles_list = []

        for article in articles:
            link = article.find('a', href=True)
            article_url = f"https://paperswithcode.com{link['href']}" if link else None

            title_element = article.find('h1')
            title = title_element.a.text.strip() if title_element and title_element.a else None

            date_element = article.find('span', class_='author-name-text item-date-pub')
            date_text = date_element.text if date_element else None
            date = datetime.strptime(date_text, '%d %b %Y').date() if date_text else None

            if article_url and title and date:
                articles_list.append({
                    'title': title,
                    'url': article_url,
                    'date': date.isoformat()
                })

        articles_list.sort(key=lambda x: x['date'], reverse=True)
        return articles_list[:num_articles]  # Retourne les articles demandés sous forme de dictionnaire

    else:
        return {'error': 'Failed to retrieve the page'}

def top_rated_articles():
    url = 'https://paperswithcode.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='row infinite-item item paper-card')
        articles_data = []

        for article in articles:
            title_element = article.find('h1')
            title = title_element.a.text.strip() if title_element and title_element.a else None

            link = article.find('a', href=True)
            article_url = f"https://paperswithcode.com{link['href']}" if link else None

            date_element = article.find('span', class_='author-name-text item-date-pub')
            date_text = date_element.text if date_element else None
            try:
                article_date = datetime.strptime(date_text, '%d %b %Y').date()
            except ValueError:
                article_date = None

            stars_element = article.find('div', class_='entity-stars')
            stars_text = stars_element.text.strip() if stars_element else "0"
            stars_text = stars_text.split()[0].replace(',', '')  
            stars = float(stars_text) if stars_text != "0" else 0

            if article_url and title and article_date:
                articles_data.append({
                    'title': title,
                    'url': article_url,
                    'date': article_date.isoformat(),
                    'stars': stars
                })

        articles_data.sort(key=lambda x: x['stars'], reverse=True)
        return articles_data[:5]  # Retourne les 5 articles les mieux notés sous forme de dictionnaire

    else:
        return {'error': 'Failed to retrieve the page'}

def articles_by_keyword(keyword):
    url = 'https://paperswithcode.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='row infinite-item item paper-card')
        found_articles = []

        for article in articles:
            title_element = article.find('h1')
            if title_element and title_element.a:
                title = title_element.a.text.strip()
                if keyword.lower() in title.lower():
                    link = title_element.a['href']
                    article_url = f"https://paperswithcode.com{link}"
                    found_articles.append({
                        'title': title,
                        'url': article_url
                    })

        return found_articles if found_articles else {'message': 'No articles found with the keyword'}

    else:
        return {'error': 'Failed to retrieve the page'}

def article_abstract(search_title):
    url = 'https://paperswithcode.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='row infinite-item item paper-card')
        
        for article in articles:
            title_element = article.find('h1')
            if title_element and title_element.a:
                title = title_element.a.text.strip()
                if title.lower() == search_title.lower():
                    abstract_element = article.find('p', class_='item-strip-abstract')
                    abstract = abstract_element.text.strip() if abstract_element else "Abstract not available"
                    return {
                        'title': search_title,
                        'abstract': abstract
                    }

        return {'message': 'Article not found'}

    else:
        return {'error': 'Failed to retrieve the page'}


"""def display_X_article(num_articles=3):  
    url = 'https://paperswithcode.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='row infinite-item item paper-card')
        articles_list = []

        for article in articles:
            # Extraction de l'URL
            link = article.find('a', href=True)
            article_url = f"https://paperswithcode.com{link['href']}" if link else None

            # Extraction du titre
            title_element = article.find('h1')
            title = title_element.a.text.strip() if title_element and title_element.a else None

            # Extraction de la date
            date_element = article.find('span', class_='author-name-text item-date-pub')
            date_text = date_element.text if date_element else None
            date = datetime.strptime(date_text, '%d %b %Y').date() if date_text else None

            if article_url and title and date:
                articles_list.append({
                    'title': title,
                    'url': article_url,
                    'date': date
                })

        # Trier les articles par date
        articles_list.sort(key=lambda x: x['date'], reverse=True)
        
        # Afficher les articles demandés
        for article in articles_list[:num_articles]:
            print(f"Title: {article['title']}\nDate: {article['date']}\nURL: {article['url']}\n")

    else:
        print('Failed to retrieve the page')

#display_X_article(5)  

def top_rated_articles():
    url = 'https://paperswithcode.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='row infinite-item item paper-card')
        articles_data = []

        for article in articles:
            title_element = article.find('h1')
            title = title_element.a.text.strip() if title_element and title_element.a else None

            link = article.find('a', href=True)
            article_url = f"https://paperswithcode.com{link['href']}" if link else None

            date_element = article.find('span', class_='author-name-text item-date-pub')
            date_text = date_element.text if date_element else None
            try:
                article_date = datetime.strptime(date_text, '%d %b %Y').date()
            except ValueError:
                article_date = None

            # Extraction du nombre d'étoiles
            stars_element = article.find('div', class_='entity-stars')
            stars_text = stars_element.text.strip() if stars_element else "0"
            stars_text = stars_text.split()[0].replace(',', '')  
            stars = float(stars_text) if stars_text != "0" else 0

            if article_url and title and article_date:
                articles_data.append({
                    'title': title,
                    'url': article_url,
                    'date': article_date,
                    'stars': stars
                })

        # Trier les articles par nombre d'étoiles décroissant
        articles_data.sort(key=lambda x: x['stars'], reverse=True)
        
        top_articles = articles_data[:5]
        print("Top 5 Rated Articles:\n")
        for article in top_articles:
            print(f"Title: {article['title']}")
            print(f"Date: {article['date']}")
            print(f"URL: {article['url']}")
            print(f"Stars: {article['stars']}\n")
    else:
        print('Failed to retrieve the page')

#top_rated_articles()

def articles_by_keyword(keyword):
    url = 'https://paperswithcode.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='row infinite-item item paper-card')
        found_articles = []

        for article in articles:
            title_element = article.find('h1')
            if title_element and title_element.a:
                title = title_element.a.text.strip()
                if keyword.lower() in title.lower():
                    link = title_element.a['href']
                    article_url = f"https://paperswithcode.com{link}"
                    found_articles.append((title, article_url))

        if found_articles:
            print(f"Articles found with keyword '{keyword}':")
            for title, url in found_articles:
                print(f"Title: {title}, URL: {url}")
        else:
            print("No articles found with the keyword.")
    else:
        print('Failed to retrieve the page')

#articles_by_keyword("An Open Source Language")



def article_abstract(search_title):
    url = 'https://paperswithcode.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='row infinite-item item paper-card')
        
        for article in articles:
            title_element = article.find('h1')
            if title_element and title_element.a:
                title = title_element.a.text.strip()
                if title.lower() == search_title.lower():
                    abstract_element = article.find('p', class_='item-strip-abstract')
                    abstract = abstract_element.text.strip() if abstract_element else "Abstract not available"
                    print(f"Abstract for '{search_title}':\n{abstract}")
                    return

        print("Article not found")
    else:
        print('Failed to retrieve the page')

#article_abstract("Lightplane: Highly-Scalable Components for Neural 3D Fields")

def run_interactive_report():
    print("Choisir la fonction voulu:")
    print("1: Afficher les x derniers articles")
    print("2: Afficher les 5 articles les mieux notés")
    print("3: Article par mots-clés")
    print("4: Résume d'un article")
    
    choice = input("Entrer votre choix (1-4): ")
    
    try:
        choice = int(choice)
    except ValueError:
        print("Choix invalide")
        return
    
    if choice == 1:
        num_articles = int(input("Nombre d'article: "))
        results = display_X_article(num_articles)
        print(results)
    elif choice == 2:
        results = top_rated_articles()
        print(results)
    elif choice == 3:
        keyword = input("Mot-clé: ")
        results = articles_by_keyword(keyword)
        print(results)
    elif choice == 4:
        title = input("Titre : ")
        result = article_abstract(title)
        print(result)
    else:
        print("Choix invalide, choisir un nombre entre 1 et 4")


run_interactive_report()
"""