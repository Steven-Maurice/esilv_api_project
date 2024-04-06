Final Project - Python, Git & Linux

FILE : apgl_project.py

- Project Objective :

This project aims to create a simple and efficient way to retrieve and display the latest research articles on AI from the arXiv website. Using the arXiv API, our Python-based Flask application provides quick access to recent AI articles, making it easier to search the archive.

- Code Organization :

The application is structured into modular functions and Flask routes to provide a clean and understandable codebase. Below is a summary of the key components and their functions:

fetch_articles()
Fetches a list of AI-related articles from arXiv using a search query. It used to include randomness in selecting articles by varying the start index but we removed that to simplify our code. 
To compensate, we decided to take a list of 15 articles instead of 5, ensuring a wide range of articles to be covered. 
However, this randomness feature is still present in the no_flask.ipynb file, the exact same code but with no Flask implementation, using print to replace endpoints. It is simply a backup file in case there was a problem with the Flask API. 
Each article's title, summary, publication date, authors, and link to the PDF are collected.

get_data()
Displays a simple list of fetched article titles in a JSON format. It serves as an initial touchpoint for users to see what articles have been retrieved.
Iterates over the articles list, printing each article's title.

articles()
Provides detailed information about each article, including title, publication date, authors, and a brief summary.
Expands on `print_get_data` by offering more comprehensive details about each article.

article(number)
Displays the full content of a specified article, including its PDF link, enabling users to access the full article.
Accepts an article number as input.

perform_sentiment_analysis(content)
Performs sentiment analysis on all articles. This feature provides insights into the overall tone of the article.
Utilizes the `TextBlob` library to analyze the sentiment of the article's summary, indicating whether the tone is positive, negative, or neutral.

ml(number=None)
Executes sentiment analysis on all fetched articles, presenting a sentiment overview of the latest AI research trends.
Calls `perform_sentiment_analysis` for each article's summary and prints the results.

- Usage :
The Flask application exposes several endpoints for interaction:

/get_data: retrieves the first 5 AI-related articles from the arXiv site.
/articles: displays a brief list of information about each item.
/article/<number>: select an article in order to view its content in detail
/ml and /ml/<number>: displays sentiment analysis on articles, either collectively or individually.

- Running our flask app (make sure to clone the branch first) :
Create a virtual environment env : 'python -m venv env'
Activate the virtual environment : 'env\Scripts\activate' on Windows and 'source env/bin/activate' on macOS and Linux
Set the FLASK_APP environment variable : 'set FLASK_APP=apgl_project.py' on Windows and 'export FLASK_APP=apgl_project.py' on macOS and Linux 
Execute 'flask run'.
Access the endpoints on the web with the provided url.
It's also possible to use 'curl' followed by that same url to access the specific endpoint (remember to use a different terminal then!).
