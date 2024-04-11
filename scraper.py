from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

def get_articles(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles_container = soup.find('ul', class_='cols-container')
        articles = articles_container.find_all('li', recursive=False)
        return [(art.find('a').text.strip(), 'https://openai.com' + art.find('a')['href']) for art in articles if art.find('a')]
    else:
        print('La page n\'a pas pu être récupérée')
        return []
    
def get_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the article content using the 'content' id
        content_div = soup.find('div', id='content')
        if content_div:
            # Extract the text from the content div, handling any nested tags as needed
            content = ' '.join(content_div.stripped_strings)  # Gets text from all children, removing extra whitespace
            return content
        else:
            return 'Content not found'
    else:
        return 'Failed to retrieve the article content'