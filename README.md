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

### Explanation of the project
    This project develops a Flask API designed to facilitate access to and analysis of scientific articles focused on artificial intelligence (AI), extracted from the arXiv API. This Flask API serves as a bridge to retrieve, store, and process information on the latest AI research. Here is a detailed summary of the functionalities offered by the different endpoints of the API, along with examples of use:

    Endpoint: /get_data
    Utility: Initiates the retrieval of AI articles from the arXiv API, selecting essential information such as the ID, title, publication date, authors, summary, and the PDF URL. The articles are stored in a global list articles_data, facilitating their access for subsequent operations.
    Example of use:
    GET http://localhost:5000/get_data
    Response: {"message": "Articles fetched successfully"}

    Endpoint: /articles
    Utility: Provides an overview of the retrieved articles, displaying their ID, title, publication date, authors, and URL. This allows users to quickly browse the articles without delving into the content details.
    Example of use:
    GET http://localhost:5000/articles

    Endpoint: /article/<number>
    Utility: Provides complete details on a specific article, identified by its ID, including the summary and the PDF URL.
    Example of use:
    GET http://localhost:5000/article/1234567

    Machine Learning Endpoint: /ml/<article_id>
    Utility: Applies a simple text analysis to determine the main keyword of an article specified by its ID and recommends other articles that share this keyword.
    Example of use:
    GET http://localhost:5000/ml/1234567

    Additional ML Endpoint: /search_by_keyword/<keyword>
    Utility: Allows users to search for articles containing a specific keyword in their summary, facilitating targeted research within the vast literature on AI.
    Example of use:
    GET http://localhost:5000/search_by_keyword/neural
    Response (if successful): List of corresponding articles.
    Response (if no results): {"message": "No articles found containing the keyword"}

    This set of endpoints aims to provide an efficient platform for exploring advances in AI. By integrating simplified ML analyses, the project makes information accessible and allows users to discover connections between articles and relevant themes through article summaries.


