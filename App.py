
from flask import Flask, jsonify, request
from Scrapping import display_X_article, top_rated_articles, articles_by_keyword, article_abstract

app = Flask(__name__)

@app.route('/api/display_articles/<int:num_articles>', methods=['GET'])
def api_display_articles(num_articles):
    results = display_X_article(num_articles)
    return jsonify(results)

@app.route('/api/top_rated_articles', methods=['GET'])
def api_top_rated_articles():
    results = top_rated_articles()
    return jsonify(results)

@app.route('/api/articles_by_keyword', methods=['GET'])
def api_articles_by_keyword():
    keyword = request.args.get('keyword')
    results = articles_by_keyword(keyword)
    return jsonify(results)

@app.route('/api/article_abstract', methods=['GET'])
def api_article_abstract():
    title = request.args.get('title')
    result = article_abstract(title)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
