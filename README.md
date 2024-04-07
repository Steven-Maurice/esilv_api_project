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


###  Explanation of our project

Our objective in this project is to fetch information from the chosen site and create different endpoints.

The API that we’ve chosen is ArXiv, which is a free online archive that provides research papers in computer science, machine learning … that covers a large domain of scientific topics, especially AI. 

In order to build our endpoints, here we choose the method with Flask, a python web framework. We define endpoints by using the @app.route() decorator, which specifies the route at which the endpoint will be accessible. We choose here to return responses in JSON format.

We put all endpoints in the same .py file (https://arxiv_extractor.py/) so that it will be easier for people who want to check our code to manipulate.


### 1. Endpoint /get_data

We created an endpoint for /get_data, which asked us to fetch a list of articles from the site.

We defined a retrieve_articles() function. It sends a request to the ArXiv API and retrieves article data. The code retrieves 25 articles related to computer vision (but then if we want other contents we can change it to other topics)

We also extracted some related information to these articles such as the article's title, author, summary, published date, ID, and link. The extracted article information is then stored in a list of dictionaries called articles.

Afterwards we defined the get_data() as a Flask route decorator for the /get_data URL endpoint. When this endpoint is accessed, the retrieve_articles() function is called to fetch the articles.


### 2. Endpoint /articles

We created an endpoint for /articles that displays information about the articles, including the article number, title, publication date, etc., but not the content itself.

So it’s similar to what we did for the first endpoint by creating the retrieve_articles() function to fetch the articles from the ArXiv API, and the result is stored in the articles variable. 


### 3. Endpoint /article/<number>

Then we created another endpoint for /article/<number> that gives us access to the content of a specified article. 

The @app.route('/articles/<int:number>') decorator specifies a new endpoint URL pattern with a variable <int:number> that allows capturing an integer value as a parameter in the URL.
The article() function is defined as the handler for this endpoint, it takes the number parameter representing the article number. 

For example if we want to get access to the 3rd article within the 25 articles, we do /articles/3


### 4. Endpoint /ml

Here we did 2 updates.

- The first one's objective is to give a keyword and the endpoint will provides me with the recommended article (best one among 100 articles) and give us the link that allows us to get access to that article directly. We used elements of machine learning such as TfidfVectorizer, Cosine Similarity, perform_recommendation().

We used a vector representation is created for the article summaries using the TfidfVectorizer class from the scikit-learn library. This transforms the text into numerical vectors representing their content.

Then we define a route /ml/recommendation, which will be used to recommend an article based on a specified keyword. 

Afterwards we defined the perform_recommendation(content) function takes the specified content (in our case, the keyword) and transforms it into a vector representation. 

Then, it calculates the cosine similarities between the content and the article summaries. The index of the article with the highest similarity is returned as the recommendation.

For example we use "image processing" here but of course we can choose other keywords based on our needs.  Then we are redirected to the user to the recommended article link thanks to redirect_article(number) function.

- The second one is based on the idea of the first one, what we added here is to give for example a thematic and ask it to give me different articles arount this topic.

For example we can do /ml/esg to get recommendations of articles around esg

