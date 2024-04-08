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

# Groups

## Julie - Laureen - Virgile

### API on craft.ai blog

Hi there! 👋

We are Julie, Laureen and Virgile. We are financial engineering students at ESILV, La Défense, Paris, France. Within the framework of one of our courses, we decided to made an API, to scrape articles of craft.ai blog.

#### Installation

This API is using Python 3. We recommand using Python 3.11. To install our projects, simply run these commands:

```bash
  cd craft.ai
  pip install -r requirements.txt
  python3 server.py
```

If you want to use our API in dev mode, please launch our API with this command:

```bash
flask --app server.py --debug run
```

#### Endpoints

- /articles : Fetch all articles basic informations on craft.ai blog
- /article/:id : Fetch the article specified with the autor, description, and full article in HTML
- /get_data : Fetch 5 randoms articles from /articles endpoint
- /ml : Applied a sentimental analysis ML on all articles basic informations
- /ml/:id : Applied a sentimental analysis ML based on one article
