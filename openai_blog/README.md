Ce projet vise a fournir une API Flask pour récuprer et analyser le contenu du blog d'OpenAI.
L'API permet aux utilisateurs de :

-récupérer les derniers articles publiés sur le blog d'OpenAI.
-obtenir des détails sur chaque article, y compris le titre, l'URL, l'image associée, et la date de publication.
-effectuer une analyse de sentiment sur les titres des articles pour évaluer la positivité ou la négativité des nouvelles récentes concernant l'IA.

Le code du projet est structuré comme suit : 
-'app.py' : le fichier principal qui configure et exécute l'application Flask. il définit les endpoints de l'API et les lie aux fonctions appropriées.
-'scraper.py' : contient la logique pour scraper le blog d'OpenAI et extraire les informations des articles. Cette logique est utilisée par certaines routes dans 'app.py' pour fournir les données nécessaires.
-'sentiment_analysis.py' : implémente la fonctionnalité d'analyse de sentiment en utilisant la bibliothèque NLTK. Cette fonction est appelée pour évaluer le sentiment des titres des articles récupérés.

L'API est accessible localement via 'http://127.0.0.1:5000/' après avoir exécuté 'app.py'. Les endpoints sont les suivants:

-'/get_data' :  récupère les derniers articles du blog d'OpenAI.
-'/articles' : affich une liste des articles avec leur titre, URL, image URL, et date.
-'/article/<number>' : affiche les détails d'un article spécifique en utilisant son numéro dans la liste.
-'/ml/<number> : effectue et retourne une analyse de sentiment sur le titre d'un article spécifique.

