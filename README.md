# Esilv_Api_Project

## Project Overview

Pour notre projet nous avons utiliser Flask. Dans ce projet nous allons récupérer des données du site Arxiv qui rassemble les derniers articles écrit sur l'IA et les analyser grâce à plusieurs Endpoints. Grâce à cela nous pourrons obtenir facilement des informations sur chaque article ou même rechercher es articles dans leur base de données.

## Les Endpoints

Pour ce projet nous avons créé plusieurs Endpoints :
1/ '/get_data'--> permet de récupérer les 5 premières lignes de l'article.
2/ '/articles'--> permet d'afficher' les informations liées à l'article comme le Titre ou encore la date de publication.
3/ '/article/'--> permet d'accéder aux informations (contenues dans '/articles') d'un article à partir de son numéro.
4/ '/ml'--> permet d'analyser le sentiment de l'article grâce au machine learning en utilisant transformers.
5/ '/ml/<int:number>' --> permet de rechercher un article grâce à son numéro et d'analyser le sentiment de cleui-ci.

## Guide d'utilisation

Pour utiliser notre code vous allez devoir commencer par clôner notre repository et installer toutes les bibliothèques utilisées dans le code. Vous allez ensuite devoir exécuter notre code (la partie intitulée server.py). Vous pourrez ensuite utiliser les différentes fonctionnalités que nous avons codées avec les Endpoints.

## Tests

Vous trouverez ici un exemple d'utilisation de notre projet sur la base de données de Axiv en utilisant nos différents Endpoints.