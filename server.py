from flask import Flask, jsonify, abort
import requests
from textblob import TextBlob

app = Flask(__name__)

news_cache = {}

def fetch_stories():
    """
    Fetches the last 200 story IDs from Hacker News using API.
    For each story ID not already in the cache (`news_cache`), it requests the story's details.
    If the story's title contains "AI", that story is added to the cache.
    """
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
    if response.status_code == 200:
        top_stories_ids = response.json()[:200]  
        for story_id in top_stories_ids:
            if story_id not in news_cache:
                story_response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty")
                if story_response.status_code == 200:
                    story_details = story_response.json()
                    if 'title' in story_details and 'AI' in story_details['title']:
                        news_cache[story_id] = story_details


@app.route('/')
def index():
    """
    Defines the root route ("/") of the app.
    Returns an HTML message as a homepage, guiding users on how to use the API
    """
    mess="<b>News about IA from hacker-news. </b><br><br>"
    mess2='Step 1 : <br> • <a href="/get_data">/get_data</a> : fetch articles<br><br>'
    mess3='Step 2 : <br> • <a href="/articles">/articles</a> : display all articles <br>'
    mess4='• "/article/id" : display article by ID <br><br>'
    mess5='Step 3 : <br> • <a href="/ml">/ml</a> : Display sentiment for all articles <br>'
    mess6='• "/ml/id" : Display sentiment for a specific article (by ID) <br>'
    return mess + mess2 + mess3 + mess4 + mess5 + mess6

@app.route('/articles', methods=['GET'])
def articles():
    """
    This route ("/articles") first calls `fetch_stories` to ensure the cache is updated,
    then generates a list of available articles in the cache, including each article's ID, title, and publication date.
    The response is formatted in JSON.
    """
    fetch_stories()
    articles_info = [
        {"number": story_id, "title": details["title"], "publication_date": details.get("time")}
        for story_id, details in news_cache.items()
    ]
    return jsonify(articles_info)

@app.route('/article/<int:number>', methods=['GET'])
def article(id):
    """
    This route ("/article/<int:number>") allows access to a specific article by its ID.
    If the ID is found in the cache, the article's details are returned in JSON.
    Otherwise, a 404 error is returned indicating the article was not found.
    """
    if id in news_cache:
        return jsonify(news_cache[id])
    else:
        return abort(404, description="Article not found")

def analyze_sentiment(text):
    """
    Function that analyzes the sentiment of a given text using TextBlob.
    Returns "positive" if the polarity score is above 0, "negative" if below 0, and "neutral" otherwise.
    """
    analysis = TextBlob(text)
    return "positif" if analysis.sentiment.polarity > 0 else "négatif" if analysis.sentiment.polarity < 0 else "neutre"

@app.route('/ml', methods=['GET'])
@app.route('/ml/<int:number>', methods=['GET'])

def ml(number=None):
    """
    Defines two routes ("/ml" and "/ml/<int:number>") for sentiment analysis.
    If an ID is provided, performs sentiment analysis on that specific article's title.
    If no ID is provided, performs sentiment analysis for all articles in the cache.
    The results are returned in JSON. Returns a 404 error if the ID is not found.
    """
    if number and number in news_cache:
        article = news_cache[number]
        sentiment = analyze_sentiment(article['title'])
        return jsonify({"number": number, "sentiment": sentiment})
    elif not number:
        sentiments = {story_id: analyze_sentiment(details['title']) for story_id, details in news_cache.items()}
        return jsonify(sentiments)
    else:
        return abort(404, description="Article not found for ML analysis")

if __name__ == '__main__':
    port = 5001 
    app.run(port=port)
