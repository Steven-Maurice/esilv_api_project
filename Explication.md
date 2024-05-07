# Explication du Projet

## Objectif du Projet

Le but de ce projet est de fournir une interface utilisateur interactive pour interroger et visualiser des informations sur des articles scientifiques issus du site "Papers with Code"
L'application permet aux utilisateurs de :

- Afficher les articles récents.
- Afficher les 5 articles les mieux notés.
- Rechercher des articles basés sur des mots-clés.
- Obtenir un résumé pour un article spécifique.

## Organisation du Code

Le projet contient 4 fonctions citées juste au dessus et une fonction principale ayant pour rôle l'interaction avec l'utilisateur.

## Explication des fonctions

1. **Display Recent Articles (`display_X_article`)** :
   - Permet de visualiser rapidement les dernières publications.
   - Sélectionne les articles les plus récents en se basant sur leur date de publication.
   - Fournit les titres, dates et liens directement à l'utilisateur.

2. **Top Rated Articles (`top_rated_articles`)** :
   - Met en lumière les articles les plus appréciés de la communauté.
   - Classe les articles en fonction de leur nombre d'étoiles.

3. **Articles by Keyword (`articles_by_keyword`)** :
   - Recherche ciblée d'articles par mots-clés dans les titres.
   - Renvoie les titres et liens des articles correspondants aux critères de recherche,idéal pour trouver des articles sur des sujets spécifiques rapidement.

4. **Article Abstract (`article_abstract`)** :
   - Accès rapide au résumé d'un article spécifique.
   - Identifie et extrait l'abstract basé sur le titre complet fourni.

### Modules et Dépendances

- Utilisation de **Requests** pour les requêtes HTTP.
- Utilisation de **BeautifulSoup** pour le parsing du HTML.
- Le projet utilise également **datetime** pour gérer les dates des articles.

