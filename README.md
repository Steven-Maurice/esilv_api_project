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

Résumé de notre projet :

Notre API est basée sur l'interface de programmation (API) d'arXiv et permet plusieurs actions liées à la recherche et à l'interaction avec des articles scientifiques. 

Tout d'abord, nous pouvons chercher des données sur arXiv :
On peut les rechercher en interrogeant l'API d'arXiv à l'aide de la fonction fetch_arxiv_data, qui accepte des paramètres tels que la requête de recherche, le point de départ, le nombre maximum de résultats, la méthode de tri et l'ordre de tri.

De plus, nous avons réaliser une analyse de sentiment :
La fonction analyze_sentiment utilise le module SentimentIntensityAnalyzer de NLTK pour déterminer si le résumé d'un article est plutôt positif, négatif ou neutre.

On peut également faire un téléchargement de PDF :
L'endpoint /download/pdf/<paper_id> permet de télécharger directement le PDF d'un article à partir de son ID arXiv.

Nous avons ajouté une gestion des Utilisateurs :
À travers divers endpoints (/signup, /login, /logout, /dashboard, etc.), les utilisateurs peuvent s'inscrire, se connecter, se déconnecter et les administrateurs peuvent gérer les comptes utilisateurs.

Comme le demandait le sujet nous avons également réaliser une fonction permettant l'extraction de détails d'article :
La fonction scrape_article_details permet d'extraire et de présenter les détails d'un article spécifique, comme le titre, le résumé, les auteurs, la date de publication et le lien vers l'article.

L'API offre plusieurs endpoints qui retournent des données au format JSON (/get_data/, /articles, /article/<number>, /ml/<article_id>), ce qui permet une intégration facile avec d'autres applications ou des analyses de données.


