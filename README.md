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


We used the website "https://blog.google/technology/ai/" which displays AI News.
We created an API which scrapes the title, the link(URL) and the publication date of the articles. We were able to scrape 6 articles which are stored in articles.json.
We created several endpoints in server.py :
- /get_data : this endpoint calls the function "scrape()" which fetches the 6 articles and the content   we decided to scrape.
- /nb_articles : gives the number of articles we scraped
- /scraped_data : returns everything we scraped
- /date_articles : this endpoint returns the date of the 6 articles

