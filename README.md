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

### Notre projet

Nous avons créé une API permettant de scraper les articles de DeepMind, la filiale intelligence artificielle de Google qui a notamment sorti récemment Gemini, un concurrent à ChatGPT, ainsi qu'AlphaGo, la première intelligence artificielle à battre le champion du monde au jeu de Go : https://www.youtube.com/watch?v=WXuK6gekU1Y

Dans cette API, nous avons 4 **endpoints**:

1. /search : Cet endpoint permet de faire une recherche des derniers articles de blog que DeepMind a publiés. Par défaut, il affiche les 10 derniers mais on peut choisir combien en afficher avec le mot clé article_number.
Ex : /search?article_number=5 permet d'afficher les 5 derniers articles.

2. /articles : Cet endpoint permet, comme avec search, de rechercher les derniers articles de blog de DeepMind mais cette fois en affichant aussi les informations complémentaires sur les articles comme le label, la date de publication ainsi que la description de l'article. De même que pour search, le mot clé article_number fonctionne de la même façon.
Ex : /articles?article_number=5 permet d'afficher les 5 derniers articles de façon détaillée.

3. /article/<number> : Cet endpoint permet de recevoir tout le contenu écrit de l'article <number>.
Ex : /article/1 permet d'afficher tout le contenu écrit du dernier article publié par DeepMind.

4. /ml/<number> : Cet endpoint permet de recevoir le contenu écrit résumé de l'article <number>, nous résumons l'article grâce à un modèle de Deep Learning entraîné OpenSource avec Huggingface : https://huggingface.co/facebook/bart-large-cnn
Ex : /ml/1 permet d'afficher le contenu résumé du dernier article publié par DeepMind.