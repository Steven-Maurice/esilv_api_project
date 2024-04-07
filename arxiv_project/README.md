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

## Project Description:

This Flask API interacts with the arXiv API to retrieve and analyze articles related to the field of Artificial Intelligence (AI). It provides several endpoints for fetching article data, accessing article content, and applying machine learning techniques to analyze sentiment and extract keywords from the articles.

## Endpoints:

home: A Flask route that serves as the homepage and lists available endpoints.

### get_data

    GET /get_data:
        Fetches a list of articles from arXiv based on the 'cat:cs.AI' category.
        Returns information about the articles, including title, authors, link, publication date, summary and article number.
        Example: http://127.0.0.1:5000/get_data
The JSON response is an array of objects, each representing an academic article with metadata and content details. Here's a breakdown of the fields within each object:

    authors: An array containing the names of the individuals who authored the article.
    link: A string representing the URL where the article can be accessed on the arXiv website.
    number: A string that serves as the unique identifier for the article on arXiv.
    published: A timestamp indicating when the article was published on arXiv.
    summary: A brief description of the article's content, highlighting the main research points and findings.
    title: The title of the article, which typically gives an idea of the subject matter.

This JSON response is useful for anyone looking to programmatically access information about academic articles, such as researchers or students who need to quickly find articles on specific topics without manually searching the arXiv website. Each object in the array provides a comprehensive overview of an article, allowing users to determine its relevance to their research or interests.

## articles

    GET /articles:
        Fetches a list of articles from arXiv based on the 'cat:cs.AI' category.
        Returns information about the articles, including title, authors, link, publication date, and article number, but not the summary (it was asked to not give the content of the article).
        Example: http://127.0.0.1:5000/articles
When you access the endpoint at http://127.0.0.1:5000/articles, you receive a JSON response containing a list of articles, each with its metadata but without the summary. The JSON response for each article includes several fields:

    authors: A list of the authors of the article.
    link: A URL to the article's page on the arXiv website.
    number: The arXiv identifier of the article.
    published: The publication date and time of the article.
    title: The title of the article.

This endpoint is particularly useful for researchers, students, and anyone interested in obtaining detailed information about academic articles in a programmatic and efficient manner. It allows users to quickly access metadata for multiple articles without navigating through individual web pages.

## article

    GET /article/<article_number>:
        Accesses the content of a specified article based on the article number.
        Returns the article's title, summary, authors, link, publication date, and article number.
        Example: http://127.0.0.1:5000/article/2404.03579
When you access the endpoint with the identifier 2404.03579, you receive a JSON response containing the article's metadata and summary.
The JSON response includes several fields:

    authors: A list of the authors of the article.
    link: A URL to the article's page on the arXiv website.
    number: The arXiv identifier of the article.
    published: The publication date and time of the article.
    title: The title of the article.

This endpoint is particularly useful for researchers, students, and anyone interested in obtaining detailed information about a specific academic article without having to navigate through the arXiv website. It provides a quick and programmatic way to access article content and metadata.
}

## ml

    GET /ml or GET /ml/<article_number>:
        Executes a machine learning script to analyze sentiment and extract keywords from articles.
        If an article number is provided, it applies machine learning techniques to a single article.
        If no article number is provided, it applies machine learning techniques to all articles fetched from arXiv.
        Returns sentiment analysis results (positive, negative, or neutral) and extracted keywords for each article.
        Example: http://127.0.0.1:5000/ml
        http://127.0.0.1:5000/ml/2404.03579
The JSON response is structured as an array of objects, each representing an analysis of an article. Each object contains the following fields:

    keywords: An array of strings representing the main topics or concepts found in the article.
    number: A string representing the unique identifier of the article, which could be an arXiv ID.
    sentiment: A string indicating the overall sentiment detected in the article's text.
    title: The title of the article.

For example, the first object in the provided response indicates that the article with the number "2404.03657v1" has a negative sentiment and keywords related to "video instance segmentation" and "important video understanding". The title of the article is "OW-VISCap: Open-World Video Instance Segmentation and Captioning".

This kind of service can be useful for researchers, publishers, and readers who want to quickly understand the sentiment and key topics of a large number of articles without reading them in full. It can also be used to categorize and recommend articles based on user interests.

## Functions:

fetch_arxiv_articles: A function that constructs a query URL and fetches articles from the arXiv API. It can be used to fetch articles by search query or by specific ID.

analyze_sentiment: A function that uses VADER to analyze the sentiment of a given text.

extract_keywords: A function that uses YAKE to extract keywords from a given text.
