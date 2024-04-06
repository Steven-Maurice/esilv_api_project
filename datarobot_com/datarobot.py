from flask import Flask, Response

from base.request import Request
from base.scrapt_content import return_5_most_recent

app = Flask(__name__)


@app.route("/get_data")
def get_data():
    file_path = f"./windows/article_{0}.html"

    Request(article_number=0).get_html()
    blogs = []
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
        blogs += return_5_most_recent(html_content)

    popup_script = f'<script>alert("Welcome on the scrapted website, we fetched the 5 most recent articles");</script>'

    html_content = html_content.replace("</body>", f"{popup_script}</body>")

    for i in range(1, len(blogs) + 1):
        Request(article_number=i, article_url=blogs[i - 1]).get_html()

    return Response(html_content, mimetype="text/html")


@app.route("/articles")
def articles(articles):
    return articles


@app.route("/article/<int:a_number>")
def article(a_number):
    file_path = f"./windows/article_{a_number}.html"

    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    return Response(html_content, mimetype="text/html")


if __name__ == "__main__":
    app.run(debug=True)
