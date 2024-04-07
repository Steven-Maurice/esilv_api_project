from flask import Flask, jsonify, abort
import requests
from textblob import TextBlob

app = Flask(__name__)

news_cache = {}

def fetch_stories():
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
    mess="<b>News about IA from hacker-news. </b><br><br>"
    mess2='Step 1 : <br> • <a href="/get_data">/get_data</a> : fetch articles<br><br>'
    mess3='Step 2 : <br> • <a href="/articles">/articles</a> : display all articles <br>'
    mess4='• "/article/id" : display article by ID <br><br>'
    mess5='Step 3 : <br> • <a href="/ml">/ml</a> : Display sentiment for all articles <br>'
    mess6='• "/ml/id" : Display sentiment for a specific article (by ID) <br>'
    return mess + mess2 + mess3 + mess4 + mess5 + mess6

@app.route('/articles', methods=['GET'])
def articles():
    fetch_stories()
    articles_info = [
        {"number": story_id, "title": details["title"], "publication_date": details.get("time")}
        for story_id, details in news_cache.items()
    ]
    return jsonify(articles_info)

@app.route('/article/<int:number>', methods=['GET'])
def article(number):
    if number in news_cache:
        return jsonify(news_cache[number])
    else:
        return abort(404, description="Article not found")

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return "positif" if analysis.sentiment.polarity > 0 else "négatif" if analysis.sentiment.polarity < 0 else "neutre"
