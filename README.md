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

### Project 

    1.  Nous avons mis sur pied un projet dans le cadre de notre cours sur le développement web, où nous avons créé une API en utilisant Flask. Notre but était de simplifier l'accès aux informations récentes sur l'intelligence artificielle, en fournissant non seulement des articles en français mais aussi en analysant le ton de ces articles - positif, négatif ou neutre. Pour cela, nous interrogeons NewsAPI pour récupérer les articles, puis nous utilisons un outil appelé VADER pour l'analyse de sentiment.

    2. Voici un aperçu des fonctionnalités que nous avons intégrées :
    
    /get_data : Cette route nous permet de collecter les cinq derniers articles parus sur l'intelligence artificielle. Elle nous donne un aperçu complet incluant le titre, la date de publication, le lien vers l'article, son contenu, et l'auteur, tout cela sous format JSON.
    /articles : Ici, on peut voir une liste des articles récupérés, sans le contenu, pour avoir un aperçu rapide. Ça retourne le titre, la date, le lien et l'auteur de chaque article.
    /article/<number> : Cette commande nous donne accès au contenu complet d'un article spécifique, en se basant sur son numéro. Si l'article n'existe pas, une erreur est retournée.
    /ml : On utilise cette route pour analyser le sentiment de tous les articles qu'on a récupérés. Le résultat est un objet JSON qui liste le titre de chaque article avec le sentiment analysé.
    /ml/<number> : Cela nous permet d'effectuer une analyse de sentiment sur un article en particulier, identifié par son numéro.

    3. Voici comment on utilise notre API :
    
    Pour avoir les dernières nouvelles sur l'IA, on lance un GET sur http://127.0.0.1:5000/get_data.
    Pour un résumé des articles sans contenu, c'est sur http://127.0.0.1:5000/articles.
    Pour les détails d'un article spécifique, par exemple le troisième, on utilise http://127.0.0.1:5000/article/3.
    Pour une analyse du sentiment de tous les articles, on va sur http://127.0.0.1:5000/ml.
    Et pour l'analyse d'un article spécifique, disons le deuxième, c'est http://127.0.0.1:5000/ml/2.
    
    Nous pensons que cette API est un excellent outil pour les chercheurs, les journalistes ou toute personne intéressée par les tendances et les perceptions de l'intelligence artificielle dans l'actualité.

    
