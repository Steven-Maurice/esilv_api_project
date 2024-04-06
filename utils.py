import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask import abort


def get_openai_blog_posts():
    """
    Retrieve OpenAI blog posts.
    
    Returns:
        list: A list of dictionaries containing the details of the posts.
    """
    # Define the URL of OpenAI's blog
    url = "https://www.openai.com/blog/"

    # Send an HTTP request to the URL and get the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    posts = []

    # Find all the blog posts
    blog_posts = soup.select(".container .ui-list li")

    for key, post in enumerate(blog_posts):
        # Extract data from each post
        link = post.find("a")['href']
        image = post.find("img")['src']
        title = post.find("h3").get_text(strip=True)
        publication_date = post.find("span").get_text(strip=True)

        # Add post data to the list of articles
        posts.append({
            'id' : key+1,
            'link': f"https://openai.com{link}" ,
            'image': image,
            'title': title,
            'publication_date': publication_date
        })
    return posts


def get_openai_blog_posts_titles():
    """
    Retrieve titles of OpenAI blog posts.
    
    Returns:
        list: A list of strings representing the titles.
    """
    # Define the URL of OpenAI's blog
    url = "https://www.openai.com/blog/"

    # Send an HTTP request to the URL and get the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    posts = []

    # Find all the blog posts
    blog_posts = soup.select(".container .ui-list li")

    for post in blog_posts:
        # Extract data from each post
        title = post.find("h3").get_text(strip=True)

        # Add post data to the list of articles
        posts.append(title)
    return posts



def get_one_post_content(url :  str):
    """
    Retrieve the content of a specific OpenAI blog post.
    
    Args:
        url (str): The URL of the post.
        
    Returns:
        str: The content of the post as plain text.
    """

    # Send an HTTP request to the URL and get the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    post_content = soup.find(id='content')

    return post_content.get_text(strip=True)








def analyse_sentiment(article_content : str):
    
    """
    Analyze the sentiment of an article's content.
    
    Args:
        article_content (str): The content of the article as plain text.
        
    Returns:
        str: A string indicating the detected sentiment (positive, neutral, negative).
    """
    # Initialiser l'analyseur de sentiment
    analyzer = SentimentIntensityAnalyzer()


    # Analyser le sentiment du texte de l'article
    sentiment_score = analyzer.polarity_scores(article_content)

    # Interpréter le score de sentiment
    if sentiment_score['compound'] >= 0.05:
        return "positive"
    elif sentiment_score['compound'] <= -0.05:
        return "neutral"
    else:
        return "negative"



def analyse_sentiment_for_a_post(number : int):
     
    """
    Analyze the sentiment of a specific OpenAI blog post.
    
    Args:
        number (int): The number of the post.
        
    Returns:
        dict: A dictionary containing the details of the post along with its detected sentiment.
    """
    posts = get_openai_blog_posts()
    post = next((post for post in posts if post["id"] == number), None)
    if not post:
        abort(404, description="Post not found")
    
    post['content'] = get_one_post_content(post['link'])
    post['sentiment'] = analyse_sentiment(article_content=post['content'])

    return post

  
