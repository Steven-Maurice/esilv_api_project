Description du projet:

On a choisi l'API de ARXIV car nous sommes en Parcours Recherche et nous voulions créer une API facilitant la création d'Etat de l'Art pour des sujets de Recherche.

L'organisation du code est structurée autour de plusieurs endpoints Flask :

/get_data : Cet endpoint permet de récupérer une liste d'articles basée sur une requête de recherche spécifique. Il supporte des paramètres tels que le terme de recherche et le nombre maximum de résultats à retourner.

/articles : Ici, on fournit les informations de base sur les articles récupérés, comme l'id de l'article, le titre et la date de publication, ce qui est utile pour un aperçu rapide sans accéder au contenu intégral.

/article/<id> : Cet endpoint est conçu pour obtenir le contenu complet d'un article spécifié par son id, ce qui est essentiel pour approfondir l'analyse d'un travail particulier.

/ml/sentiment : En se basant sur textblob, cet endpoint évalue le ton émotionnel des résumés des articles. Cette fonctionnalité est précieuse pour déterminer l'orientation générale d'un article, par exemple, pour identifier rapidement les travaux de recherche positifs sur une nouvelle découverte.Grâce à textblob, on calcule les valeurs de polarité et de subjectivité de chaque article en se basant sur les mots et phrases utilisés dans le texte, en se référant à des listes préétablies de mots connotés positivement ou négativement, et de degrés de subjectivité associés à certains termes.

Exemples d'utilisations:
http://127.0.0.1:5000/get_data (configuration de base affichant 5 articles de recherche sur l'IA)
http://127.0.0.1:5000/get_data?search_query=all:ai&max_results=20 ( possibilité d'augmenter le nombre d'articles affichés en changeant le max_results)
http://127.0.0.1:5000/get_data?search_query=AI%20deep%20learning (si je veux chercher des articles liant IA et deep learning)
http://127.0.0.1:5000/articles

http://127.0.0.1:5000/article/2403.05551v1 (on peut chercher un article précis avec son identifiant)

http://127.0.0.1:5000/ml/sentiment (on peut accéder à la polarité et la subjectivité d'un article, polarité proche de 0 = texte neutre, 1 = texte positif -enthousiame, éloge- -1 = texte négatif -colère, tristesse-, subjectivité proche de 0 = très objectif, 1 = très subjectif)
