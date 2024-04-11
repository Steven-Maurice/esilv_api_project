# Esilv_Api_Project

## Instructions 

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


## Our Article Analysis API

This API provides functionality to fetch articles from the OpenAI blog, analyze their sentiment, and generate summaries.


### Setup

Before you can run the API, you need to install the required dependencies:

```
pip install -r requirements.txt
```

PyTorch is also required for the transformers library. The installation of PyTorch can vary depending on your system's CUDA version if using a GPU, or you can install the CPU-only version. For the CPU-version it is already specified in the requirements.txt file. 


### Running the API

Execute the following command to run the API:

```
python server.py
```

The API will start and be accessible at `http://127.0.0.1:5000`.


### Endpoints

- `/`: Returns a 'Welcome to the OpenAI Blog API!' message to confirm that the API is operational.
- `/get_data`: Fetches a list of articles from the OpenAI blog.
- `/articles`: Provides metadata for articles, such as title, publication date, and URL.
- `/article/<number>`: Retrieves the content of the article specified by its number.
- `/ml/<number>`: Performs sentiment analysis and summarization on the content of the specified article. It may take a little time for your local machine to sumarize an article. 

