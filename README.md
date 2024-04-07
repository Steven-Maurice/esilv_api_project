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

### Our project 

The API we implemented fetches the papers highlighted by HuggingFace, and computes a vector embedding of each of these papers. The embeddings can then be used to perform sementic search or visualisation. 

__Code__ 

The routes are coded in the server.py file, and make use of the Articles and Article classes. Those two classes were implemented in the huggingfacepapers directory, and contain the logic of our code. 

To run the project, first install the required packages with 
```
pip install -r requirements.txt
```
Then launch the server with 
```
python server.py
```
Starting the server may take a while, as it first needs to load the machine learning model.  

__Endpoints__

```http
GET /get_data?start_date=2024-01-01&end_date=2024-04-06
```

Retrieves papers from https://huggingface.co/papers. 

| Query parameter | Type | Description |
| :--- | :--- | :--- |
| `start_date` | `date` | **Optional**. The date from which we start retrieving papers | 
| `end_date` | `date` | **Optional**. The date until which retrieve papers |

---

```http
GET /articles
```

Returns the list of article previews. 

--- 

```http
GET /article/<id>
```

Fetches the details of a paper and returns it. 

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` | **Required**. A paper identifier (eg: `2404.03592`)  | 

--- 

```http
GET /ml
```

Runs the vector embedding algorithm on each articles. 

--- 

```http
GET /ml/<id>
```

Runs the vector embedding algorithm on a specific article, and returns its embedding. 

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` | **Required**. A paper identifier (eg: `2404.03592`)  |

--- 

```http
GET /ml/search?query=Text+to+image
```

Returns the results of a sementic search of the query. The papers are given a score based on cosine similarity between their embedding and the embedding of the query.  

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `query` | `string` | **Required**. The user query (eg: "Text to image" to find papers related to text to image models)|

--- 

```http
GET /ml/2d_vis
```

Runs a PCA on the papers embeddings to reduce the dimensionnality to 2, and then plot the papers' titles on a graph. 