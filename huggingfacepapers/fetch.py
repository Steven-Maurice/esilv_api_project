import requests
from bs4 import BeautifulSoup
from huggingfacepapers import parse

def articles():
    response = requests.get("https://huggingface.co/papers")
    if response.status_code != 200:
        raise Exception("Request error")
    articles = parse.articles(response)
    return articles