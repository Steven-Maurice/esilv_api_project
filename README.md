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

Résumé de notre projet :

Notre API est basée sur l'interface de programmation (API) d'arXiv et permet plusieurs actions liées à la recherche et à l'interaction avec des articles scientifiques. 

Tout d'abord, nous pouvons chercher des données sur arXiv :
On peut les rechercher en interrogeant l'API d'arXiv à l'aide de la fonction fetch_arxiv_data, qui accepte des paramètres tels que la requête de recherche, le point de départ, le nombre maximum de résultats, la méthode de tri et l'ordre de tri.

De plus, nous avons réaliser une analyse de sentiment :
La fonction analyze_sentiment utilise le module SentimentIntensityAnalyzer de NLTK pour déterminer si le résumé d'un article est plutôt positif, négatif ou neutre.

On peut également faire un téléchargement de PDF :
L'endpoint /download/pdf/<paper_id> permet de télécharger directement le PDF d'un article à partir de son ID arXiv.

Nous avons ajouté une gestion des Utilisateurs :
À travers divers endpoints (/signup, /login, /logout, /dashboard, etc.), les utilisateurs peuvent s'inscrire, se connecter, se déconnecter et les administrateurs peuvent gérer les comptes utilisateurs.

Comme le demandait le sujet nous avons également réaliser une fonction permettant l'extraction de détails d'article :
La fonction scrape_article_details permet d'extraire et de présenter les détails d'un article spécifique, comme le titre, le résumé, les auteurs, la date de publication et le lien vers l'article.

L'API offre plusieurs endpoints qui retournent des données au format JSON (/get_data/, /articles, /article/<number>, /ml/<article_id>), ce qui permet une intégration facile avec d'autres applications ou des analyses de données.

On obtient donc la liste de fonctionnnalité suivante : 
- Sign up :
  Nous avons défini une route '/signup', accessible via les méthodes GET et POST. Cette route permet à un nouvel utilisateur de s'inscrire à l'application en fournissant son email et son mot de passe. Lorsque cette route est appelée avec une requête POST, le code récupère d'abord l'email et le mot de passe fournis par l'utilisateur à partir des données du formulaire. Ensuite, il vérifie si l'email fourni est déjà utilisé par un utilisateur existant dans la base de données. Si tel est le cas, un message d'avertissement est affiché via `flash`, indiquant que l'email est déjà utilisé, et l'utilisateur est redirigé vers la page d'inscription pour réessayer. Si l'email fourni n'est pas déjà utilisé par un autre utilisateur, un nouvel utilisateur est créé avec cet email. Le mot de passe est également défini pour cet utilisateur en utilisant `set_password()`. Ensuite, le nouvel utilisateur est ajouté à la base de données avec `db.session.add(new_user)` et les modifications sont commit avec `db.session.commit()`. L'utilisateur est alors automatiquement connecté en utilisant `login_user(new_user)`, puis est redirigé vers une page nommée 'about' à l'aide de `redirect(url_for('about'))`. Si la méthode de la requête est GET, cela signifie que l'utilisateur souhaite accéder à la page d'inscription. Le code retourne alors le modèle de page 'signup.html', qui est chargé de présenter un formulaire d'inscription où l'utilisateur peut saisir son email et son mot de passe.

- Login : 
  Cette fonction, que nous avons nommée `login` dans notre code, gère le processus de connexion des utilisateurs à l'application. Lorsque cette fonction est appelée, elle vérifie d'abord si la méthode de la requête est POST, ce qui signifie qu'un formulaire a été soumis. Ensuite, elle récupère l'email et le mot de passe fournis par l'utilisateur à partir du formulaire. En utilisant l'email, elle cherche l'utilisateur correspondant dans la base de données. Si l'utilisateur est trouvé et que le mot de passe correspond, l'utilisateur est connecté avec succès en utilisant `login_user(user)`. Si l'email de l'utilisateur se trouve dans une liste d'administrateurs prédéfinie, l'utilisateur est redirigé vers le tableau de bord, sinon il est redirigé vers la page `about`. En cas d'erreur, nous retournons un message d'avertissement informant que l'email ou le mot de passe fourni est invalide. Si la méthode de la requête n'est pas POST, la fonction renvoie le modèle de page HTML pour la page de connexion (`login.html`).

