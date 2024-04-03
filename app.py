# -*- coding: utf-8 -*-

from flask import Flask, request, Response, render_template
import requests
import feedparser

app = Flask(__name__)

ARXIV_API_URL = "http://export.arxiv.org/api/query"

@app.route('/')
def about():
    return render_template('about.html')


@app.route('/search')
def search():
    query = request.args.get('query', '')
    start = request.args.get('start', '0')
    max_results = request.args.get('max_results', '10')
    sortBy = request.args.get('sortBy', 'lastUpdatedDate')
    sortOrder = request.args.get('sortOrder', 'descending')  
    params = {
        "search_query": query if query else "e",
        "start": start, 
        "max_results": max_results,
        "sortBy": sortBy, 
        "sortOrder": sortOrder
        
 
    }
    response = requests.get(ARXIV_API_URL, params=params)
    feed = feedparser.parse(response.content)

    if not feed.entries:
        return render_template('search.html', entries=[], message="No results found.")

    entries = []
    for entry in feed.entries:
        authors = [author.name for author in entry.authors] if entry.authors else 'Anonymous'
        entry_data = {
            'title': entry.title,
            'authors': ', '.join(authors),
            'summary': entry.summary,
            'published': entry.published,
            'link': entry.link
        }
        entry_data['arxiv_id'] = entry.id.split('/abs/')[-1]  
        entries.append(entry_data)

    return render_template('search.html', entries=entries)

@app.route('/download/pdf/<paper_id>')
def download_pdf(paper_id):
    pdf_url = f"https://arxiv.org/pdf/{paper_id}.pdf"
    response = requests.get(pdf_url)
    # Ensure the request was successful before returning the response
    if response.status_code == 200:
        return Response(
            response.content,
            mimetype='application/pdf',
            headers={"Content-Disposition": f"attachment;filename={paper_id}.pdf"}
        )
    else:
        return f"Error downloading PDF: Status {response.status_code}", 500


if __name__ == '__main__':
    app.run(debug=True)
