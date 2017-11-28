Process Book
===================

>Ce document est un cahier d'avancement. Il a pour but de décrire l'évolution du projet.

----------

Semaine 1 (16 au 23 novembre)
-------------

####Objectifs à remplir :

 - Constituer un groupe
 - Choix d’un sujet avec comme thématique la mobilité et les transports
 - Rechercher un jeu de données
 - Définir les visualisations intéressantes (http://fds.design) 


####Constitution du groupe
Notre groupe est constitué de : Arthur Aubret (M2 Informatique), Caroline Gaud (M2 Bioinformatique) et Brice Letcher (M2 Bioinformatique).


####Sujet et jeux de données
Nous avons décidé de travailler sur des données aériennes et plus particulièrement sur celles de l’aéroport de Lyon Saint-Exupéry. Notre idée est de pouvoir représenter, via différentes visualisations, la quantité de vols au départ et à l’arrivé de l’aéroport de façon temporelle (saisons, vacances), spatial (pays, continents) et catégorique (compagnie, nombre de passagers).
Pour des raisons commerciales, les données aériennes semblent compliquées à obtenir. Cependant, nous avons fait une demande auprès des données du Grand Lyon (https://data.grandlyon.com) pour y avoir accès.


####Design de visualisations
Nous avons fait trois designs de visualisations afin de représenter les départs et arrivées de Lyon Saint-Exupéry. Nous aimerions pouvoir répondre aux questions suivantes : où vont les vols ? quand ? quelles sont les destinations privilégiées ? 
Nos représentations impliquent : une carte, une heatmap et un streamgraph.

**Carte** : visualisation des flux via des flèches plus ou moins épaisses en fonction de la quantité de vols (par mois ou saisons ?). Nous voudrions ajouter quelques outils sur la carte

 - Filtrer par rapport à une destination 
 - Filtrer par rapport à une compagnie
 - Zoom sur la carte
 - Scroll over une destination (flèche) pour visualiser les statistiques disponibles sur cette destination

![carte](https://github.com/DatavisuProject/LYS/ProcessBook/Images/Capture1.PNG "Design carte")

**Heatmap** : visualisation des horaires / jours d’affluence

- Scroll over une case pour visualiser les statistiques disponibles sur cette journée
- Différentes modes : vols et passagers
- Sélection de timeframe pour essayer de comparer les périodes de vacances et non vacances par exemple

**Streamgraph** : distribution du trafic par airline dans le temps

- Trafic total : vols vs passagers
- Scroll over une aire : statistiques sur cette compagnie

Les designs de ces visualisations sont disponibles dans le dossier « DesignSheet ». 


----------

Semaine 2 (23 au 30 novembre)
-------------

####Objectifs à remplir :

 - Obtention des données
 - Recherches sur l'état de l'art
 - Rédaction du premier jet d’un article scientifique


####Jeux de données
Nous avons pu obtenir les données demandées au Grand Lyon le 26 novembre. Malheureusement, elles ne correspondent pas à nos attentent puisqu’il s’agit de données en temps réelles et non d’un historique. Après de nombreuses recherches nous n’avons pu trouver les données que nous espérions : l’historique des vols à l’arrivée et au départ de l’aéroport Saint-Exupéry.
Finalement, nous avons pu trouver des données de vols qui se rapprochent de ce que nous voulions pour Lyon sur le site Kaggle (https://www.kaggle.com/freddejn/flights/data). Il s’agit d’un historique de vols aux Etats-Unis de ? à 2015. 


####Design de visualisation
Étant donné que nos données ne correspondent pas exactement à celles attendues, nous avons dû modifier les visualisations établies la semaine précédente. 


####Article scientifique
Le premier jet de notre article est disponible dans le dossier « Article ». Il nous a permis de finaliser le cadrage du projet, d’identifier les travaux importants liés au projet et de proposer les premières pistes de conception. 
