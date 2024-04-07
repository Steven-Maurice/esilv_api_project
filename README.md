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

### Endpoint

## Important Note

Before you start using the AI News API, please ensure you have the `eventregistry` Python package installed, as it is crucial for the API's functionality. You can install this package by running the following command in your terminal or command prompt: **pip install eventregistry**


Our API is designed to deliver news articles focused on artificial intelligence. To achieve this, we leverage a third-party API (News API) that allows us to aggregate news from various media sources. To ensure the relevance and quality of the retrieved articles, we've implemented a quantum filter that selects only the top 20% of newsletters, thus eliminating articles considered as "useless" or less relevant.
Here's an overview of the endpoints available through our API:
* /get_data: Returns the titles of 5 selected articles, providing a quick glimpse into the latest AI news without overwhelming the user with too much information at once.
* /articles: Provides details of 5 articles, including the article number (its URI), title, publication date, and other relevant metadata, except for the article's body. This approach allows for a detailed understanding of the articles while maintaining brevity.
* /article<number>: By inserting the specific URI number of an article, you can access a detailed view of that article, including all its available aspects and information, except for its full content. This enables in-depth exploration of topics of particular interest.
* /ml_positive: Returns 5 articles that have received a positive score in sentiment analysis. This feature is ideal for users looking for uplifting news or positive developments in the field of artificial intelligence.
* /ml_negative: Conversely, this endpoint presents 5 articles with a negative score in sentiment analysis, offering insight into the challenges or critical viewpoints associated with artificial intelligence.



### Exemple of use
This guide assumes the AI News API is hosted locally at http://localhost:5000. Below, you'll find examples of how to interact with each endpoint to utilize the full potential of our API for accessing AI-related news and features.

*http://localhost:5000/get_data
  
*http://localhost:5000/articles

*http://localhost:5000/article/2024-04-314965128

*http://localhost:5000/ml_positive

*http://localhost:5000/ml_negative
