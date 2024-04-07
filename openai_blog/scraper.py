import requests
from bs4 import BeautifulSoup

def fetch_articles(url):
    """
    Fetches articles from the given URL and parses them into a list of dictionaries.

    :param url: The URL to scrape articles from.
    :return: A list of dictionaries, each representing an article with title, URL, image URL, and date.
    """
    articles = []
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')

        articles_list = soup.select('ul.cols-container li')
        for article_li in articles_list:
            title = article_li.h3.text.strip() if article_li.h3 else 'No title available'
            url = article_li.a['href'].strip() if article_li.a else 'URL not available'
            image_url = article_li.find('img')['src'].strip() if article_li.find('img') else 'Image URL not available'
            date = article_li.find('div', class_='f-body-1').span.text.strip() if article_li.find('div', class_='f-body-1') and article_li.find('div', class_='f-body-1').span else 'Date not available'

            articles.append({
                'title': title,
                'url': url,
                'image_url': image_url,
                'date': date
            })

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occurred: {err}')
    finally:
        return articles
