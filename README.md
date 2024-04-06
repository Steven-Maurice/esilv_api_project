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

## AI news API

This project involves creating a Flask API that provides news related to artificial intelligence (AI). We use web scraping techniques to retrieve OpenAI blog post information and VADER-based sentiment analysis.

## Get Started

Make sure you have installed all the necessary dependencies by running the following command in your terminal :

```bash
pip install -r requirements.txt
```

Start development server by running the following command :

```bash
python server.py
```

## Features/Endpoints

### Recovery of items

- **GET /get_data**: Retrieves a list of all available article titles.
- **GET /articles**: Shows information about all available articles.

### Displaying an Article

- **GET /article/<int:number>**: Displays the content of an article specified by its number.

### Sentiment Analysis

- **GET /ml/<int:number>**: Executes a sentiment analysis script with VADER to analyze a specific article.

## Examples

### Retrieving Data

- **GET /get_data**: Retrieves a list of all available article titles.

Response example :

```json
[
    "Title of Article 1",
    "Title of Article 2",
    ...
]
```

- **GET /articles**: Displays information on all available articles.

Response example :

```json
[
  {
    "id": 1,
    "link": "https://openai.com/article/1",
    "image": "https://openai.com/images/article/1.jpg",
    "title": "Title of Article 1",
    "publication_date": "2024-04-05"
  },
  {
    "id": 2,
    "link": "https://openai.com/article/2",
    "image": "https://openai.com/images/article/2.jpg",
    "title": "Title of Article 2",
    "publication_date": "2024-04-06"
  },
  ...
]
```

### Displaying an Article

- **GET /article/1**: Displays the content of the article with ID 1.

Response example :

```json
{
  "id": 1,
  "link": "https://openai.com/article/1",
  "image": "https://openai.com/images/article/1.jpg",
  "title": "Title of Article 1",
  "publication_date": "2024-04-05",
  "content": "Content of Article 1..."
}
```

### Sentiment Analysis

- **GET /ml/1**: Analyzes the sentiment of the article with ID 1.

Response example :

```json
{
  "id": 1,
  "link": "https://openai.com/article/1",
  "title": "Title of Article 1",
  "publication_date": "2024-04-05",
  "content": "Content of Article 1...",
  "sentiment": "positive"
}
```
