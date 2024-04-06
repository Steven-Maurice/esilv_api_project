from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

ARXIV_API_URL = "http://export.arxiv.org/api/query?"

@app.route('/get_data', methods=['GET'])
def get_data():
    query = 'cat:cs.AI'  # This query is for AI articles in Computer Science category
    max_results = 5
    response = requests.get(f"{ARXIV_API_URL}search_query={query}&start=0&max_results={max_results}")
    articles = response.text  # You'll need to parse this XML response
    return jsonify(articles)

@app.route('/articles', methods=['GET'])
def articles():
    # This endpoint should parse the articles fetched in `/get_data`
    # and return a list of articles with article number, title, publication date, etc.
    # For the sake of example, this is left as an exercise to parse and format the XML response correctly.
    return 'List of articles'

@app.route('/article/<number>', methods=['GET'])
def article(number):
    # Fetch and display the content of a specified article by its number
    # This would likely involve fetching all articles and filtering by number
    return f'Content of article {number}'

@app.route('/ml', defaults={'number': None}, methods=['GET'])
@app.route('/ml/<number>', methods=['GET'])
def ml(number):
    # Executes a machine learning script on all articles or a single one, depending on the endpoint accessed
    # This could involve sentiment analysis, summarization, etc.
    if number:
        return f'ML analysis on article {number}'
    else:
        return 'ML analysis on all articles'

if __name__ == '__main__':
    app.run(debug=True)
