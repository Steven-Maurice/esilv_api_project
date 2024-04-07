

# Esilv_Api_Project group of Brudy Le Roux and Abbadi 

Introduction:

Ce projet à pour but de créer une grand API comportant plusieurs branches chacune s'occupant d'un site ou d'une API permettant de récolter des nouvelles sur l'IA. Pour notre part, on a décidé de se concentrer sur l'API : NEWS API qui répertorie dees articles donc qui portent sur l'IA.

Nous devons donc créer plusieurs points de terminaison (routes) pour divers usages :

 /get_data pour récupérer une liste d'articles
 
 /articles pour afficher des informations sur les articles sans inclure leur contenu
 
 /article/<number> pour accéder au contenu d'un article spécifié
 
  /ml ou /ml/<number> pour exécuter un script de machine learning sur tous les articles ou un article spécifique, comme une analyse de sentiment par exemple.

Passons maintenant à l'implémentation,
```
from flask import Flask, jsonify, request
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from transformers import pipeline
import openai
import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
app = Flask(__name__)
```

Nous avons commencé par importer les bibliothèques nécessaires, y compris Flask pour notre serveur web, requests pour les requêtes HTTP, BeautifulSoup pour analyser le HTML, et plusieurs outils de transformers et nltk pour le traitement du langage naturel. Nous initialisons notre application Flask et téléchargeons des ressources nltk pour préparer l'analyse du texte.

Nous configurons ensuite des pipelines pour la génération de résumés et l'extraction d'entités nommées, ce qui nous permettra d'analyser le contenu des articles. Nous avons également défini une clé API pour l'API News, ce qui nous donne accès aux fonctionnalités avancées de ces services.
```
summarizer = pipeline("summarization")
ner = pipeline("ner")

```
Maintenant on va juste détailler les routes,

Pour /get_data
```
def get_data():
    # Fetch and store article data using News API
    fetch_articles()
    return jsonify({"success": True, "message": "Data fetched successfully", "articles": articles_data})
```
La liste articles_data est prête à stocker les informations des articles récupérés. Cette étape initiale assure que nous avons tout ce dont nous avons besoin pour récupérer, stocker et analyser les données relatives aux articles sur l'intelligence artificielle.

```
def fetch_articles():
    articles_data.clear()
    
    params = {
        'q': 'AI', 
        'pageSize': 5,
        'apiKey': NEWS_API_KEY
    }

    # Make the request to the News API
    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code == 200:
        news_data = response.json()
        for idx, article in enumerate(news_data['articles'], start=1):
           
            pub_date = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            formatted_pub_date = datetime.strftime(pub_date, '%Y-%m-%d %H:%M:%S')
            articles_data.append({
                "id": idx,
                "title": article['title'],
                "publication_date": formatted_pub_date,
                "url": article['url'],
                "content": article['content'] 
            })
```

Dans la fonction fetch_articles(), nous avons créé un mécanisme pour récupérer des articles sur l'intelligence artificielle à partir d'une API de nouvelles externes. Nous avons d'abord nettoyé notre liste d'articles précédents pour garantir que nous travaillons avec des données fraîches à chaque appel. Ensuite, nous avons défini des paramètres de recherche spécifiques, tels que le mot-clé 'AI' pour le sujet, une limite de cinq articles pour la taille de page, et nous avons utilisé notre clé API pour l'authentification.

Nous avons envoyé une requête GET à l'API de nouvelles avec ces paramètres. En cas de succès, nous avons traité la réponse JSON pour extraire les informations pertinentes de chaque article, notamment l'ID de l'article, le titre, la date de publication formatée, l'URL, et le contenu. Ces informations ont été ajoutées à notre liste globale articles_data, qui sert de stockage pour les données des articles récupérés. Cette fonction joue un rôle crucial en fournissant les données nécessaires pour les autres fonctionnalités de notre API.


Pour /articles et /article/number,
Cela réside uniquement dans des sélections d'informations déjà présentes dans get_data


Machine learning:

Dans la définition de ml_analysis, nous avons conçu une fonction capable d'effectuer une analyse de machine learning sur le contenu des articles. Cette fonction est accessible via deux endpoints, /ml et /ml/<int:number>, permettant aux utilisateurs soit d'analyser un article spécifique en fournissant son numéro, soit de recevoir un message d'erreur les invitant à spécifier un numéro d'article.

Notre /ml se compose de 3 fonctions : 

 - Une extraction des mots clés avec le pipeline ner qui va les classer selon les catégories : LOC pour localisation , PER pour personne ou MISC pour le reste
  - un résumé de l'article souhaité
  - la liste des mots les plus utilisées 

Pour faire cela , on va donc crééer des fonctions qui vont aller scraper l'entièreté du contenu des articles car sur news api seulement une partie est communiquée avec l'url en question.

