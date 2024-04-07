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



This API provides news related to Artificial Intelligence (AI) from ArXiv site by fetching articles from its API.

### Objectives : 
-Fetches a list of articles from the ArXiv API.  

-Displays information about each articles (id,title,published date,link...) without its content  

-Accesses the content of a specified article.  

-Executes a Machine Learning script  


### How the code is organised:
                              
-Installation of Packages

-Importation of required libraries (flack for the creation of our API)

-Initialisation of our API 

-Implementation of our differents endpoints : 

    1./get_data : result on http://127.0.0.1:5000/get_data
    2./articles : result on http://127.0.0.1:5000/articles
    3./article/$<number>$ : result on http://127.0.0.1:5000/number with number beeing a numbers between 1 and 5
    4./ml : result on http://127.0.0.1:5000/ml