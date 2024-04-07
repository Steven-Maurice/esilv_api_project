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


### Explanation
- We used the NewsAPI, which allows us to execute requests on various articles. We chose to focus our study on the top 5 headlines about artificial intelligence using the API with the following URL: 'https://newsapi.org/v2/top-headlines?, q=Artificial Intelligence&, pageSize=5&, apiKey=2dc9629039304cbd8d0a69e75a3509ee'

- We decided to split our code into 3 files to organize it better. We have the file main, that we have to execute. Then we have the file all_articles_endpoints where we can find the endpoint that concerns our 5 articles,
  we finally have the targeted_article_endpoint file where we can find the endpoint that apply on only one specific article.

In addition to the following explanation of our code, we provided .html file, where you are able to find examples for each implementation with screenshots of the results.

- /get_data :
    This endpoint is used to obtain five articles about AI. It uses entirely the newsAPI with the corresponding URL that gives us the top headlines for our request with many details about each articles (title, description, source name, author, publication date, and URLs). Articles are sorted by the earliest date published first.

- /articles :
    The purpose of this endpoint is to display the main information of the 5 articles we have selected. The information we display includes the article number, title, description, source name, author, publication date, and URL. However, we do not display the detailed content of the selected article. To do this, we use requests.get() from our URL and select the information we are interested in.

- /article/<int:number> :
    This endpoint is meant to be used on only 1 article and returns the entire content of the article and it's URL when the scrapping was sucessful. Otherwise, the content is given by the API and is troncated displaying the number of chars left.

- /ml/<int:number> :
    This endpoint executes a machine learning script to get the sentiment analysis of the article corresponding to the article number provided. In order to get the sentiment analysis, we used the NLTK library which gives us the scores about content of one article. Then, we implemented a function that returns an analysis corresponding to a specific score.


  