Dans la fonction fetch_full_article_content(url),
```
def fetch_full_article_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # L'exemple utilise 'article', mais tu devras adapter ce sélecteur
        article_content = soup.find('article')
        
        if article_content:
            return article_content.get_text(strip=True)
        else:
            return "Content not found or different HTML structure."
    else:
        return "Failed to retrieve the webpage."
``` 
nous avons conçu un moyen pour récupérer le contenu complet d'un article spécifique à partir de son URL. Nous commençons par envoyer une requête HTTP GET à l'URL fournie. Si la requête réussit et que nous recevons une réponse avec le statut 200, nous utilisons BeautifulSoup pour analyser le contenu HTML de la page.

Nous cherchons ensuite un élément HTML article dans la page, car c'est souvent là que le contenu principal de l'article est stocké. Une fois cet élément trouvé, nous extrayons tout le texte qu'il contient, en veillant à supprimer les espaces blancs superflus pour un résultat plus propre.

Si l'élément article est trouvé et que nous pouvons extraire le texte, nous le retournons. Dans le cas contraire, si l'élément article n'est pas trouvé ou si la structure HTML de la page est différente de celle anticipée, nous retournons un message indiquant que le contenu n'a pas été trouvé ou que la structure est différente. Si la requête initiale échoue pour une raison quelconque (par exemple, si l'URL est incorrecte ou si le serveur ne répond pas), nous retournons un message indiquant l'échec de la récupération de la page web.

Quand un numéro d'article est fourni, la fonction commence par chercher cet article spécifique dans notre collection d'articles stockés. Si l'article est trouvé, nous procédons à récupérer son contenu complet en utilisant son URL. Cette étape est cruciale pour les analyses suivantes car elle nous donne accès au texte intégral sur lequel appliquer nos modèles de NLP.

Une fois le contenu de l'article récupéré, nous effectuons trois analyses principales :


Analyse des tendances :
```
def analyze_trends(text):
    words = word_tokenize(text.lower())  # Tokenize le texte et le convertit en minuscules
    filtered_words = [word for word in words if word.isalnum()]  # Enlève la ponctuation
    stop_words = set(stopwords.words('english'))  # Obtient les stopwords en anglais
    filtered_words = [word for word in filtered_words if not word in stop_words]  # Enlève les stopwords

    # Compte et retourne les mots les plus communs
    word_counts = Counter(filtered_words)
    most_common_words = word_counts.most_common(10)  # Obtient les 10 mots les plus fréquents
    return most_common_words

```
 Nous identifions les mots les plus fréquents dans le texte de l'article, ce qui nous donne des indications sur les sujets ou thèmes principaux abordés.

Extraction d'entités nommées : 
```
def extract_entities(article_content):
    entities = ner(article_content)
    cleaned_entities = {clean_entity(entity["word"]): entity["entity"] for entity in entities}
    return cleaned_entities
```
Nous extrayons les entités telles que les noms de personnes, de lieux ou d'organisations, ce qui enrichit notre compréhension du contenu de l'article.
Génération de résumé : Nous utilisons un modèle de NLP pour créer un résumé concis de l'article, facilitant la consommation de son contenu.


Chacune de ces analyses fournit des informations précieuses sur le contenu de l'article, contribuant à une compréhension plus riche et plus nuancée du texte. Nous prenons soin de gérer les cas où le contenu complet de l'article ne peut être récupéré ou lorsque des erreurs surviennent lors du traitement, en retournant des messages d'erreur appropriés.

Si aucun numéro d'article n'est fourni (en accédant simplement à /ml), nous informons l'utilisateur qu'un numéro d'article doit être spécifié pour procéder à l'analyse. Cette approche assure que les utilisateurs comprennent comment interagir correctement avec notre API pour bénéficier de ses fonctionnalités d'analyse avancées.

Exemple:
Pour vérifier que l'APi est en ligne :
    response = requests.get('http://127.0.0.1:5000/')
    print(response.text)

Pour obtenir les dernières nouvelles sur l'IA :
    response = requests.get('http://127.0.0.1:5000/get_data')
    articles = response.json()
    print(articles)

Pour afficher une liste simplifiée des articles sans leur contenu :
    response = requests.get('http://127.0.0.1:5000/articles')
    article_summaries = response.json()
    for article in article_summaries:
        print(f"ID: {article['id']}, Titre: {article['title']}, Date de publication: {article['publication_date']}")


Remarques :
- il faut obligatoirement commencer par get_data comme requête sinon l'API n'a pas de données sur quoi se baser.

- pour la route /article/number il n'y pas de s à article contrairement à la route /articles


- pour la requête /ml on peut avoir parfois des bugs où la connection est perdue avec l'API, il faut juste arrêter cette dernière et la relancer.
