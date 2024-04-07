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

### Project details

We chose the website datarobot.com and expecially the articles about Generative AI and AI in the News.
We chose to retrieve only the 5 most recent articlesabout those 2 subjects.
We created the following endpoints : 

    - get_data: Retrieving the 5 most recent articles, storing them in the windows folder
    - articles: Displays information about the articles: title, publication date and author
    - article/number: Accesses the content of a specified article (number goes from 1 to 5 included)
    - ml and ml/number: Two distict ml process, a sentiment analysis and a summary of the article. (number goes for 1 to 5)

Some additional libraries where needed in the project, you might need to install them manually.
The flask app is in the datarobot.py python file. It's the one you have to run before going to 127.0.0.1:5000
