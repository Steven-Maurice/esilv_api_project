Final Project - Python, Git & Linux

- Project Objective :

This project aims to create a simple and efficient way to retrieve and display the latest research articles on AI from the arXiv website. Using the arXiv API, our Python code provides quick access to recent AI articles, making it easier to search the archive.

- Code Organization :

The codebase is organized into distinct functions, each handling one question of the exercise. Here's an overview of the functions and their purposes :

fetch_articles()
Fetches a list of AI-related articles from arXiv using a search query. It introduces randomness in selecting articles by varying the start index, ensuring a wide range of articles are covered. Each article's title, summary, publication date, authors, and link to the PDF are collected.

print_get_data(articles)
Displays a simple list of fetched article titles. It serves as an initial touchpoint for users to see what articles have been retrieved.
Iterates over the articles list, printing each article's title.

print_articles_details(articles)
Provides detailed information about each article, including title, publication date, authors, and a brief summary.
Expands on `print_get_data` by offering more comprehensive details about each article.

print_article_content(articles, number)
Displays the full content of a specified article, including its PDF link, enabling users to access the full article.
Accepts an article number as input.

perform_sentiment_analysis(content)
Performs sentiment analysis on all articles. This feature provides insights into the overall tone of the article.
Utilizes the `TextBlob` library to analyze the sentiment of the article's summary, indicating whether the tone is positive, negative, or neutral.

print_sentiment_analysis(articles)
Executes sentiment analysis on all fetched articles, presenting a sentiment overview of the latest AI research trends.
Calls `perform_sentiment_analysis` for each article's summary and prints the results.

- Usage :

When running, the script automatically retrieves the first 5 AI-related articles from the arXiv site. It then displays a brief list of information about each item. The user can select an article in order to view its content in detail. Finally, it displays sentiment analysis on all retrieved articles.