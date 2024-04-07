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

We have chosen the subject :

    Updates on new AI tools.




### Design
    
Our project uses FastAPI to create the API and BeautifulSoup for web scraping. We have also used the TextBlob library for sentiment analysis.

Endpoints
Here's some screenshots and explannation for each API endpoints:


### /get_data (Contribution Collective)
This endpoint returns a list of articles from the Arxiv site. The articles are retrieved using web scraping with BeautifulSoup.

To get a list of articles, send a GET request to http://localhost:5000/get_data. This will return a JSON object containing information about the latest articles in the AI category.

 Request:

    GET request to http://localhost:5000/get_data

Response:

    {"articles": [{"article_id": "2403.20306", "title": "Towards Greener LLMs: Bringing Energy-Efficiency to the Forefront of LLM Inference", "authors":"Jovan Stojkovic, Esha Choukse, Chaojie Zhang, Inigo Goiri, Josep Torrellas", "abstract_url":"https://arxiv.org/abs/2403.20306"},{"article_id": "2403.20234","title":"Artificial Neural Networks-based Real-time Classification of ENG Signals for Implanted Nerve Interfaces", "authors":"ntonio Coviello , Francesco Linsalata, Umberto Spagnolini, Maurizio Magarini", "abstract_url":"https://arxiv.org/abs/2403.20234"}, {"article_id": "2403.20212", "title": "On Size and Hardness Generalization in Unsupervised Learning for theTravelling Salesman Problem", "authors"; "Yimeng Min, Carla P. Gomes", "abstract_url":"https://arxiv.org/abs/2403.20212"},{"article_id": "2403.20204","title":"The Future ofCombating Rumors? Retrieval, Discrimination, and Generation", "authors":"Junhao Xu, Longdi Xian, Zening Liu, Mingliang Chen, Qiuyang Yin, Fenghua


### /articles (PAUL-HAKIM)
This endpoint returns differents informations about articles retrieved in get_data() such as the article number, title, publication date, article categories, author and the url of the article. The articles are retrieved with the web scraping package BeautifulSoup.
To get a list of all articles with their respective informations, send a GET request to http://localhost:5000/articles. This will return a JSON object containing a list of articles with their titles and authors.

Request:

    GET request to http://localhost:5000/articles


Response:   

        [
      {
        "author": "OpenAI ", 
        "categories": "Announcements, Product", 
        "date": "April 4, 2024", 
        "link": "https://openai.com/blog/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program", 
        "number": 0, 
        "title": "Introducing improvements to the fine-tuning API and expanding our custom models program"
      }, 
      {
        "author": "OpenAI ", 
        "categories": "Announcements, Product", 
        "date": "April 1, 2024", 
        "link": "https://openai.com/blog/start-using-chatgpt-instantly", 
        "number": 1, 
        "title": "Start using ChatGPT instantly"
      }, 
      {
        "author": "OpenAI ", 
        "categories": "Product, Announcements", 
        "date": "March 29, 2024", 
        "link": "https://openai.com/blog/navigating-the-challenges-and-opportunities-of-synthetic-voices", 
        "number": 2, 
        "title": "Navigating the Challenges and Opportunities of Synthetic Voices"
      }, ...

### /article/{number} (IBRAHIM)
This endpoint returns the content of a specified article. The content is retrieved using web scraping with BeautifulSoup.

To get information about a specific article, send a GET request to http://localhost:5000/article/{number}, where {number} is the number of the article you want to retrieve. This will return a JSON object containing the content of the chosen article .

Request:

    GET request to http://localhost:5000/article/{number}


Response:
    
    "articles": xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


 
    


### /ml (JOSEPH)

This endpoint returns the sentiment analysis of all articles using machine learning with TextBlob.
To get the sentiment analysis of all articles, you must send a GET request to http://localhost:5000/ml. This will return a JSON object containing the sentiment analysis of all articles.

Request: 

    GET http://localhost:5000/ml

Response:

    "articles": [{"article_id": "2403.20306", "title": "Towards Greener LLMs: Bringing Energy-Efficiency to the Forefront of LLM Inference", "authors":"Jovan Stojkovic, Esha Choukse, Chaojie Zhang, Inigo Goiri, Josep Torrellas", "abstract_url":


### /ml/{number}

This endpoint returns the sentiment analysis of a specific article using machine learning with TextBlob.
To get the sentiment analysis of a specific article, you must send a GET request to <http://localhost:5000/ml/>. This is the place where we have the ID of the article. This will return a JSON object containing the sentiment analysis of the article.

Request: 

    GET http://localhost:5000/ml/{article_number}


Response:

    "articles": [{"article_id": "2403.20306", "title": "Towards Greener LLMs: Bringing Energy-Efficiency to the Forefront of LLM Inference", "authors":"Jovan Stojkovic, Esha Choukse, Chaojie Zhang, Inigo Goiri, Josep Torrellas", "abstract_url":




### Group Members
The members of the group are listed in the composition.txt file.

### Conclusion
In conclusion, xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
