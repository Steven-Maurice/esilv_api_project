# -*- coding: utf-8 -*-
"""
Created on Sun Apr 7 12:45:57 2024

@author: jerem
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_articles():
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
                    'date': date
                })

        articles_list.sort(key=lambda x: x['date'], reverse=True)
        return articles_list
    else:
        print('Failed to retrieve the page')

articles = scrape_articles()
last_three_articles = articles[:3] 

for article in last_three_articles:
    print(article)