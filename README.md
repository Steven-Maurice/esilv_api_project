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

-Executes a Machine Learning script that give a sentimental analysis 

-Filter by author name or surname

-Filter by keyword in the abstrat

### How the code is organised:
                              
-Installation of Packages

-Importation of required libraries (Flack for the creation of our API)

-Initialisation of our API 

-Implementation of our differents endpoints 

-Run the API with app.run(port=5000) from Flask library

### Overview

This project involves the creation of an API, the AI News Overview API, which fetches and displays information about research papers related to Artificial Intelligence (AI) from the ArXiv API. Users can interact with this API to retrieve articles, view article details, perform sentiment analysis on articles, and search for articles containing specific keywords.

## Details about each endpoints & functions

By default, each endpoint gives article that's related to AI in general.

    </get_data> : Endpoint that gives the title and the link of random article related to AI. It calls the function arxiv_data() and extract its data.

    </articles> : Endpoint that extract every relevant information from each articles (title of the article,author,ID,Link,PDF Link, Published Date) from the data retrieve in the arxiv_data() function

    </article/<number>> : Endpoint that gives information for a specific article by giving a number

    </ml> : Endpoint that do a sentimental analysis for each AI related article and gives the title, link and if the abstract of the article is 'positive', 'negative' or 'neutral

    </author/<keyword>> : Endpoint that plays the role of filter by author name/surname. It gives articles information where the name of the author contains the keyword in parameter (example : /author/kevin  ---> results : articles from Kevin Krisciunas/ Kevin Marvel/ Kevin Cahill/ Kevin Lai ...)

    </summary/<keyword>> : Endpoint that plays the role of filter by searching if the article abstract contains our keyword. It gives articles information where the keyword is found in the summary (example : /summary/AI  ---> results : "[...]researchers in AI to some of[...]")


### How to run our project

In order to run the project, I recommend to install Flask (for the API), xml.etree (for reading data from arXiv) and vaderSentiment (for our ML function of sentimental analysis). 
To install them, I recommend to direclty write those codes above in the terminal :

    pip install vaderSentiment
    pip install Flask
    pip install xml.etree

After installing the necessary packages, you can download and run the main.py file on Spyder or other EDI (BE CAREFUL TO DOWNLOAD THE MAIN.PY AND THE FUNCTIONS.PY FILE AND RUN THEM TOGETHER !!!)

Here are where you should find locally the result for each endpoints:

    / : result on http://127.0.0.1:5000/

    /get_data : result on http://127.0.0.1:5000/get_data

    /articles : result on http://127.0.0.1:5000/articles

    /article/<number> : result on http://127.0.0.1:5000/1

    /ml : result on http://127.0.0.1:5000/ml

    /author/<keyword> : result on http://127.0.0.1:5000/author/Li

    /summary/<keyword> : result on http://127.0.0.1:5000/summary/AI




