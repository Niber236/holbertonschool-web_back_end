# Pagination

Ce projet a pour but de comprendre et d'implémenter différentes techniques de pagination sur un grand jeu de données (une base de prénoms de bébés au format CSV).

## Objectifs d'apprentissage
* Comment paginer un jeu de données avec de simples paramètres `page` et `page_size`.
* Comment paginer en renvoyant des métadonnées hypermédias (page suivante, page précédente, nombre total de pages).
* Comment créer une pagination résiliente aux suppressions (pour éviter de sauter des éléments si des lignes sont supprimées entre deux requêtes).

## Environnement
* OS: Ubuntu 20.04 LTS
* Langage: Python 3.9
* Style: pycodestyle (version 2.5.*)

## Fichiers et Tâches

| Fichier | Description |
|---|---|
| `0-simple_helper_function.py` | Fonction `index_range` qui calcule les index de début et de fin pour une page donnée. |
| `1-simple_pagination.py` | Classe `Server` qui lit le fichier CSV et renvoie la page demandée (liste de lignes). |
| `2-hypermedia_pagination.py` | Méthode `get_hyper` qui renvoie un dictionnaire contenant les données et les métadonnées de navigation. |
| `3-hypermedia_del_pagination.py` | Méthode `get_hyper_index` qui permet une pagination qui ne casse pas si des éléments sont supprimés de la base de données. |

## Données
Le projet utilise le fichier `Popular_Baby_Names.csv`.