- Log out :
  Cette fonction que nous avons décorée par `@login_required`, gère le processus de déconnexion des utilisateurs d'une application. Avant même d'exécuter le contenu de la fonction, le décorateur `@login_required` vérifie si l'utilisateur est connecté. Si l'utilisateur est connecté, la fonction se poursuit et déconnecte l'utilisateur actuel en appelant `logout_user()`. Ensuite, elle redirige l'utilisateur vers la page de connexion en utilisant `redirect(url_for('login'))`, assurant ainsi qu'une fois déconnecté, l'utilisateur est redirigé vers la page de connexion pour pouvoir se reconnecter ou accéder à d'autres parties de l'application qui nécessitent une authentification.

- Dashboard :
  Cette partie de  définit une route '/dashboard'. Cette route est accessible uniquement aux utilisateurs connectés, car nous l'avons décorée avec `@login_required`, ce qui signifie qu'elle nécessite, comme popur la fonction précédente, de s'identifier au préalable. Le code vérifie d'abord si l'utilisateur actuel est un administrateur en consultant la propriété `is_admin` de l'objet `current_user`. Si l'utilisateur n'est pas un administrateur, un message d'avertissement est affiché signalant un accès non autorisé, puis l'utilisateur est redirigé vers la page nommée 'about'. Si l'utilisateur est un administrateur, le code récupère ensuite tous les utilisateurs enregistrés dans l'application à partir de la base de données. Ces utilisateurs sont ensuite transmis à un modèle de rendu appelé 'dashboard.html', qui est chargé de créer et de présenter une interface utilisateur pour le tableau de bord de l'administrateur.

- Edit_user :
  Cette partie de notre code définit la route '/edit_user/<int:user_id>', où `<int:user_id>` est un paramètre dynamique représentant l'identifiant unique de l'utilisateur à éditer. Cette route permet à l'utilisateur connecté d'éditer les informations d'un utilisateur spécifique. La route est accessible via les méthodes GET et POST, ce qui signifie qu'elle affiche initialement les informations de l'utilisateur à éditer via une requête GET et traite les modifications envoyées via un formulaire POST. Comme pour les routes précédentes, elle est également décorée avec `@login_required`, ce qui garantit que seuls les utilisateurs authentifiés peuvent accéder à cette fonctionnalité. Lorsqu'un utilisateur visite cette page, le code récupère d'abord l'utilisateur spécifié à partir de la base de données en utilisant son identifiant, et s'il n'existe pas, il renvoie une erreur 404. Si la méthode de la requête est POST, cela signifie que l'utilisateur a soumis un formulaire pour mettre à jour les informations de l'utilisateur. Le code récupère alors l'email et le mot de passe fournis par l'utilisateur via le formulaire, met à jour les informations de l'utilisateur dans la base de données, et commit les modifications. Un message de succès est ensuite affiché à l'utilisateur via `flash`, et il est redirigé vers la page de tableau de bord. Si la méthode de la requête est GET, cela signifie que l'utilisateur souhaite visualiser le formulaire d'édition avec les informations actuelles de l'utilisateur. Le code retourne alors finalement 'edit_user.html', en transmettant l'objet utilisateur à ce modèle pour afficher les détails actuels de l'utilisateur dans le formulaire d'édition.

Les deux fonctions suivantes sont accesibles à partir des boutons de la page du tableau de bord. 
- Delete_user :
  Nous définisson alors '/delete_user/<int:user_id>', où `<int:user_id>` est à nouveau un paramètre dynamique représentant l'identifiant unique de l'utilisateur que nous souhaitons supprimer. Cela permet à l'utilisateur connecté de supprimer un utilisateur spécifique de l'application. Lorsque nous y accedons, le code récupère d'abord l'utilisateur spécifié à partir de la base de données en utilisant son identifiant. Si aucun utilisateur correspondant n'est trouvé, une erreur 404 est renvoyée pour indiquer que l'utilisateur à supprimer n'existe pas. Ensuite, le code supprime cet utilisateur de la base de données en utilisant `db.session.delete(user_to_delete)` et commit les modifications avec `db.session.commit()`. Un message de succès est affiché à l'utilisateur via `flash`, indiquant que l'utilisateur a été supprimé avec succès. Enfin, l'utilisateur est redirigé vers la page de tableau de bord à l'aide de `redirect(url_for('dashboard'))`.

