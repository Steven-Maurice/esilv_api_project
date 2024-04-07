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

    GET request to http://127.0.0.1:5000/get_data

Response:

    [
      {
        "link": "https://openai.com/blog/introducing-improvements-to-the-fine-tuning-api-and-expanding-our-custom-models-program",
        "number": 0,
        "title": "Introducing improvements to the fine-tuning API and expanding our custom models program"
      },
      {
        "link": "https://openai.com/blog/start-using-chatgpt-instantly",
        "number": 1,
        "title": "Start using ChatGPT instantly"
      },
      {
        "link": "https://openai.com/blog/navigating-the-challenges-and-opportunities-of-synthetic-voices",
        "number": 2,
        "title": "Navigating the Challenges and Opportunities of Synthetic Voices"
      },
      {
        "link": "https://openai.com/blog/sora-first-impressions",
        "number": 3,
        "title": "Sora: first impressions"
      },
      {
        "link": "https://openai.com/blog/global-news-partnerships-le-monde-and-prisa-media",
        "number": 4,
        "title": "Global news partnerships: Le Monde and Prisa Media"
      },
      {
        "link": "https://openai.com/blog/openai-announces-new-members-to-board-of-directors",
        "number": 5,
        "title": "OpenAI announces new members to board of directors"
      },
      {
        "link": "https://openai.com/blog/review-completed--altman-brockman-to-continue-to-lead-openai",
        "number": 6,
        "title": "Review completed & Altman, Brockman to continue to lead OpenAI"
      },
      {
        "link": "https://openai.com/blog/openai-and-elon-musk",
        "number": 7,
        "title": "OpenAI and Elon Musk"
      },
      {
        "link": "https://openai.com/blog/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors",
        "number": 8,
        "title": "Disrupting malicious uses of AI by state-affiliated threat actors"
      },
      {
        "link": "https://openai.com/blog/memory-and-new-controls-for-chatgpt",
        "number": 9,
        "title": "Memory and new controls for ChatGPT"
      },
      {
        "link": "https://openai.com/blog/new-embedding-models-and-api-updates",
        "number": 10,
        "title": "New embedding models and API updates"
      },
      {
        "link": "https://openai.com/blog/democratic-inputs-to-ai-grant-program-lessons-learned-and-implementation-plans",
        "number": 11,
        "title": "Democratic inputs to AI grant program: lessons learned and implementation plans"
      },
      {
        "link": "https://openai.com/blog/how-openai-is-approaching-2024-worldwide-elections",
        "number": 12,
        "title": "How OpenAI is approaching 2024 worldwide elections"
      },
      {
        "link": "https://openai.com/blog/introducing-chatgpt-team",
        "number": 13,
        "title": "Introducing ChatGPT Team"
      },
      {
        "link": "https://openai.com/blog/introducing-the-gpt-store",
        "number": 14,
        "title": "Introducing the GPT Store"
      },
      {
        "link": "https://openai.com/blog/openai-and-journalism",
        "number": 15,
        "title": "OpenAI and journalism"
      },
      {
        "link": "https://openai.com/blog/superalignment-fast-grants",
        "number": 16,
        "title": "Superalignment Fast Grants"
      },
      {
        "link": "https://openai.com/blog/partnership-with-axel-springer-to-deepen-beneficial-use-of-ai-in-journalism",
        "number": 17,
        "title": "Partnership with Axel Springer to deepen beneficial use of AI in journalism"
      },
      {
        "link": "https://openai.com/blog/sam-altman-returns-as-ceo-openai-has-a-new-initial-board",
        "number": 18,
        "title": "Sam Altman returns as CEO, OpenAI has a new initial board"
      },
      {
        "link": "https://openai.com/blog/openai-announces-leadership-transition",
        "number": 19,
        "title": "OpenAI announces leadership transition"
      }
    ]


### /articles (PAUL-HAKIM)
This endpoint returns differents informations about articles retrieved in get_data() such as the article number, title, publication date, article categories, author and the url of the article. The articles are retrieved with the web scraping package BeautifulSoup.
To get a list of all articles with their respective informations, send a GET request to http://127.0.0.1:5000/articles. This will return a JSON object containing a list of articles with their titles and authors.

Request:

    GET request to http://127.0.0.1:5000/articles


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

To get information about a specific article, send a GET request to http://127.0.0.1:5000/article/{number}, where {number} is the number of the article you want to retrieve. This will return a JSON object containing the content of the chosen article .

Request:

    GET request to http://localhost:5000/article/{number}


Response:
    
    "articles": xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


 
    


### /ml (JOSEPH)

This endpoint returns the sentiment analysis of all articles using machine learning with TextBlob.
To get the sentiment analysis of all articles, you must send a GET request to http://127.0.0.1:5000/ml. This will return a JSON object containing the sentiment analysis of all articles.

Request: 

    GET http://localhost:5000/ml

Response:

    "articles": [{"article_id": "2403.20306", "title": "Towards Greener LLMs: Bringing Energy-Efficiency to the Forefront of LLM Inference", "authors":"Jovan Stojkovic, Esha Choukse, Chaojie Zhang, Inigo Goiri, Josep Torrellas", "abstract_url":


### /ml/{number}

This endpoint returns the sentiment analysis of a specific article using machine learning with TextBlob.
To get the sentiment analysis of a specific article, you must send a GET request to http://127.0.0.1:5000/ml/<number>. This is the place where we have the ID of the article. This will return a JSON object containing the sentiment analysis of the article.

Request: 

    GET http://127.0.0.1:5000/ml/{article_number}


Response:

    "articles": [{"article_id": "2403.20306", "title": "Towards Greener LLMs: Bringing Energy-Efficiency to the Forefront of LLM Inference", "authors":"Jovan Stojkovic, Esha Choukse, Chaojie Zhang, Inigo Goiri, Josep Torrellas", "abstract_url":




### Group Members
The members of the group are listed in the composition.txt file.

### Conclusion
In conclusion, xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
