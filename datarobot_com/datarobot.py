from flask import Flask, Response
import os
from base.request import Request
from base.scrap_content import return_5_most_recent
import codecs
from bs4 import BeautifulSoup
from datetime import datetime

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
def articles():
    dossier_html = "./windows"
    articles_data = []

    for i in range(1, 6):
        filepath = os.path.join(dossier_html, f"article_{i}.html")
        with codecs.open(filepath, "r", "utf-8") as file:
            soup = BeautifulSoup(file.read(), "html.parser")
            title = soup.title.string if soup.title else "Titre non trouvé"
            if soup.title:
                title = soup.title.string.split("|")[0].strip()
            else:
                itle = "Titre non trouvé"

            meta_tag = soup.find("meta", property="article:modified_time")
            if meta_tag:
                date_time_obj = datetime.strptime(
                    meta_tag["content"], "%Y-%m-%dT%H:%M:%S%z"
                )
                date = date_time_obj.strftime("%Y-%m-%d")
            else:
                date = "Date non trouvée"
            articles_data.append({"title": title, "date": date})

    html_response = "<html><head><title>Liste des Articles</title></head><body>"
    html_response += "<h1>Articles</h1><ul>"
    for article in articles_data:
        html_response += f"<li><strong>Titre :</strong> {article['title']} - <strong>Date :</strong> {article['date']}</li>"
    html_response += "</ul></body></html>"

    return Response(html_response, mimetype="text/html")


@app.route("/article/<int:a_number>")
def article(a_number):
    file_path = f"./windows/article_{a_number}.html"

    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    return Response(html_content, mimetype="text/html")


if __name__ == "__main__":
    app.run(debug=True)