- Add_user :
Nous passosn ensuite à '/add_user', accessible uniquement via la méthode POST. Cela permet à un utilisateur authentifié d'ajouter un nouveau utilisateur à l'application. Elle nécessite une session utilisateur authentifiée pour accéder à cette fonctionnalité. Donc, lorsque celle-ci est appelée avec une requête POST, le code récupère d'abord l'email et le mot de passe fournis par l'utilisateur à partir des données du formulaire. Il vérifie ensuite si un utilisateur avec l'email fourni existe déjà dans la base de données. Si tel est le cas, un message d'avertissement est affiché via `flash`, indiquant que l'email est déjà utilisé, puis l'utilisateur est redirigé vers la page de tableau de bord. Si l'email fourni n'est pas déjà utilisé par un autre utilisateur, nous crééons un nouvel utilisateur avec cet email. Le mot de passe est également défini pour cet utilisateur en utilisant `set_password()`. Ensuite, le nouvel utilisateur est ajouté à la base de données avec `db.session.add(new_user)` et les modifications sont commit avec `db.session.commit()`. Nous affichosn un message de succès à l'utilisateur via `flash`, indiquant que le nouvel utilisateur a été ajouté avec succès. Et finalement, l'utilisateur est redirigé vers la page de tableau de bord.

- About : 
    Le chemin '/about', accessible uniquement aux utilisateurs connectés, affiche une page d'informations générales sur l'application. La route renvoie le modèle de page 'about.html' à l'utilisateur. Ce modèle est responsable de la présentation des informations à propos de l'application. Comme la route est protégée par `@login_required`, cela garantit que seuls les utilisateurs authentifiés peuvent accéder à cette page. Si un utilisateur non connecté tente d'accéder à cette route, il sera redirigé vers la page de connexion afin de se connecter avant de pouvoir voir les informations sur la page 'about'.

- Search :
  La route '/search', accessible uniquement aux utilisateurs connectés,  permet aux utilisateurs d'effectuer une recherche dans la base de données articles académiques récupérés depuis arXiv. Lorsque cette route est visitée, notre code récupère les paramètres de recherche depuis les arguments de la requête HTTP GET, tels que la requête de recherche (`query`), l'auteur (`author`), le point de départ (`start`), le nombre maximal de résultats (`max_results`), le tri par (`sortBy`), et l'ordre de tri (`sortOrder`). En fonction des paramètres de recherche fournis, une requête appropriée est construite pour interroger la base de données d'articles. Les résultats de la recherche sont récupérés à l'aide de la fonction `fetch_arxiv_data()` avec les paramètres de recherche fournis. Les données récupérées sont ensuite analysées et traitées pour être présentées correctement. Si aucun résultat n'est trouvé pour la requête de recherche donnée, un message indiquant "Aucun résultat trouvé." est renvoyé à l'utilisateur. Si des résultats sont trouvés, les entrées sont formatées et structurées pour être présentées dans le modèle de page 'search.html'. Chaque entrée contient des informations telles que le titre, les auteurs, le résumé, la date de publication, le lien vers l'article, le sentiment analysé à partir du résumé de l'article, et l'identifiant arXiv. Ces données sont présentées à l'utilisateur via le modèle de rendu 'search.html'.

