from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import spacy
import random
from spacy.util import minibatch
from spacy.training.example import Example
app = Flask(__name__)



def scrape_article_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        article_content_element = soup.find(class_="entry-content")
        divs = soup.find_all("div", class_="tdb-block-inner")
        if article_content_element:
            article_content = "\n".join([p.get_text(strip=True) for p in article_content_element.find_all('p')])
            return article_content
        elif divs:
            texte_complet = ""
            for div in divs:
              texte_complet += div.get_text(strip=True) + "\n"
            return texte_complet
        else:
          print("No element with class 'entry-content' found.")
          return None
    else:
        print("Failed to fetch article content.")
        return None



def scrape():
    # URL du site à scraper
    url = 'https://www.actuia.com/'
    response = requests.get(url)
    if response.status_code == 200:
        # Analyser le contenu HTML de la page
        soup = BeautifulSoup(response.content, 'html.parser')
        td_module_flex_tags = soup.find_all(class_="td_module_flex td_module_flex_1 td_module_wrap td-animation-stack")
        articles_data = []
        i=0
        for tag in td_module_flex_tags[:5]:  # Prendre seulement les cinq premiers blocs
            title = tag.find(class_="entry-title td-module-title").get_text(strip=True) if tag.find(class_="entry-title td-module-title") else None
            publication_date = tag.find(class_="entry-date updated td-module-date")['datetime'] if tag.find(class_="entry-date updated td-module-date") else None
            author = tag.find(class_="td-post-author-name").get_text(strip=True) if tag.find(class_="td-post-author-name") else None
            resume = tag.find(class_="td-excerpt").get_text(strip=True) if tag.find(class_="td-excerpt") else None
            read_more_link = tag.find(class_="td-read-more").find('a')['href'] if tag.find(class_="td-read-more") else None
            if read_more_link:
                article_content = scrape_article_content(read_more_link)
            else:
                article_content = None

            article = {
                "id": i,
                "title": title,
                "publication_date": publication_date,
                "author": author,
                "resume": resume,
                "read_more_link": read_more_link,
                "content": article_content
            }
            articles_data.append(article)
            i=i+1
        return articles_data

articles = scrape()

#for article in articles:
#    print(article)

training_data = [
    ("Il avait alors parlé de son projet de bureau à Tokyo, assurant vouloir développer un projet d’excellence pour les Japonais et parfaire les modèles grâce à la langue et à la culture nippones.", "Avancée positive"),
    ("Toutefois, une entreprise avant-gardiste se rendra compte qu’il existe des mises en œuvre de l’IA contraires à l’éthique et potentiellement nuisibles.", "Avancée négative"),
    ("Lorsqu’il s’agit d’IA, les clients exigent que les solutions soient à la fois dignes de confiance, transparentes, responsables et éthiques.", "Avancée positive"),
    ("L’automatisation impulsée par l’IA risque de supprimer des emplois dans de nombreux secteurs, laissant de nombreuses personnes sans travail.", "Avancée négative"),
    ("Pour s’inscrire dans un leadership éthique, les entreprises doivent faire preuve de transparence dans leurs pratiques, leurs sources, l’utilisation des données, les algorithmes et les processus de prise de décision ainsi que sur la reproductibilité et l’audibilité.", "Avancée positive"),
    ("En outre, elles doivent s’appliquer à créer une culture de la responsabilité en élaborant des guidelines et en limitant les biais de leurs systèmes d’IA afin que les décisions prises soient justes et non discriminatoires.", "Avancée positive"),
    ("L’IA peut gérer efficacement les Big Data, en analysant et en tirant des informations utiles à partir de vastes ensembles de données.", "Avancée positive"),
    ("L’objectif est de garantir que les technologies de l’IA soient utilisées à la hauteur de leur potentiel, de manière éthique et responsable.", "Avancée positive"),
    ("Les deepfakes, générés par des algorithmes d’IA, peuvent être utilisés pour tromper et diffuser de fausses informations.", "Avancée négative"),
    ("Elle contribue à améliorer les processus et les flux de travail dans divers domaines, de la logistique à la recherche scientifique.", "Avancée positive"),
    ("Les violations de la vie privée sont une préoccupation majeure, car l’IA peut collecter et analyser des données personnelles sans consentement.", "Avancée négative"),
    ("L’IA peut aggraver les inégalités socio-économiques, car elle peut favoriser ceux qui ont accès à la technologie et aux données.", "Avancée négative"),
]
nlp = spacy.blank("fr")
textcat = nlp.add_pipe("textcat")
textcat.add_label("Avancée positive")
textcat.add_label("Avancée négative")
train_texts, train_cats = zip(*training_data)
train_data = list(zip(train_texts, [{"cats": {"Avancée positive": label == "Avancée positive", "Avancée négative": label == "Avancée négative"}} for label in train_cats]))
random.seed(1)
spacy.util.fix_random_seed(1)
optimizer = nlp.begin_training()
for epoch in range(10):
    random.shuffle(train_data)
    losses = {}
    batches = minibatch(train_data, size=8)
    for batch in batches:
        texts, annotations = zip(*batch)
        example = []
        for i in range(len(texts)):
            doc = nlp.make_doc(texts[i])
            example.append(Example.from_dict(doc, annotations[i]))
        nlp.update(example, drop=0.5, losses=losses)
    

def classer_texte(texte):
    doc = nlp(texte)
    proba_positif = doc.cats["Avancée positive"]
    proba_négatif = doc.cats["Avancée négative"]
    if proba_positif > proba_négatif:
        return "Avancée positive"
    else:
        return "Avancée négative"


@app.route('/get_data')
def get_data():
    return jsonify(articles[:5])  # Renvoie les 5 premiers articles

@app.route('/articles')
def display_articles():
    # Affiche les informations sur les articles, mais pas le contenu
    article_info = [{"Id ":article["id"],"title": article["title"], "publication_date": article["publication_date"],"author": article["author"],"resume": article["resume"]} for article in articles]
    return jsonify(article_info)

@app.route('/article/<int:number>')
def get_article(number):
    # Accède au contenu d'un article spécifié par son numéro
    article = next((article for article in articles if article["id"] == number), None)
    if article:
        return article["content"]
    else:
        return "Article not found", 404


@app.route('/ml/<int:number>', methods=['GET'])
def machine_learning(number=None):
    if number is None:
        return "spécifier un nombre"
    else:
        # Applique le script à un article spécifié par son numéro
        article = next((article for article in articles if article["id"] == number), None)
        if article:
            classification = classer_texte(article['content'])
            return f"Classification pour '{article['title']}' \n{classification}"
            #return "bla ML"
        else:
            return "Article not found", 404


if __name__ == '__main__':
    app.run(debug=True)