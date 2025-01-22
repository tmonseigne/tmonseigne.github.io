---
layout: post
title: (Très) courte introduction à Python
date: 2023-09-06
description: (Très) courte introduction à Python ou comment faire de l'analyse de données en Science ouverte ?
img: theme/Programmation-Theme.png
tags: [Explication]
author: Thibaut Monseigne
---

* TOC
{:toc}
{: .toc-post}

## Définition

Python est un langage de programmation interprété, multiplateforme, utilisant un typage dynamique fort et possédant une syntaxe conçue pour être lisible et intuitive, ce qui facilite son apprentissage.

* **Langage de programmation** : Comme tout langage (ou langue), un langage de programmation est nécessaire afin de communiquer, dans ce cas, avec la machine. Il obéit à des règles de vocabulaire et de syntaxe précises.
* **Langage de programmation interprété** : Un langage interprété est le second type de langage le plus courant avec les langages compilés, il nécessite un interpréteur pour être compris, mais aucune compilation préalable n'est requise.
* **Langage de programmation multiplateforme** : Multiplateforme signifie que le langage est compréhensible sur plusieurs systèmes d'exploitation différents (Windows, Linux, macOS, Android…)
* **Typage dynamique fort** : Le typage se sépare en quatre catégories typage dynamique ou statique et fort ou faible. En informatique, la catégorie du typage indique la permissivité du langage à accepter des changements de statut. Pour continuer sur l'analogie de la langue avec le français. Il y a un typage dynamique fort également. Un nom propre peut devenir un verbe, mais seulement sous certaines conditions. Ce sera par exemple un verbe du premier groupe. En revanche, un déterminant ne peut être transformé en verbe.
* **Syntaxe** : Comme pour tout langage, la syntaxe sert à structurer la communication pour que celle-ci soit compréhensible.

## Les différents types de langages

Il existe une multitude de langages interprétés et compilés (plus d'une cinquantaine) et un nombre fluctuant d'outils no-code. Il est évident qu'il n'existe pas de meilleur choix universel donc je vais définir ces trois types de langage.

### Les cliquodromes (Programmation No-code)

Les outils No-code ne nécessitent souvent aucune connaissance informatique ou de programmation. Ils sont disponibles à partir d'une interface web ou d'un logiciel à part entière exprès pour cela. La plupart sont aussi appelés cliquodromes, car la quasi-totalité des actions peut être effectuée à la souris. Il existe des outils qui utilisent une programmation graphique qui consiste à empiler des blocs afin de créer un script que le programme comprendra.
Ces outils ont chacun leur propre paradigme et langage et sont créés à partir de langages plus classiques.
L'inconvénient principal de ce genre de solution est le manque de flexibilité, si la personne qui fournit l'outil n'a pas implémenté une fonction dont vous avez besoin, vous ne pourrez pas l'utiliser. Par exemple, lors de l'affichage de graphique dans Excel, si vous voulez combiner des graphiques plus complexes, vous risquez de vous confronter à un mur.

### Les langages interprétés (Programmation haut niveau)

Les langages interprétés nécessitent un interpréteur. Il s'agit de concevoir des scripts ou textes compréhensibles par l'interpréteur. Les sites web, par exemple, sont de simples fichiers textes. Mais si l'on ajoute des codes au milieu du texte, on peut changer la couleur, le fond, la taille, la position…

Le langage le plus populaire de ces dernières années est Python, un langage interprété.

* L'avantage d'un langage interprété est que si une personne installe l'interpréteur, le simple script suffit pour que n'importe qui puisse l'utiliser. C'est ce qui se passe pour les sites web. Votre navigateur (Firefox, Opera, Chrome…) se charge de traduire le site pour vous, mais le site n'est qu'un fichier texte.
* L'inconvénient principal est que l'interpréteur peut consommer plus de ressources et si le programme demande beaucoup de calculs, cette solution sera souvent plus lente qu'avec les langages compilés.

### Les langages compilés (Programmation bas niveau)

Les langages compilés nécessitent un compilateur lors de la création d'un programme. Le programme ainsi créé fonctionnera sur l'ordinateur où il a été compilé et ceux qui fonctionnent comme lui. Les personnes souhaitant l'utiliser n'ont rien à installer (si ce n'est le programme en lui-même), mais juste à lancer le programme.

Ce type de langage est souvent plus bas niveau et nécessite des connaissances plus approfondies de programmation.

* L'avantage principal est un contrôle complet de ce que vous voulez faire, si vous avez les connaissances nécessaires. Les personnes souhaitant utiliser votre programme n'ont rien à installer. La plupart du temps, effectuer les mêmes tâches avec un langage interprété et compilé prendra moins de temps sur ce dernier.
* L'inconvénient principal est que le programme doit être compilé pour un type de machine. Un programme pour un PC Windows ne fonctionnera pas directement sur votre téléphone ou un Mac. Faire en sorte qu'un programme soit compatible avec différents systèmes peut devenir problématique.

## Quel langage choisir ?

Les informaticiens aiment aussi les classements de popularité, concernant les langages de programmation, parmi les plus connus, il y a l'[index TIOBE](https://www.tiobe.com/tiobe-index/) ou l'[IEE spectrum](https://spectrum.ieee.org/the-top-programming-languages-2023). Depuis sa création, Python grignote inlassablement des parts à tout ses "concurrents" pour se hisser à la première place depuis quelques années et continuer à assurer sa position dominante en creusant l'écart.

Évidemment, chaque langage à un but, une utilisation plus ou moins adaptée à la situation. Par exemple, JavaScript souvent en haut des classements est le principal langage lors de développement web qui est le domaine qui possède une demande de plus en plus importante. Mais il ne servira pas à grand-chose dans le cadre de la recherche à part dans quelques cas particuliers comme la création/gestion de formulaires.

Dans ces classements, il faut également prendre en compte les langages compilés, ils nécessitent plus de développement et des connaissances approfondies, ce qui, pour l'analyse de données, peut être largement superflu. Les différentes solutions de No-code ne sont listées dans aucun classement par manque d'utilisateurs et de flexibilité. Souvent, ils sont couplés avec un langage pour combler leurs plus grosses lacunes.

## Pourquoi Python est-il numéro 1 pour les sciences ouvertes ?

Python a conquis le monde des sciences ouvertes pour plusieurs raisons :

1. **Polyvalence** : Python peut être utilisé dans une variété de domaines, de l'analyse de données à la modélisation mathématique en passant par l'apprentissage automatique. Il offre une flexibilité exceptionnelle pour aborder des problèmes complexes.
2. **Grande Popularité** : Python est en tête des classements de popularité des langages de programmation depuis des années, ce qui signifie qu'il y a une abondance de ressources, de forums et de support disponible.
3. **Communauté Active** : Python bénéficie d'une communauté de développeurs et de chercheurs très active. Cela signifie qu'il existe de nombreuses bibliothèques et modules prêts à l'emploi pour une grande variété de tâches scientifiques.
4. **Facilité d'Apprentissage** : Sa syntaxe simple et lisible en fait un excellent choix pour les débutants en programmation. Les scientifiques peuvent se concentrer sur la résolution de problèmes plutôt que sur la maîtrise de la syntaxe.
5. **Prototypage rapide** : La création de tests rapide avant l'élaboration d'un script plus complet est très facile.

En fin de compte, Python est le langage de choix pour de nombreuses disciplines scientifiques en raison de sa polyvalence, de sa communauté dynamique et de sa facilité d'utilisation.

## Exemple

[Fichier Python](../_includes/code/introduction/read_datas.py)

```python
{% include code/introduction/read_datas.py %}
```
