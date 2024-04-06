from flask import Flask, jsonify
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)


def analyze_sentiment(content):
    # Perform sentiment analysis using TextBlob
    blob = TextBlob(content)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        sentiment = 'positive'
    elif sentiment_score < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return sentiment

def scrape_openai_blog():
    URL = "https://openai.com/blog/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    articles_data = []

    article_titles = soup.find_all('h3', class_='f-subhead-2')
    for title in article_titles:
        article_title = title.text.strip()
        article_link = title.find_parent('a', href=True)['href']
        pub_date_span = title.find_next_sibling("div").find("span", {"aria-hidden": "true"})
        publication_date = pub_date_span.text.strip() if pub_date_span else "Unknown date"

        articles_data.append({
            "title": article_title, 
            "publication_date": publication_date,
            "url": "https://openai.com" + article_link
        })

    return articles_data[:5]

def fetch_article_details(article_url):
    page = requests.get(article_url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    author_element = soup.find('h4', class_='f-subhead-2')  
    description_element = soup.find('div', class_='mt-spacing-4 f-subhead-1 ui-richtext')
    description = description_element.find('p').text.strip() if description_element and description_element.find('p') else 'Description not found'
    
    author_name = author_element.text.strip() if author_element else 'Unknown Author'

    return {"author": author_name, "description": description}


def scrape_openai_blog():
    URL = "https://openai.com/blog/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    articles_data = []

    article_titles = soup.find_all('h3', class_='f-subhead-2')
    for title in article_titles:
        article_title = title.text.strip()
        article_link = title.find_parent('a', href=True)['href']
        pub_date_span = title.find_next_sibling("div").find("span", {"aria-hidden": "true"})
        publication_date = pub_date_span.text.strip() if pub_date_span else "Unknown date"

        articles_data.append({
            "title": article_title, 
            "publication_date": publication_date,
            "url": "https://openai.com" + article_link
        })

    return articles_data

def fetch_article_content(article_url):
    # Adjust the URL to include the '/blog/' segment if it's not present
    if '/blog/' not in article_url:
        article_url = article_url.replace("https://openai.com/", "https://openai.com/blog/")

    page = requests.get(article_url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    # Targeting the specific structure you've provided
    content_element = soup.find('div', class_='ui-richtext')
    if content_element:
        # Extracting all paragraphs inside the div
        paragraphs = content_element.find_all('p')
        article_content = ' '.join(p.text for p in paragraphs)
        return {"content": article_content}
    else:
        print(f"Content not found for article: {article_url}")
        return {"content": "Content not found"}

# Route for performing sentiment analysis on a single article
@app.route('/ml/<int:number>', methods=['GET'])
def ml_analysis(number):
    # Fetch the article content for the specified article number
    articles = scrape_openai_blog()
    if 0 <= number < len(articles):
        article = articles[number]
        article_url = article['url']
        content_response = fetch_article_content(article_url)
        if content_response and 'content' in content_response:
            sentiment = analyze_sentiment(content_response['content'])
            return jsonify({"article": article, "sentiment": sentiment})
        else:
            return jsonify({"error": "Content not found for the specified article."}), 404
    else:
        return jsonify({"error": "Invalid article number."}), 400


@app.route('/article/<path:article_path>', methods=['GET'])
def article_content(article_path):
    base_url = "https://openai.com/"
    full_url = base_url + article_path
    content = fetch_article_content(full_url)
    return jsonify({"content": content})

@app.route('/get_data', methods=['GET'])
def get_data():
    articles = scrape_openai_blog()
    simplified_articles = [{"title": a["title"], "publication_date": a["publication_date"]} for a in articles]
    return jsonify(simplified_articles)

@app.route('/articles', methods=['GET'])
def articles_detailed():
    basic_articles = scrape_openai_blog()
    detailed_articles = []

    for article in basic_articles:
        detailed_info = fetch_article_details(article["url"])
        article.update(detailed_info)  
        detailed_articles.append(article)

    return jsonify(detailed_articles)

if __name__ == '__main__':
    app.run(debug=True)
