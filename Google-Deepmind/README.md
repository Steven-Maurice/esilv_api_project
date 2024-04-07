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


# Google DeepMind API

This project is a Flask web application that provides endpoints to scrape and analyze articles from the Google DeepMind blog.

## Project Overview

The project consists of several components:

1. **Flask Setup**: The project uses Flask, a web development framework for Python, to create the RESTful API endpoints.

2. **Scraping Google Deepmind Blog**: In our Python program, there is a function named `get_articles_titles_random()` that performs web scraping on the Google Deepmind blog. The purpose of this function is to gather information about the latest articles published on the blog, including their titles, publication dates, and URLs. It searches for `<p>` tags with the specified classes in the analyzed HTML page. Then, it extracts the text from each tag and stores it in a list. Only the first five titles are kept and returned.

   There is also a function named `get_articles_titles_by_category()`. It takes a parameter `category_url`, which represents the URL of a specific category of articles on the blog. Finally, the function returns a list containing the titles of the latest articles in the specified category.

3. **Fetching Article Details**: The `get_articles_infos_random()` function retrieves details for a specific article such as author name and description by scraping the article's page.

4. **Fetching Article Content**: The `get_articles_content_random()` function retrieves the full content of a specific article by scraping its page. There's also a function called `get_articles_content_by_category()`. It takes a parameter `category_url`, which represents the URL of a specific category of articles on the blog. The function sends a request to this URL to retrieve the content of articles within that category. The function returns this list containing the content of articles within the specified category.

5. **Sentiment Analysis**: The `analyze_sentiment_total()` function uses TextBlob to perform sentiment analysis on the content of articles, categorizing it as positive, negative, or neutral based on polarity. The `analyze_sentiment()` function uses TextBlob also to perform sentiment analysis on the content of the article we choose (by the number).


The project offers the following endpoints:

- /getCategories: This endpoint provides the categories of articles available on the Google DeepMind blog.
- /ml/<int:number>: This endpoint accepts an article number as input and returns the sentiment analysis result for that specific article.
- /article/<int:number>: This endpoint takes the path to an article and returns its content.
- /get_data: This endpoint returns a simplified version of article data, including titles and publication dates, for all articles.
- /articles: This endpoint returns detailed information about all articles, including titles, publication dates, authors, and descriptions.


## Examples
- To get categories : `/getCategories`

[
  "Company",
  "Events",
  "Impact",
  "Life at DeepMind",
  "Open source",
  "Research",
  "Responsibility & Safety"
]

- To get simplified article data: `/get_data`

[
  "Open-sourcing MuJoCo",
  "Using JAX to accelerate our research",
  "Computational predictions of protein structures associated with COVID-19",
  "TF-Replicator: Distributed Machine Learning for Researchers",
  "Open sourcing TRFL: a library of reinforcement learning building blocks"
]

- To get content of an article with path "some-article-path": `/article/<int:number>`


if we take the number one, we have :
"Yuval Tassa and Saran Tunyasuvunakool\nIn October 2021, we announced that we acquired theMuJoCo physics simulator, and made it freely available for everyone to support research everywhere. We also committed to developing and maintaining MuJoCo as a free, open-source, community-driven project with best-in-class capabilities. Today, we’re thrilled to report that open sourcing is complete and the entire codebase ison GitHub!\nHere, we explain why MuJoCo is a great platform for open-source collaboration and share a preview of our roadmap going forward.\nA platform for collaboration\nPhysics simulators are critical tools in modern robotics research and often fall into these two categories:\nClosed-source, commercial software.\nOpen-source software, often created in academia.\nThe first category is opaque to the user, and although sometimes free to use, cannot be modified and is hard to understand. The second category often has a smaller user base and suffers when its developers and maintainers graduate.\nMuJoCo is one of the few full-featured simulators backed by an established company, which is truly open source. As a research-driven organisation, we view MuJoCo as a platform for collaboration, where roboticists and engineers can join us to develop one of the world’s best robot simulators.\nFeatures that make MuJoCo particularly attractive for collaboration are:\nFull-featured simulator that canmodelcomplexmechanisms.\nReadable, performant, portable code.\nEasily extensible codebase.\nDetailed documentation: both user-facing and code comments.\nWe hope that colleagues across academia and the OSS community benefit from this platform and contribute to the codebase, improving research for everyone.\nPerformance\nAs a C library with no dynamic memory allocation, MuJoCo is very fast. Unfortunately, raw physics speed has historically been hindered by Python wrappers, which made batched, multi-threaded operations non-performant due to the presence of the Global Interpreter Lock (GIL) and non-compiled code. In our roadmap below, we address this issue going forward.\nFor now, we’d like to share some benchmarking results for two common models. The results were obtained on a standard AMD Ryzen 9 5950X machine, running Windows 10.\nThese values were obtained from our testspeed sample code. Notably, control noise is injected into the actuators preventing the system from settling into a fixed state, and are therefore representative of real-world performance.\nRoadmap\nHere’s our near-term roadmap for MuJoCo:\nUnlock MuJoCo’s speed potential with batched, multi-threaded simulation.\nSupport larger scenes with improvements to internal memory management.\nNew incremental compiler with better model composability.\nSupport for better rendering via Unity integration.\nNative support for physics derivatives, both analytical and finite-differenced.\nLearn more\nHelpful resources about MuJoCo:\nMuJoCo’s documentation\nMuJoCo repository on GitHub\nHow to contribute\nWe look forward to receiving your contributions!\nI accept Google's Terms and Conditions and acknowledge that my information will be used in accordance withGoogle's Privacy Policy.\n"

- To get detailed information about all articles: `/articles`

{
  "article1": {
    "publication date ": "23 May 2022",
    "title": "Open-sourcing MuJoCo"
  },
  "article2": {
    "publication date ": "4 December 2020",
    "title": "Using JAX to accelerate our research"
  },
  "article3": {
    "publication date ": "4 August 2020",
    "title": "Computational predictions of protein structures associated with COVID-19"
  },
  "article4": {
    "publication date ": "7 March 2019",
    "title": "TF-Replicator: Distributed Machine Learning for Researchers"
  },
  "article5": {
    "publication date ": "17 October 2018",
    "title": "Open sourcing TRFL: a library of reinforcement learning building blocks"
  }
}

- To get sentiment analysis for the second article: `/ml/1`

0.137981977372221

A positive score suggests a positive sentiment, while a negative score indicates a negative sentiment. In this context, the score suggests a slightly positive sentiment in the analyzed article.


Overall, this project demonstrates the use of web scraping techniques to gather data from the Google DeepMind blog, creating RESTful API endpoints using Flask, performing sentiment analysis on article content, and serving various information related to articles on the blog. The project provides endpoints for retrieving article categories, fetching article details, content, and sentiment analysis results. It showcases how web scraping and API development can be utilized to extract and analyze information from online sources.


