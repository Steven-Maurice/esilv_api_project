from flask import Flask, jsonify, abort
from utils import get_openai_blog_posts, get_openai_blog_posts_titles, get_one_post_content, analyse_sentiment_for_a_post 

app = Flask(__name__)


@app.route("/get_data")
def get_data():
    """
    Retrieves a list of all available articles.
    
    Returns:
        list: A list of titles of available articles.
    """
    return jsonify(get_openai_blog_posts_titles())

@app.route("/articles")
def get_articles():
    """
    Displays information on all available articles.
    
    Returns:
        dict: A dictionary containing the total number of articles and details of each article.
    """
    posts = get_openai_blog_posts()
    return jsonify({'total': len(posts), 'posts': posts})

@app.route("/article/<int:number>")
def get_article(number):
    """
    Displays the content of a specified article by its number.
    
    Args:
        number (int): The number of the article to retrieve.
        
    Returns:
        dict: A dictionary containing details of the article, including its content.
    """
    posts = get_openai_blog_posts()
    post = next((post for post in posts if post["id"] == number), None)
    if not post:
        abort(404, description="Post not found")
    
    post['content'] = get_one_post_content(post['link'])
    return jsonify(post)
    

@app.route("/ml/<int:number>")
def get_sentiment(number):
    """
    Executes a sentiment analysis script to analyze an article.
    
    Args:
        number (int): The number of the article to analyze.
        
    Returns:
        dict: A dictionary containing details of the article and its detected sentiment.
    """
    post = analyse_sentiment_for_a_post(number)
    return jsonify(post)

if __name__ == "__main__":
    app.run(debug=True)
