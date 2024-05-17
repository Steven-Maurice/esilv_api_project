# Explication du Projet

## Objectif du Projet

Nous avons mis sur pied un projet dans le cadre de notre cours sur le développement web, où nous avons créé une API en utilisant Flask. Notre objectif est de fournir une interface utilisateur interactive pour interroger et visualiser des informations sur des articles scientifiques issus du site "Papers with Code". L'application permet aux utilisateurs de :

- Afficher les articles récents.
- Afficher les 5 articles les mieux notés.
- Rechercher des articles basés sur des mots-clés.
- Obtenir un résumé pour un article spécifique.

## Fonctionnalités

- **/api/display_articles/<num_articles>** : Cette route permet d'afficher les articles récents. Elle renvoie les titres, dates et liens des articles les plus récents sous forme de JSON, en fonction du nombre spécifié.
  
- **/api/top_rated_articles** : Cette route met en lumière les articles les plus appréciés de la communauté. Elle classe les articles en fonction de leur nombre d'étoiles et renvoie les 5 articles les mieux notés sous forme de JSON.
  
- **/api/articles_by_keyword?keyword=<keyword>** : Cette route permet une recherche ciblée d'articles par mots-clés dans les titres. Elle renvoie les titres et liens des articles correspondant aux critères de recherche sous forme de JSON.
  
- **/api/article_abstract?title=<title>** : Cette route permet d'accéder rapidement au résumé d'un article spécifique. Elle identifie et extrait l'abstract basé sur le titre complet fourni et le renvoie sous forme de JSON.

## Utilisation de l'API

- Pour afficher les articles récents, lancez un GET sur `http://127.0.0.1:5000/api/display_articles/<num_articles>`.
  
- Pour afficher les 5 articles les mieux notés, lancez un GET sur `http://127.0.0.1:5000/api/top_rated_articles`.
  
- Pour rechercher des articles par mots-clés, lancez un GET sur `http://127.0.0.1:5000/api/articles_by_keyword?keyword=<keyword>`.
  
- Pour obtenir le résumé d'un article spécifique, lancez un GET sur `http://127.0.0.1:5000/api/article_abstract?title=<title>`.


## Modules et Dépendances

- Utilisation de **Requests** pour les requêtes HTTP.
- Utilisation de **BeautifulSoup** pour le parsing du HTML.
- Le projet utilise également **datetime** pour gérer les dates des articles.