- Download_pdf :
  Ce code définit '/download/pdf/<paper_id>', où `<paper_id>` est un paramètre dynamique représentant l'identifiant d'un document académique sur arXiv. Cette route permet aux utilisateurs connectés de télécharger le fichier PDF associé à un article académique spécifique en utilisant son identifiant arXiv. Lorsque cette route est appelée, le code construit l'URL de téléchargement PDF en utilisant l'identifiant arXiv fourni dans le paramètre `<paper_id>`. Ensuite, une requête est envoyée à l'URL de téléchargement PDF à l'aide de la bibliothèque `requests`. Si la réponse de la requête a un code de statut 200, cela signifie que le fichier PDF a été trouvé et peut être téléchargé avec succès. Dans ce cas, le contenu de la réponse est renvoyé à l'utilisateur avec un type de contenu `application/pdf`, et le nom du fichier est spécifié dans les en-têtes de la réponse pour indiquer qu'il doit être téléchargé comme une pièce jointe nommée `<paper_id>.pdf`. Si la réponse de la requête n'a pas un code de statut 200, cela indique qu'il y a eu une erreur lors du téléchargement du fichier PDF. Dans ce cas, un message d'erreur est renvoyé à l'utilisateur avec un code d'état 500, indiquant une erreur interne du serveur.

- Endpoints : On définit alors '/endpoints', accessible uniquement aux utilisateurs connectés qui permet aux utilisateurs d'accéder à une page qui présente les différents endpoints disponibles dans l'application.

Afin de naviguer à travers les recherches et qu'elles soient afficher en json, nous avons les fonctions suivantes :
- Get_data :
  Cette partie du code définit '/get_data/' et '/get_data/<topic>'. La première URL est utilisée par défaut lorsque aucun sujet spécifique n'est fourni, tandis que la seconde URL permet de rechercher des articles sur un sujet spécifique. Lorsque cette route est visitée, elle récupère les identifiants et les titres des articles liés au sujet spécifié à partir d'arXiv en utilisant la fonction `fetch_arxiv_data()`. Pour chaque article récupéré, l'identifiant arXiv est extrait, puis l'URL de l'article correspondant est construit. Ensuite, la fonction `scrape_article_details()` est utilisée pour obtenir les détails de chaque article, tels que le titre. Les données des articles sont stockées dans une liste de dictionnaires, où chaque dictionnaire contient l'identifiant et le titre d'un article. Enfin, les données des articles sont retournées sous forme de réponse JSON avec le code d'état HTTP 200, et le type de contenu est spécifié comme 'application/json'. Cette réponse contient une liste de dictionnaires JSON représentant les identifiants et les titres des articles récupérés à partir d'arXiv.

  Accordons un focus sur la méthode `scrape_article_details()` : `scrape_article_details(article_url)` est uen fonction qui nous permet d'extraire les détails d'un article académique à partir de son URL. Elle prend en entrée l'URL de l'article et utilise la bibliothèque BeautifulSoup pour analyser le contenu HTML de la page de l'article. Tout d'abord, la fonction envoie une requête GET à l'URL de l'article pour récupérer le contenu de la page. Si la réponse de la requête n'a pas un code de statut 200, cela signifie qu'il y a eu une erreur lors du chargement de la page de l'article, et la fonction renvoie un message d'erreur indiquant que l'article n'a pas été trouvé ou n'a pas pu être chargé. Si la réponse de la requête a un code de statut 200, la fonction procède à l'extraction des détails de l'article à partir du contenu HTML de la page. Elle recherche les balises HTML appropriées pour extraire le titre, le résumé, les auteurs, la date de publication et le lien vers l'article. Ces détails sont ensuite formatés dans un dictionnaire et retournés par la fonction.

