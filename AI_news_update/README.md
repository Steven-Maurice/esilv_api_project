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


Response:(example with article 1)
    
    {
      "content": "We\u00e2\u0080\u0099re adding new features to help developers have more control over fine-tuning and announcing new ways to build custom models with OpenAI. There are a variety of techniques that
      developers can use to increase model performance in an effort to reduce latency, improve accuracy, and reduce costs. Whether it\u00e2\u0080\u0099s extending model knowledge with retrieval-augmented generation
      (RAG), customizing a model\u00e2\u0080\u0099s behavior with fine-tuning, or building a custom-trained model with new domain-specific knowledge, we have developed a range of options to support ourcustomers\u00e2\u0080\u0099 AI implementations. 
      Today, we\u00e2\u0080\u0099re launching new features to give developers more control over fine-tuning with the API and introducing more ways to work with our team of AI experts and researchers to build custom models. 
      We launched the self-serve fine-tuning API for GPT-3.5 in August 2023. Since then, thousands of organizations have trained hundreds of thousands of models using our API. Fine-tuning can help models deeply understand content and augment a model\u00e2\u0080\u0099s existing knowledge and capabilities for a specific task. Our fine-tuning API also supports a larger volume of examples than can fit in a single prompt to achieve higher quality results while reducing cost and latency. Some of the common use cases of fine-tuning include training a model to generate better code in a particular programming language, to summarize text in a specific format, or to craft personalized content based on user behavior.\u00c2\u00a0 For example,\u00c2\u00a0Indeed, a global job matching and hiring platform, wants to simplify the hiring process. As part of this, Indeed launched a feature that sends personalized recommendations to job seekers, highlighting relevant jobs based on their skills, experience, and preferences. They fine-tuned GPT-3.5 Turbo to generate higher quality and more accurate explanations. As a result, Indeed was able to improve cost and latency by reducing the number of tokens in prompt by 80%. This let them scale from less than one million messages to job seekers per month to roughly 20 million. Today, we\u00e2\u0080\u0099re introducing new features to give developers even more control over their fine-tuning jobs, including: Assisted Fine-Tuning At DevDay last November, we announced a Custom Model program designed to train and optimize models for a specific domain, in partnership with a dedicated group of OpenAI researchers. Since then, we've met with dozens of customers to assess their custom model needs and evolved our program to further maximize performance. Today, we are formally announcing our assisted fine-tuning offering as part of the Custom Model program. Assisted fine-tuning is a collaborative effort with our technical teams to leverage techniques beyond the fine-tuning API, such as additional hyperparameters and various parameter efficient fine-tuning (PEFT) methods at a larger scale. It\u00e2\u0080\u0099s particularly helpful for organizations that need support setting up efficient training data pipelines, evaluation systems, and bespoke parameters and methods to maximize model performance for their use case or task. For example, SK Telecom, a telecommunications operator serving over 30 million subscribers in South Korea, wanted to customize a model to be an expert in the telecommunications domain with an initial focus on customer service. They worked with OpenAI to fine-tune GPT-4 to improve its performance in telecom-related conversations in the Korean language. Over the course of multiple weeks, SKT and OpenAI drove meaningful performance improvement in telecom customer service tasks\u00e2\u0080\u0094a 35% increase in conversation summarization quality, a 33% increase in intent recognition accuracy, and an increase in satisfaction scores from 3.6 to 4.5 (out of 5) when comparing the fine-tuned model to GPT-4.\u00c2\u00a0 Custom-Trained Model In some cases, organizations need to train a purpose-built model from scratch that understands their business, industry, or domain. Fully custom-trained models imbue new knowledge from a specific domain by modifying key steps of the model training process using novel mid-training and post-training techniques. Organizations that see success with a fully custom-trained model often have large quantities of proprietary data\u00e2\u0080\u0094millions of examples or billions of tokens\u00e2\u0080\u0094that they want to use to teach the model new knowledge or complex, unique behaviors for highly specific use cases.\u00c2\u00a0 For example, Harvey, an AI-native legal tool for attorneys, partnered with OpenAI to create a custom-trained large language model for case law. While foundation models were strong at reasoning, they lacked the extensive knowledge of legal case history and other knowledge required for legal work. After testing out prompt engineering, RAG, and fine-tuning, Harvey worked with our team to add the depth of context needed to the model\u00e2\u0080\u0094the equivalent of 10 billion tokens worth of data. Our team modified every step of the model training process, from domain-specific mid-training to customizing post-training processes and incorporating expert attorney feedback. The resulting model achieved an 83% increase in factual responses and attorneys preferred the customized model\u00e2\u0080\u0099s outputs 97% of the time over GPT-4. We believe that in the future, the vast majority of organizations will develop customized models that are personalized to their industry, business, or use case. With a variety of techniques available to build a custom model, organizations of all sizes can develop personalized models to realize more meaningful, specific impact from their AI implementations. The key is to clearly scope the use case, design and implement evaluation systems, choose the right techniques, and be prepared to iterate over time for the model to reach optimal performance.\u00c2\u00a0 With OpenAI, most organizations can see meaningful results quickly with the self-serve fine-tuning API. For any organizations that need to more deeply fine-tune their models or imbue new, domain-specific knowledge into the model, our Custom Model programs can help.\u00c2\u00a0 Visit our fine-tuning API docs to start fine-tuning our models. For more information on how we can help customize models for your use case, reach out to us.\u00c2\u00a0",
      "number": 0,
      "title": "Introducing improvements to the fine-tuning API and expanding our custom models program"
    }


 
    


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
