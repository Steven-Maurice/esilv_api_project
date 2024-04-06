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


### HOW TO RUN OUR PROJECT

To interact with our API, we recommend using POSTMAN (you can download it on internet very easily), a popular platform for API testing and interaction. Below are example requests for each endpoint, assuming the API is hosted locally at `http://localhost:5000`:

- For `/get_data`: `http://localhost:5000/get_data`
- For `/articles`: `http://localhost:5000/articles`
- For a specific article, such as the second one: `http://localhost:5000/articles/2`
- For the NLP-driven keyword synthesis: `http://localhost:5000/ml`
- For a specific article's author, such as the second one: `http://localhost:5000/authors/2`
- For `/authors`: `http://localhost:5000/authors`
- For having articles with a specific keyword, such as machine: `http://localhost:5000/search/machine`
- For having some statistics on article: `http://localhost:5000/search/statistics`

### Projects Overview

In this project, we delve into the realm of academic research by focusing on Google Scholar, a widely recognized platform for accessing scholarly articles and research papers. Recognizing the gap in official API support for Google Scholar, we have decided to construct our own API to facilitate access to and analysis of scholarly articles. Our API is built upon the capabilities provided by SerpAPI, a service known for its ability to scrape search engine results efficiently and effectively.

#### Created Endpoints

Our API introduces four distinct endpoints, each designed to serve a specific purpose in the exploration of academic literature related to Artificial Intelligence (AI), with a focus on content available in English. Below is a description of these endpoints and their functionalities:

- **/get_data**: This endpoint is the gateway to fetching the most recent articles containing the keyword "artificial intelligence" and ensures that only English-language content is considered. Upon successful execution, it sends a confirmation message to the user, indicating the completion of the data retrieval process.

- **/articles**: Utilizing this endpoint, users can obtain detailed information about the articles fetched by `/get_data`. It provides essential details such as the article's ID, title, abstract, authors' names, and the URL.

- **/articles/number**: This endpoint offers a more focused interaction by allowing users to specify an article of interest through its number (as identified in the data fetched by `/get_data`). The selected article is then opened in the user's default web browser, facilitating immediate access to the full text.

- **/ml**: Drawing upon Natural Language Processing (NLP) algorithms, this endpoint synthesizes a concise set of keywords summarizing the abstracts of articles obtained via `/get_data`. This feature aids in quickly grasping the overarching themes and focal points of the compiled research.

- **/authors/number**: This endpoint enables users to retrieve a list of authors for a specific article identified by its number.

- **/authors**: This endpoint aggregates authorship information across all articles fetched by the API. It lists each author and the number of articles they have contributed to within the dataset, offering insights into the most prolific voices in AI research.

- **/search/keyword**: By incorporating a keyword parameter, this endpoint facilitates targeted searches within the fetched articles, returning only those that mention the specified keyword in their title or abstract. This feature is instrumental in narrowing down research to specific interests or topics within the AI domain.

- **/statistics**: It offers a summary that includes the total number of articles, distribution of publications per author, and identifies the most frequently occurring words in titles and abstracts (excluding common stop words). This endpoint is key for identifying trends and focal areas within the latest AI research.






