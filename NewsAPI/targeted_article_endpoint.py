from flask import Blueprint, jsonify
from newsapi import NewsApiClient
from flask import Flask
from bs4 import BeautifulSoup
import requests
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

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

#we create a function that gives interpretation based on coefficent
def interpret_score(score):
    """
    Interprets the sentiment score.

    Args:
        score (dict): A dictionary containing sentiment scores.

    Returns:
        str: The interpretation of the sentiment score.
    """
    comp = score['compound']
    pos = score['pos']
    neu = score['neu']
    neg = score['neg']

    if comp >= 0.05:
        if pos > 0.5:
            return "L'article est globalement positif, exprimant un sentiment favorable."
        else:
            return "Bien que majoritairement positif, l'article contient des nuances neutres significatives."
    elif comp <= -0.05:
        if neg > 0.5:
            return "L'article est globalement négatif, exprimant des opinions ou des sentiments défavorables."
        else:
            return "Bien que majoritairement négatif, l'article contient des nuances neutres significatives."
    else:
        if neu > 0.7:
            return "L'article est principalement neutre, avec peu d'expression de sentiments positifs ou négatifs."
        else:
            return "L'article présente un équilibre entre les sentiments positifs et négatifs, sans prédominance claire."


#we create the endpoint 'ml/article_number that executes a machine learning script to get the sentiment analysis of the provided article
@article_blueprint.route('/ml/<int:number>', methods=['GET'])
def analyse_sentiment(number):
    """
    Analyzes the sentiment of a specific article.

    Args:
        number (int): The index of the article to analyze.

    Returns:
        dict: JSON response containing the sentiment analysis results.
    """
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
    full_content = scrape_article_content(selected_article['url'])

    #if our scraping doesn't work, we use the API response
    if full_content is None:
        full_content = selected_article.get('content', 'Content not available.')
 
    detailed_article = {
        'content': full_content,
        'url': selected_article['url'],
    }
    #we perform the sentiment analysis on the content using the SentimentIntensityAnalyzer() function from NLTK library
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(detailed_article['content'])

    #we interpret the score with the function created previously
    interpretation = interpret_score(score)
    
    return jsonify({
        'score': score,
        'interpretation': interpretation
    })


