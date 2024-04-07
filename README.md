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

# Our Group

**ATTILA Guillaume, GIRAUDON Baptiste**

### API on IA News

In this project, we have developed an API to fetch news about AI published on 'https://hacker-news.firebaseio.com/'. Hacker News is a platform that allows anyone to share their research/projects with the community. Our API aims to recover AI-related news from this platform, making it easier for users to find the latest developments and discussions in the field of AI.

### Endpoints

    - /get_data: Fetches a list of articles about AI in the 200 recents posts on hacker-news.
    - /articles: Displays information about all of the articles, including the article number, title, publication date, etc., but not the content itself.
    - /article/<id>: Accesses the content of a specified article.
    - /ml : Executes a machine learning script of sentiment analysis on all articles fetched and display it (use of textblob)
    - /ml/<idr>: Executes a machine learning script of sentiment analysis on a specified article and display it (use of textblob)

### Exemples

After use the route to '/get_data', articles are fetched.

'/articles' load a page with : 
      
      {
        "number": 39953707,
        "publication_date": 1712422802,
        "title": "Zep AI (YC W24) Is Hiring a Founding Go Engineer"
      },
      {
        "number": 39953861,
        "publication_date": 1712424092,
        "title": "AI eye-tracking to determine whether child has autism"
      },
      {
        "number": 39946169,
        "publication_date": 1712345430,
        "title": "AI and the Problem of Knowledge Collapse"
      }, 
      
      ....

'/article/39953707' gives details about the article 'Zep AI (YC W24) Is Hiring a Founding Go Engineer' :
    
    {
      "by": "roseway4",
      "id": 39953707,
      "score": 1,
      "time": 1712422802,
      "title": "Zep AI (YC W24) Is Hiring a Founding Go Engineer",
      "type": "job",
      "url": "https://jobs.gem.com/zep/am9icG9zdDre4RbzEeB4wYY7s9TjXwhp"
    }

'/ml/39953707' gives us the sentiment of this articles :
    
    {
      "number": 39953707,
      "sentiment": "neutre"
    }

'/ml/' will display the sentiment for all articles :
    
    {
      "39918245": "neutre",
      "39918500": "négatif",
      "39921673": "neutre",
      "39934696": "négatif",
      "39938126": "neutre",
      "39945104": "neutre",
      "39946169": "neutre",
      "39947967": "neutre",
      "39953707": "neutre",
      "39953861": "neutre"
    }
