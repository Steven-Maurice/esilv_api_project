from flask import Blueprint, jsonify
from newsapi import NewsApiClient
from flask import Flask
from bs4 import BeautifulSoup
import requests

article_blueprint = Blueprint('article', __name__)

def scrape_article_content(url):
    """
    Scrapes the content of an article from the provided URL.

    Args:
        url (str): The URL of the article.

    Returns:
        str: The scraped content of the article.
    """
    try:
        headers = {
            'User-Agent': 'Votre User-Agent ici'
        }
        response = requests.get(url, headers=headers)

        #we parse the html content using BeautifulSoup
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')

            #we select potential content selectors to extract the article content
            content_selectors = ['article', 'div.article-content', '.main-article-content']
            article_content = None

            #we iterate through the selectors to find the appropriate one
            for selector in content_selectors:
                article_content = soup.select_one(selector)
                if article_content:
                    break

            if article_content:
                #we join the stripped strings of the article content
                return ' '.join(article_content.stripped_strings)
            else:
                return None
        else:
            return None
        
    except Exception as e:
        print(f"Error during web scraping: {e}")
        return None
    
@article_blueprint.route('/article/<int:number>', methods=['GET'])
def article(number):
    url = ('https://newsapi.org/v2/top-headlines?'
            'q=Artificial Intelligence&'
            'pageSize=5&'
            'apiKey=2dc9629039304cbd8d0a69e75a3509ee')
    #we send the get request to the API
    response = requests.get(url)
    #we check if the API request is succesful
    if response.status_code != 200:
        abort(500, description="API request failed")
    data = response.json()
    articles_data = data['articles']
    #we check if the number is valid
    if not 1 <= number <= len(articles_data):
        abort(404, description="Article number out of range")
 
    selected_article = articles_data[number -1]
    #we create the content from the previously defined function scrape_article_content
    full_content = scrape_article_content(selected_article['url'])

    #if our scraping doesn't work, we use the API response
    if full_content is None:
        full_content = selected_article.get('content', 'Content not available.')

    detailed_article = {
        'content': full_content,
        'url': selected_article['url'],
    }
    return jsonify(detailed_article)


