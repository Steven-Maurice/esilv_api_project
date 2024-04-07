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


## Antoine BUFFANDEAU - Leo DROUIN
## Objective:

The objective of the project is to create a web application that fetches and displays articles from the [MIT News website](https://news.mit.edu/topic/artificial-intelligence2) and performs sentiment analysis on the article content. Users can access various endpoints to retrieve article data, view article details, and analyze article sentiment.

## Run the server:
To run the project, first install the required packages with the following line:

`pip install -r requirements.txt`

Then you can run the server with the following line:

`python server.py`

## Code Organization:

### Scraping (scraping.py):

Contains functions to scrape article data from the MIT News website.

- **scrape_mit_news():** Scrapes the MIT News website to fetch article titles, dates, links, and images. It returns a list of dictionaries containing this information for the latest articles.
- **scrape_article_content(url):** Scrapes the content of a specific article from its URL. It returns the formatted content of the article.

### Analysis (analysis.py):

Implements sentiment analysis on the article content using machine learning models and sentiment analysis libraries.

- **analyze_sentiment(articles, article_texts):** Analyzes the sentiment of articles by fitting a machine learning model on training data and making predictions on the article texts. It returns a list of dictionaries containing sentiment analysis results for each article.

### Routes (routes.py):

Defines routes for the Flask application to handle user requests and responses. Each route corresponds to a specific endpoint:

- **`/`:** Displays the home page of the website with information about the project and available endpoints;
- **`/get_data`:** Fetches and displays a list of 5 latest articles from MIT News;
- **`/articles`:** Displays information about all articles, including titles, dates, links, and images;
- **`/article/<int number>`:** Displays the content of a specified article;
- **`/ml`:** Executes sentiment analysis on all articles and displays the analysis results;
- **`/ml/<int number>`:** Executes sentiment analysis on a specific article and displays the analysis result.

## Conclusion
Overall, the project is organized into separate modules for scraping, analysis, routing, and server initialization, following a structured approach to handle different aspects of the web application.