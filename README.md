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


# OpenAI Blog Scraper & Sentiment Analysis

This project is a Flask web application that provides endpoints to scrape and analyze articles from the OpenAI blog.

## Project Overview

The project consists of several components:

1. **Scraping OpenAI Blog**: The `scrape_openai_blog()` function scrapes the OpenAI blog homepage to gather information about the latest articles. It collects data such as article titles, publication dates, and URLs.

2. **Fetching Article Details**: The `fetch_article_details()` function retrieves details for a specific article such as author name and description by scraping the article's page.

3. **Fetching Article Content**: The `fetch_article_content()` function retrieves the full content of a specific article by scraping its page.

4. **Sentiment Analysis**: The `analyze_sentiment()` function uses TextBlob to perform sentiment analysis on the content of an article, categorizing it as positive, negative, or neutral based on polarity.

## Endpoints

The project provides the following endpoints:

- `/ml/<int:number>`: This endpoint takes an article number as input and returns the sentiment analysis result for that article.
- `/article/<path:article_path>`: This endpoint takes the path to an article and returns its content.
- `/get_data`: This endpoint returns a simplified version of article data, including titles and publication dates, for all articles.
- `/articles`: This endpoint returns detailed information about all articles, including titles, publication dates, authors, and descriptions.

## Examples

- To get sentiment analysis for the third article: `/ml/2`
- To get content of an article with path "some-article-path": `/article/some-article-path`
- To get simplified article data: `/get_data`
- To get detailed information about all articles: `/articles`

## How to Use

1. Clone the repository.
2. Install the required dependencies using the following command:

- pip install requests beautifulsoup4 textblob Flask


3. Run the Flask application with `python server.py`.
4. Access the provided endpoints to retrieve OpenAI blog data and perform sentiment analysis.
5. One can see the demosntration f it by running testing.py

## Testing

A test program `testing.py` is provided to demonstrate how to call the API endpoints.

