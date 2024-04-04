from flask import Flask, jsonify, request
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

ARXIV_API_URL = "http://export.arxiv.org/api/query"

def get_arxiv_data(search_query="all:ai", max_results=5):
    params = {
        'search_query': search_query,
        'start': 0,
        'max_results': max_results
    }
    response = requests.get(ARXIV_API_URL, params=params)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_arxiv_response(response_text):
    root = ET.fromstring(response_text)
    entries = root.findall('{http://www.w3.org/2005/Atom}entry')
    
    articles_data = []
    for entry in entries:
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        publication_date = entry.find('{http://www.w3.org/2005/Atom}published').text
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text

        articles_data.append({
            'title': title.strip(),
            'publication_date': publication_date,
            'summary': summary.strip()
        })
    
    return articles_data

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        search_query = request.args.get('search_query', 'all:ai')
        max_results = request.args.get('max_results', 5, type=int)
        response_text = get_arxiv_data(search_query, max_results)
        if response_text:
            articles = parse_arxiv_response(response_text)
            return jsonify(articles), 200
        else:
            return jsonify({'error': 'Failed to fetch data from arXiv'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