- Articles :
  Nous définissons par la suite une première route '/articles', accessible uniquement aux utilisateurs connectés qui est destinée à afficher une liste d'articles académiques sur un sujet spécifique, dans notre cas, le sujet est défini comme 'AI'. Lorsque cette route est appelée, elle récupère les données des articles liés au sujet à partir d'arXiv en utilisant la fonction `fetch_arxiv_data()`. Pour chaque article récupéré, l'identifiant arXiv est extrait, puis l'URL de l'article correspondant est construit. Ensuite, la fonction `scrape_article_details()` est utilisée pour obtenir les détails de chaque article, tels que le titre, les auteurs, la date de publication et le lien. Les détails des articles sont stockés dans une liste de dictionnaires, où chaque dictionnaire représente un article avec ses détails. Enfin, les données des articles sont retournées sous forme de réponse JSON avec le code d'état HTTP 200, et le type de contenu est spécifié comme 'application/json'. Cette réponse contient une liste de dictionnaires JSON représentant les détails des articles académiques récupérés à partir d'arXiv.

  La deuxième route est définie avec l'URL '/article/' suivie d'un numéro d'article en option. Cette route permet de rechercher un article spécifique en utilisant son numéro d'identification arXiv. Lorsque cette route est visitée, elle récupère les détails de l'article associé au numéro d'identification spécifié en utilisant la fonction scrape_article_details(). Les détails de l'article sont stockés dans une liste de dictionnaires, puis retournés sous forme de réponse JSON avec le code d'état HTTP 200 comme précédemment.

  La troisième route est définie avec l'URL '/ml/' suivie d'un identifiant d'article en option. Cette route est accessible uniquement aux utilisateurs connectés et permet également d'effectuer une analyse de sentiment sur le résumé d'un article académique de la même manière que la première route. Cependant, en plus de cela, elle vérifie également si l'article associé à l'identifiant spécifié est accessible et a été correctement chargé. Si l'article n'est pas trouvé ou s'il échoue à charger, un message d'erreur est renvoyé avec le code d'état HTTP correspondant. Sinon, les résultats de l'analyse de sentiment sont renvoyés comme décrit précédemment.

- Mise en page de notre application :

L'interface utilisateur de notre API utilise HTML pour structurer le contenu et CSS pour le styliser, créant une expérience riche et interactive pour les utilisateurs. Les fichiers HTML définissent la structure de la page, comme l'en-tête, les sections principales, et le pied de page, tandis que le CSS contrôle l'apparence visuelle, telle que les couleurs, les polices, et la disposition des éléments.

La page d'accueil, comme illustrée dans 'index.html', sert de point d'entrée, présentant l'API et ses capacités. Avec des boutons, elle guide les utilisateurs vers des actions clés telles que la recherche dans l'API et la découverte des endpoints disponibles.

La page de tableau de bord ('dashboard.html') est un espace réservé aux administrateurs pour gérer les utilisateurs. Elle est accessible via une authentification sécurisée et offre des fonctionnalités telles que l'ajout, la modification et la suppression des utilisateurs.

Les feuilles de style CSS spécifiques à chaque page, référencées dans les balises <link>, assurent que chaque élément de l'interface est cohérent avec l'identité visuelle de l'API et offre une expérience utilisateur intuitive sur tous les appareils et tailles d'écran grâce à des principes de design responsive.

Les pages 'login.html' et 'signup.html' fournissent des formulaires pour que les utilisateurs puissent se connecter ou s'inscrire, respectivement, avec une esthétique épurée et une fonctionnalité claire, renforçant ainsi la facilité d'utilisation et la sécurité.

- Identification et Sécurité de notre application :

Dans notre application, les identifiants de connexion pour le compte administrateur sont prédéfinis dans le code app.py avec l'adresse email admin@gmail.com et le mot de passe admin. Ces identifiants sont utilisés pour se connecter à l'interface administrateur où des actions privilégiées telles que la gestion des utilisateurs peuvent être effectuées. L'accès au tableau de bord administrateur est strictement réservé aux comptes ayant le statut d'administrateur, ce qui est vérifié à travers une liste d'administrateurs ou un attribut spécifique sur l'objet utilisateur. Si un utilisateur non administrateur tente d'accéder au tableau de bord, un mécanisme de protection implémenté par le décorateur @login_required et des vérifications supplémentaires de statut redirige l'utilisateur vers la page de connexion, assurant ainsi que les zones sensibles de l'application restent inaccessibles aux utilisateurs non autorisés. De plus, l'accès aux pages qui requièrent une session utilisateur active est également restreint ; les utilisateurs non connectés ou non inscrits seront redirigés vers des pages de connexion ou d'inscription, renforçant la sécurité de l'application et protégeant les informations sensibles des utilisateurs.
