from flask import jsonify, Response
from mit_ai_blog.scraping import scrape_mit_news, scrape_article_content
from mit_ai_blog.analysis import analyze_sentiment

def index():
    text = "<html><head><title>Page of Antoine and Leo !</title></head><body>"
    text += "<p>Made by Antoine BUFFANDEAU and Leo DROUIN.</p>"
    text += "<h1>Welcome to MIT news !</h1>"
    text += "<p>This is the home page of our website which displays articles from "
    text += "<a href='https://news.mit.edu/topic/artificial-intelligence2'>MIT News</a>.</p>"
    text += "<h2>The endpoints:</h2>"
    text += "<ul><li> <strong>/get_data</strong> : Fetches a list of 5 articles from the site ;</li>"
    text += "<li> <strong>/articles</strong> : Displays information about the articles, including the article number, title, publication date, etc., but not the content itself ;</li>"
    text += "<li> <strong>/article/&lt;article_number&gt;</strong> : Accesses the content of a specified article ;</li>"
    text += "<li> <strong>/ml</strong> or <strong>/ml/&lt;article_number&gt;</strong> : Executes a machine learning script performing sentiment analysis.</li></ul>"
    text += "</body></html>"
    return Response(text, mimetype="text/html")

def get_data():
    articles = scrape_mit_news()
    if articles:
        data_info = "<h1>Data</h1>"
        for article in articles:
            data_info += f"<p>Title: {article['title']}</p>"
            data_info += "<hr>"
        return data_info
    else:
        return "<h1>Error</h1><p>Failed to retrieve data from MIT News.</p>", 500

def get_articles():
    articles = scrape_mit_news()
    if articles:
        article_info = "<h1>Articles</h1>"
        for article in articles:
            article_info += f"<p>Article number: {article['Article number']}</p>"
            article_info += f"<p>Title: {article['title']}</p>"
            article_info += f"<p>Date: {article['date']}</p>"
            article_info += f"<p>Link: <a href='{article['link']}'>{article['link']}</a></p>"
            article_info += f"<img src='{article['Image']}' alt='Article image'>"
        return article_info
    else:
        return "<h1>Error</h1><p>Failed to retrieve data from MIT News.</p>", 500


def get_article(number):
    articles = scrape_mit_news()
    if 0 < number <= len(articles):
        article_url = articles[number - 1]["link"]
        article_content = scrape_article_content(article_url)
        if article_content:
            return jsonify({"content": article_content})
        else:
            return jsonify({"error": "Failed to retrieve article content."}), 500
    else:
        return jsonify({"error": f"Article number {number} not found."}), 404

def ml_analysis_all():
    articles = scrape_mit_news()
    if articles:
        article_texts = [scrape_article_content(article['link']) for article in articles]
        results = analyze_sentiment(articles, article_texts)
        return jsonify(results)
    else:
        return jsonify({"error": "Failed to retrieve data from MIT News."}), 500

def ml_analysis_one(number):
    articles = scrape_mit_news()
    if articles:
        if 0 < number <= len(articles):
            article_content = scrape_article_content(articles[number - 1]["link"])
            results = analyze_sentiment([articles[number - 1]], [article_content])
            return jsonify(results)
        else:
            return jsonify({"error": f"Article number {number} not found."}), 404
    else:
        return jsonify({"error": "Failed to retrieve data from MIT News."}), 500
