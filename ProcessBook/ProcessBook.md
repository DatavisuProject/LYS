Process Book
===================

```Ce document est un cahier d'avancement. Il a pour but de décrire l'évolution du projet.```

----------

## Semaine 1 (16 au 23 novembre 2017)

### Objectifs à remplir

 - Constituer un groupe
 - Choix d’un sujet avec comme thématique la mobilité et les transports
 - Rechercher un jeu de données
 - Définir les visualisations intéressantes (http://fds.design) 


### Constitution du groupe
Notre groupe est constitué de : Arthur Aubret (M2 Informatique), Caroline Gaud (M2 Bioinformatique) et Brice Letcher (M2 Bioinformatique).


### Sujet et jeux de données
Nous avons décidé de travailler sur des données aériennes et plus particulièrement sur celles de l’aéroport de Lyon Saint-Exupéry. Notre idée est de pouvoir représenter, via différentes visualisations, la quantité de vols au départ et à l’arrivé de l’aéroport de façon temporelle (saisons, vacances), spatial (pays, continents) et catégorique (compagnie, nombre de passagers).
Pour des raisons commerciales, les données aériennes semblent compliquées à obtenir. Cependant, nous avons fait une demande auprès des données du Grand Lyon (https://data.grandlyon.com) pour y avoir accès.


### Design de visualisations
Nous avons fait trois designs de visualisations afin de représenter les départs et arrivées de Lyon Saint-Exupéry. Nous aimerions pouvoir répondre aux questions suivantes : où vont les vols ? quand ? quelles sont les destinations privilégiées ? 
Nos représentations impliquent : une carte, une heatmap et un streamgraph.

**Carte** : visualisation des flux via des flèches plus ou moins épaisses en fonction de la quantité de vols (par mois ou saisons ?). Nous voudrions ajouter quelques outils sur la carte

 - Filtrer par rapport à une destination 
 - Filtrer par rapport à une compagnie
 - Zoom sur la carte
 - Scroll over une destination (flèche) pour visualiser les statistiques disponibles sur cette destination

![carte1](https://github.com/DatavisuProject/LYS/blob/master/ProcessBook/Images/Capture1.PNG)

**Heatmap** : visualisation des horaires / jours d’affluence

- Scroll over une case pour visualiser les statistiques disponibles sur cette journée
- Différentes modes : vols et passagers
- Sélection de timeframe pour essayer de comparer les périodes de vacances et non vacances par exemple

![heatmap](https://github.com/DatavisuProject/LYS/blob/master/ProcessBook/Images/Capture2.PNG)

**Streamgraph** : distribution du trafic par airline dans le temps

- Trafic total : vols vs passagers
- Scroll over une aire : statistiques sur cette compagnie

![streamgraph](https://github.com/DatavisuProject/LYS/blob/master/ProcessBook/Images/Capture3.PNG)

Les designs de ces visualisations sont disponibles dans le dossier « DesignSheet ». 


----------

## Semaine 2 (23 au 30 novembre 2017)

### Objectifs à remplir

 - Obtention des données
 - Recherches sur l'état de l'art
 - Rédaction d’un premier article scientifique


### Jeux de données
Nous avons pu obtenir les données demandées au Grand Lyon le 26 novembre. Malheureusement, elles ne correspondent pas à nos attentent puisqu’il s’agit de données en temps réelles et non d’un historique. Après de nombreuses recherches nous n’avons pu trouver les données que nous espérions : l’historique des vols à l’arrivée et au départ de l’aéroport Saint-Exupéry.
Finalement, nous avons pu trouver des données de vols qui se rapprochent de ce que nous voulions pour Lyon sur le site Kaggle (https://www.kaggle.com/freddejn/flights/data). Il s’agit d’un historique de vols aux Etats-Unis de 2015. 


### Design de visualisation
Étant donné que nos données ne correspondent pas exactement à celles attendues, nous avons dû modifier les visualisations établies la semaine précédente. Ainsi, le design de la carte effectué la semaine précédente a été revu comme nous travaillons finalement sur les Etats-Unis.

![carte2](https://github.com/DatavisuProject/LYS/blob/master/ProcessBook/Images/Capture4.PNG)



### Article scientifique
La première version de notre article est disponible dans le dossier « Article ». Il nous a permis de finaliser le cadrage du projet, d’identifier les travaux importants liés au projet et de proposer les premières pistes de conception. 


----------

## Semaine 3 (30 novembre au 7 décembre 2017)

### Objectifs à remplir
- Rédaction peer review

### Peer review
Nous avons réalisé une critique de l'article scientifique rédigé par le groupe 9 (reformulation du problème, état de l'art et propositions). 
Le résultat de cette analyse est disponible sur le Google document https://docs.google.com/spreadsheets/d/1np6Qo-42TQ5IjShXn9ylVW90sb24cR31yQ20aLQc-7g/edit#gid=321460824.


----------

## Semaine 4 (7 au 14 décembre 2017)

### Objectifs à remplir
- Evolution de la problématique : nouveau sujet


### Problématique du projet
Après discussion avec notre encadrant (Romain Vuillemot), nous nous sommes rendus compte que notre problématique était trop vague et que les réalisations que nous comptions faire existaient déjà. Cette semaine a permis de commencer à trouver un autre sujet et de réfléchir aux nouvelles visualisations envisageable. 
Nous gardons le jeu de données sur les vols aériens au USA puisque celui-ci est très bien fourni. Mais nous avons décidé de tourner le problème dans un autre sens : plutôt que de se placer côté passager, nous allons étudier les déplacements des avions.


----------

## Semaine 5 (14 au 21 décembre 2017)

### Objectifs à remplir
- Définir des visualisations


### Visualisations
Comme il a été expliqué précédemment, nous avons complètement changé de sujet (mais en gardant les mêmes données). Il a donc fallu trouver de nouvelles visualisations intéressantes à développer pour répondre à notre problématique :  quels sont les différents patterns d'itinéraires des vols aux USA ?
Pour cela nous avons identifier deux visualisations. La première donnerais un aperçu de l'itinéraire des avions sur des cartes des Etats-Unis. On aurait donc un panel avec une multitudes de petites cartes. La deuxième permettrait de visualiser plus en détail l'itinéraire avec une information temporelle supplémentaire (exemple avec des trains : https://bl.ocks.org/mbostock/5544008).

![Marey's train](https://github.com/DatavisuProject/LYS/blob/master/ProcessBook/Images/Capture5.PNG)


----------

## Semaines 6 et 7 (21 décembre 2017 au 4 janvier 2018)

### Objectifs à remplir
- Créer les visualisations
- Rédiger article scientifique


### Visualisations
Ces deux semaines ont permis d'initier le développement des visualisations et d'arriver à avoir des visualisations globalement fonctionnelles. C'est-à-dire que l'on arrive à générer des mini-cartes des US et de tracer le pattern aérien d'un avion par carte. De l'autre côté, un clique sur une carte permet d'afficher la 'Marey map' correspondante. La visualisation comporte encore quelques erreurs mais on peut visualiser de façon plus précise les vols : quelle est l'origine ? la destination ? quelle est la distance parcourue ? ou encore combien de temps dure le vol ?

### Article
L'article scientifique écrit pour le rendu intermédiaire a du être totalement repris puisque nous avons changé de sujet depuis. Nous avons donc débuté la rédaction en se concentrant dans un premier temps sur la partie 'related work'.



----------

## Semaine 8 (4 au 10 janvier 2018)

### Objectifs à remplir
- Finir les visualisations
- Développer une petite interface web
- Finir la rédaction d'article


### Visualisations
Cette dernière semaine de projet nous a permis de résoudre les erreurs que nous avions. Par ailleurs, d'autres fonctionnalités on été ajoutées comme le fait de pouvoir visualiser sur les Marey map la ponctualité des avions. Des options de filtrages on été insérées : on peut choisir de visualiser un avion en particulier ou encore d'afficher 10 avions qui ont un certain aéroport d'origine. À noter que pour un avion, son aéroport d'origine est celui vers lequel il se rend le plus souvent. Enfin, lorsque l'on survol un trajet (une barre) on peut voir le temps de vol et la distance parcourue. Sur la carte on verra alors le trajet se mettre en évidence pour ce rendre compte du trajet de l'avion.

### Interface
Pour rendre la visualisation plus attractive, nous avons fait un peu de développement html avec l'ajout d'une barre de menu ou encore un descriptif du projet.