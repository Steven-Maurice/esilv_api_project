import requests

def fetch_endpoint_data(endpoint_url):
    response = requests.get(endpoint_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {endpoint_url}")
        return None

def fetch_article_content(article_url):
    content_url = article_url.replace("https://openai.com/blog/", "")
    return fetch_endpoint_data(f"{base_url}/article/{content_url}")

def fetch_ml_result(article_number):
    return fetch_endpoint_data(f"{base_url}/ml/{article_number}")

def display_articles(articles, detailed=False):
    for index, article in enumerate(articles):
        print(f"Title: {article['title']}")
        print(f"Publication Date: {article['publication_date']}")
        if detailed:
            print(f"Author: {article.get('author', 'N/A')}")
            # Fetch and display the content of the article
            content_response = fetch_article_content(article['url'])
            if content_response and 'content' in content_response:
                print(f"Content: {content_response['content']}")
            else:
                print("Content: N/A")

            # Fetch and display ML result (sentiment analysis)
            ml_result = fetch_ml_result(index)
            if ml_result and 'sentiment' in ml_result:
                print(f"Sentiment: {ml_result['sentiment']}")
            else:
                print("Sentiment: N/A")
        print("")

# URL to your Flask app
base_url = "http://127.0.0.1:5000"

# Fetch and display data from /get_data endpoint
print("Fetching basic article data...\n")
basic_articles = fetch_endpoint_data(f"{base_url}/get_data")
if basic_articles:
    display_articles(basic_articles)

# Fetch and display data from /articles endpoint
print("Fetching detailed article data...\n")
detailed_articles = fetch_endpoint_data(f"{base_url}/articles")
if detailed_articles:
    display_articles(detailed_articles, detailed=True)
