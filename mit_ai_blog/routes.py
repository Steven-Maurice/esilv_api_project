from flask import jsonify, Response
from mit_ai_blog.scraping import scrape_mit_news, scrape_article_content
from mit_ai_blog.analysis import analyze_sentiment

#Welcome page
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

#Function which prints the title of the articles
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

#Function which print the data of the articles (title/number/link/image)
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

#Function which retrieve artciel content
def get_article(number):
    articles = scrape_mit_news()
    if 0 < number <= len(articles):
        article_url = articles[number - 1]["link"]
        article_content = scrape_article_content(article_url)
        if article_content:
            return f"<h1>Article {number}</h1><p>{article_content}</p>"
        else:
            return "<h1>Error</h1><p>Failed to retrieve article content.</p>", 500
    else:
        return f"<h1>Error</h1><p>Article number {number} not found.</p>", 404

#Funtion which perform the sentiment analysis:
# - Polarity: refers to the emotional intensity or sentiment expressed in text ;
# - Subjectivity: refers to the degree to which a statement is opinionated or expresses personal feelings.
def ml_analysis_all():
    articles = scrape_mit_news()
    if articles:
        article_texts = [scrape_article_content(article['link']) for article in articles]
        results = analyze_sentiment(articles, article_texts)
        html_response = "<h1>Sentiment Analysis Results</h1>"
        for result in results:
            html_response += f"<p>Article: {result['Article']}</p>"
            html_response += f"<p>Title: {result['title']}</p>"
            html_response += f"<p>Sentiment: {result['sentiment']}</p>"
            html_response += f"<p>Polarity: {result['polarity']}</p>"
            html_response += f"<p>Subjectivity: {result['subjectivity']}</p>"
            html_response += f"<p>Vader Polarity Analysis: {result['Polarity analysis']}</p>"
            html_response += "<hr>"
        return html_response
    else:
        return "<h1>Error</h1><p>Failed to retrieve data from MIT News.</p>", 500

#Function which perform sentiment analysis on the article specified
def ml_analysis_one(number):
    articles = scrape_mit_news()
    if articles:
        if 0 < number <= len(articles):
            article_content = scrape_article_content(articles[number - 1]["link"])
            results = analyze_sentiment([articles[number - 1]], [article_content])
            html_response = "<h1>Sentiment Analysis Result</h1>"
            for result in results:
                html_response += f"<p>Article: {result['Article']}</p>"
                html_response += f"<p>Title: {result['title']}</p>"
                html_response += f"<p>Sentiment: {result['sentiment']}</p>"
                html_response += f"<p>Polarity: {result['polarity']}</p>"
                html_response += f"<p>Subjectivity: {result['subjectivity']}</p>"
                html_response += f"<p>Vader Polarity Analysis: {result['Polarity analysis']}</p>"
            return html_response
        else:
            return f"<h1>Error</h1><p>Article number {number} not found.</p>", 404
    else:
        return "<h1>Error</h1><p>Failed to retrieve data from MIT News.</p>", 500