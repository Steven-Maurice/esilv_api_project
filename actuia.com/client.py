import requests

# URL du serveur Flask
server_url = "http://127.0.0.1:5000"

# Route "/get_data" pour récupérer une liste d'articles
response = requests.get(f"{server_url}/get_data")
print("GET /get_data Response:")
#print(response.json())
print("-------------------------")

# Route "/articles" pour afficher les informations sur les articles
response = requests.get(f"{server_url}/articles")
print("GET /articles Response:")
print(response.json())
print("-------------------------")

# Route "/article/<number>" pour récupérer le contenu d'un article spécifique
article_number = 1
response = requests.get(f"{server_url}/article/{article_number}")
print(f"GET /article/{article_number} Response:")
print(response.text)
print("-------------------------")


article_number = 5
response = requests.get(f"{server_url}/ml/{article_number}")
print(f"GET /ml/{article_number} Response:")
print(response.text)
print("-------------------------")