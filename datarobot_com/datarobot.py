from flask import Flask, Response
import os
from base.request import Request
from base.scrap_content import return_5_most_recent
import codecs
from bs4 import BeautifulSoup
from datetime import datetime
from textblob import TextBlob
from base.interpretation import interpretation

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

            about_author_div = soup.find(
                "div",
                text="About the author",
                class_="uk-text-overline uk-text-muted uk-margin-remove-top uk-margin-bottom",
            )
            if about_author_div:
                author_span = about_author_div.find_next_sibling("div").find(
                    "span", class_="uk-h5 uk-margin-remove-bottom"
                )
                author = (
                    author_span.text.strip() if author_span else "Auteur non trouvé"
                )
            else:
                author = "Auteur non trouvé"

            articles_data.append({"title": title, "date": date, "author": author})

    html_response = "<html><head><title>Liste des Articles</title></head><body>"
    html_response += "<h1>Articles</h1><ul>"
    for article in articles_data:
        html_response += f"<li><strong>Title :</strong> {article['title']} - <strong>Date :</strong> {article['date']} - <strong>Author :</strong> {article['author']}</li>"
    html_response += "</ul></body></html>"

    return Response(html_response, mimetype="text/html")


@app.route("/article/<int:a_number>")
def article(a_number):
    file_path = f"./windows/article_{a_number}.html"

    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    return Response(html_content, mimetype="text/html")


@app.route("/ml", defaults={"number": None})
@app.route("/ml/<number>")
def machine_learning(number):
    dossier_html = "./windows"
    html_response = (
        "<html><head><title>Analyse de Sentiment des Articles</title></head><body>"
    )
    html_response += "<h1>Résultats de l'Analyse de Sentiment</h1><ul>"

    if number:
        articles = [f"article_{number}.html"]
    else:

        articles = [f"article_{i}.html" for i in range(1, 6)]

    for article in articles:
        filepath = os.path.join(dossier_html, article)
        try:
            with codecs.open(filepath, "r", "utf-8") as file:
                soup = BeautifulSoup(file.read(), "html.parser")
                text = soup.get_text()
                analysis = TextBlob(text)
                interpretation_resultat = interpretation(
                    analysis.sentiment.polarity, analysis.sentiment.subjectivity
                )
                html_response += f"<li><strong>{article}</strong>: Polarity = {analysis.sentiment.polarity}, Subjectivity = {analysis.sentiment.subjectivity}, Interpretation = {interpretation_resultat}</li>"
        except FileNotFoundError:
            continue

    html_response += "</ul></body></html>"
    return Response(html_response, mimetype="text/html")


if __name__ == "__main__":
    app.run(debug=True)
