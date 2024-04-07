# Esilv_Api_Project

### Project
**Create an API for AI News Overview**

This project involves creating an API that provides news related to Artificial Intelligence (AI). Each group will select an AI-related site (e.g., OpenAI blog) as their source.

### Objective

The goal is to fetch information from the chosen site, either by scraping or through an existing API. You will create several endpoints for different purposes:

    - /get_data: Fetches a list of articles from the site. Retrieving 5 articles might be sufficient.
    - /articles: Displays information about the articles, including the article number, title, publication date, etc., but not the content itself.
    - /article/<number>: Accesses the content of a specified article.
    - /ml or /ml/<number>: Executes a machine learning script. Depending on the desired goal, it applies to either all articles or a single one. For example, sentiment analysis.

You can choose website about many subject like:

    - Updates on new AI tools.
    - News about image generation.
    - Information on new models.
    - Research papers, such as those from ArXiv or Google DeepMind.

### Process

    1. Each group should create a branch named after the names of the group members.
    2. Inside the branch, create a working directory named after the chosen site.
    3. Add a file named composition.txt that lists the members of the group.
    4. Add a section below these rules to explain your project, describe the created endpoints and their uses, and provide examples.

### Implementation

    Rapport Explicatif du Projet

Introduction:
Le projet consiste à créer une application web utilisant le framework Flask en Python. L'objectif principal de l'application est de scraper un blog  pour récupérer des articles, puis de fournir une interface permettant d'accéder à ces articles et d'effectuer un sentiment analysis sur les articles.
Nous avons décider de scrapper  blog- ia.com, un site d'actualité sur l'IA.

Fonctionnalités:

    Fonctions principales:

        scrape_article(url):

        Cette fonction prend une URL d'article en entrée puis Elle envoie une requête HTTP GET à l'URL spécifiée et récupère le contenu de la page web.En utilisant BeautifulSoup, elle extrait le titre de l'article, la date de publication, le contenu et l'auteur de l'article.

        findUrlHref(base_url):

        Cette fonction prend l'URL de base du site web en entrée. Elle parcourt les différentes pages du blog en incrémentant le numéro de la page jusqu'à ce qu'elle ne trouve plus de page suivante.
        Pour chaque page, elle extrait les URLs des articles en utilisant BeautifulSoup. Puis retourne une liste d'URLs uniques des articles trouvés sur le site.


    Scraping du Blog:
        Le programme commence par importer deux fonctions, scrape_article et findUrlHref, depuis un module nommé scrape_info. Ces fonctions sont utilisées pour extraire les informations pertinentes des articles du blog.
        L'URL du blog à scraper est https://blog-ia.com.
        Les URLs de tous les articles sont récupérés en utilisant la fonction findUrlHref.
        Pour chaque URL récupéré, les informations telles que le titre, la date, l'auteur et le contenu de l'article sont extraites en utilisant la fonction scrape_article et stockées dans une liste nommée articles.

    Endpoints Flask:
        /home: Cette root renvoie un template HTML pour la page d'accueil.
        /get_data: Cette root renvoie un template HTML qui affiche tous les articles récupérés à partir du blog.
        /article/{article_id}: Cette root prend un identifiant d'article en paramètre et renvoie un template HTML affichant les détails de cet article.
        /machine_learning: Cette root renvoie un template HTML pour une page dédiée  au sentiment analysis.

    Templates HTML:
        Les templates HTML (home.html, get_data.html, article.html, ml.html) sont utilisés pour présenter les données récupérées et pour fournir une interface utilisateur.

Exécution:
Lorsque le scripts server.py est exécuté, Flask lance un serveur web local. Les utilisateurs peuvent accéder aux différentes roots définies et consulter les articles. 

Ce projet fut très enrichissant :

    La partie scraping :
    Nous avons compris la structure d'un site et comment avoir accès à certaines informations grâce à des requêtes effectuées sur les balises.

    La partie développement web :
    Même si nous avons bien conscience que notre projet peut paraître ridicule, nous avons compris l'essence du développement web : partir d'une feuille blanche et confectionner. Le champ des possibles est immense.

Conclusion : La partie scraping a été plutôt réussie, cependant, nous avons rencontré des difficultés avec l'analyse de sentiment. Nous nous interrogeons même sur la pertinence de ce principe sur nos articles qui ne sont ni des commentaires ni des notations.

Nous vous remercions pour votre enseignement de Git/Python/Linux des deux semestres.

Bien à vous,

 Rannou Maxime
 Pierre Vergote
 Roussez Antoine