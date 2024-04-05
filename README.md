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

### Explanation of our code development

We create a Flask web application to explore publications from Google DeepMind. It includes several endpoints to get publication details and analyze them with a simple machine learning tool. 

#### Endpoints
Here’s a brief look at what each endpoint does:

1. **Homepage (`/`)**:
This is the welcome page for the API, just greeting users. When we open the main URL of the application, it will display 
"Welcome to the DeepMind News API!".

2. **Get Data (`/get_data`)**:
This endpoint will give you a quick snapshot of the first five publications. We can use this when you want a brief list of 
what's new.

For example, in 05/04/2024, the outcome of this endpoint will be:
["Neural Fields as Distributions: Signal Processing Beyond Euclidean Space",
"Mirasol3B: A Multimodal Autoregressive Model for Time-Aligned and Contextual Modalities",
"Bayes' Rays: uncertainty quantification for neural radiance fields",
"\u03c02vec: Policy Representations with SuccessorFeatures",
"Kalman Filter for Online Classification of Non-Stationary Data"]

4. **Articles List (`/articles`)**:
It shows a more comprehensive list of publications including details like title, date, authors, and where it was published.
It's great for browsing all the available publications without getting into too much detail.

 For example, in 05/04/2024, the outcome of this endpoint will be:
[{"authors":"Daniel Rebain, Soroosh Yazdani, Kwang Moo Yi, Andrea Tagliasacchi","date":"17 Jun 24\n17 June 2024","number":1,"title":"Neural Fields as Distributions: Signal Processing Beyond Euclidean Space","venue":"CVPR 2024"},{"authors":"AJ Piergiovanni, Isaac Noble, Dahun Kim, Michael S. Ryoo, Victor Gomes, Anelia Angelova","date":"17 Jun 24\n17 June 2024","number":2,"title":"Mirasol3B: A Multimodal Autoregressive Model for Time-Aligned and Contextual Modalities","venue":"CVPR 2024"},
{"authors":"Lily Goli, Cody Reading, Silvia Sellan, Alec Jacobson, Andrea Tagliasacchi","date":"17 Jun 24\n17 June 2024","number":3,"title":"Bayes' Rays: uncertainty quantification for neural radiance fields","venue":"CVPR 2024"},{"authors":"Gianluca Scarpellini*, Ksenia Konyushkova, Claudio Fantacci, Tom Paine, Yutian Chen, Misha Denil","date":"7 May 24\n7 May 2024","number":4,"title":"\u03c02vec: Policy Representations with SuccessorFeatures","venue":"ICLR 2024"},{"authors":"Alexandre Galashov, Michalis Titsias, J\u00f6rg Bornschein, Amal Rannen-Triki, Razvan Pascanu, Yee Whye Teh","date":"7 May 24\n7 May 2024","number":5,"title":"Kalman Filter for Online Classification of Non-Stationary Data","venue":"ICLR 2024"}

6. **Specific Article (`/article/<int:number>`)**:
This endpoints will fetch detailed information about a single publication using its unique number.
We can use this when you need complete information about a particular publication.

For exemple, for article 1:
{"authors":"Daniel Rebain, Soroosh Yazdani, Kwang Moo Yi, Andrea Tagliasacchi","date":"17 Jun 24\n17 June 2024","number":1,"title":"Neural Fields as Distributions: Signal Processing Beyond Euclidean Space","venue":"CVPR 2024"}

8. **Machine Learning Analysis (`/ml` or `/ml/<int:number>`)**:
It Performs keyword extraction on titles of publications. You can run it on all articles or just one. This is handy for quickly finding the main topics in one or more publications.

For exemple, the keywords for first five articles:
{"1":["Fields as Distributions","Signal Processing","Euclidean Space","Processing Beyond Euclidean","Neural Fields"],
"2":["Multimodal Autoregressive Model","Contextual Modalities","Multimodal Autoregressive","Autoregressive Model","Model for Time-Aligned"],
"3":["Bayes' Rays","neural radiance fields","uncertainty quantification","radiance fields","Rays"],
"4":["Policy Representations","Representations with SuccessorFeatures","Policy","Representations","SuccessorFeatures"],
"5":["Filter for Online","Online Classification","Kalman Filter","Non-Stationary Data","Classification of Non-Stationary"]}

The keywords for the second article:
   - {"2":["Multimodal Autoregressive Model","Contextual Modalities","Multimodal Autoregressive","Autoregressive Model","Model for Time-Aligned"]}

Each endpoint is tailored to make exploring and understanding DeepMind's research outputs as straightforward as possible. 

#### Functions
The functions we’ve used in this application:

1. **`scrape_deepmind_publications()`**:
It uses the `requests` library to fetch the page and then parses the HTML with `BeautifulSoup` to extract publication details such as date, title, authors, and venue. The result is a list of dictionaries, each representing a publication. This function pulls publication data directly from the DeepMind research page.

It is called whenever the endpoints `/get_data`, `/articles`, `/article/<int:number>`, or `/ml` are accessed. It ensures that the most up-to-date publication data is used each time.

3. **`keyword_extraction(text, num_keywords=5)`**:
It uses the `yake` library, a tool for automatic keyword extraction. It analyzes the provided text and returns the top keywords based on their relevance and frequency. This function is configurable in terms of how many keywords you want to retrieve.

The function is specifically used in the ML endpoints (`/ml` and `/ml/<int:number>`) to provide quick thematic insights by analyzing publication titles.
