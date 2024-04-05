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

### Objectives of project

This project is a Flask-based Web API designed to provide information on the latest research findings in the 
site of Deepmind's public research publications page and presenting it to users in a structured format

### Code development

This code defines a simple Flask web application that scrapes publication data from DeepMind's research publication page and provides several endpoints for accessing this data


    - scrape_deepmind_publications used to scrape publication data from Deepmind, it sends a get request to the URL of the site. It looks for an unordered list (ul) with a class of 'list-compact', which is assumed to contain the publications and extract informations from the list.
    - Then by using each flask application routes:
              1. Home route: returns a welcome message
              2. Get data route: call the first function and fetch 5 first publication data
              3. Article route: also fetch information but transform it for display
              4. Sigle article route: fetch specific article
    - The if __name__ == '__main__': check ensures that the Flask app runs only when the script is executed directly, not when imported as a module and start it.

    
