When you run the program, the Flask server starts and begins listening for incoming requests.

You can access the API by making HTTP requests to the different routes provided by the Flask server.

If you want to retrieve article data, you can call the /get_data route. This will return the data of the first five articles in JSON format.

If you want to get information about all the articles, you can call the /articles route. This will return the information (number, title, URL, and publication date) of all the articles as JSON.

If you want to access the content of a specific article based on its number, you can use the /article/<int:number> route. Replace <int:number> with the desired article number. If the article number is valid, you will get the information (title, summary, and URL) of that article in JSON format. If the article is not found, you will receive a JSON error response with the code 404.

If you want to perform sentiment analysis on a specific article based on its number, you can use the /ml/<int:number> route. Replace <int:number> with the article number. This route will use the fetch_articles function to get all the articles, then perform sentiment analysis on the title of the article using the FeelingsAnalysis class in the feelings_analysis.py file. You will then receive the article number and the sentiment analysis result in JSON format. If the article is not found, you will receive a JSON error response with the code 404.

If you access the root of the API (route /), you will simply receive a "Hello, World!" response.

If you want to filter articles by a specific keyword, you can modify the scraping.py file. In the fetch_articles() function, you can set the keyword as a variable in the API request. For example, if you want articles about artificial intelligence, you can set the query variable in the fetch_articles() function as follows: query = "artificial intelligence". This will filter the articles based on that keyword. If you don't specify a keyword, by default, all articles will be retrieved.
