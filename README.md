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

### CHARBONNIER / DUFOUR / BONNEAU

This project involved scraping data from Google DeepMind's blog, building a JSON database, and creating an API to query the data.

The first step was to extract article information from the DeepMind website using Selenium. The Python script accessed the site and looped through each article. 
It parsed relevant details like the title, description, date and URL from the HTML.

These scrapings were stored in a list of dictionaries, with each dictionary representing one article's data. 
The list of article dicts was then serialized to a JSON file, creating the database.

Storing the data in a portable JSON format allows it to be loaded and queried independently of the scraping. The file acts as a local database for the article information.

With the database established, the next phase was developing a REST API with Flask to interface with the data.
Routes were defined to perform given tasks keeping in mind that the goal is to make the tools available so that people interested in AI can get information. The API is therefore focused on practicality.

Here are the roots : 

- Get the number of articles in the database (this is more a test root with no real utility for the user other than checking the length of the database)
- Get the url of the articles : we can imagine that the user wants to have a full view over the articles and check them independently
- Get the catagories of the articles : one can look at the distribution of the articles categoires (Research articles, articles about a company ...)

To test the API, the Flask development server was run. Requests were sent using a web browser to call the different endpoints and get dynamic responses with the queried data.
