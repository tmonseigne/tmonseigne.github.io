---
layout: post
title: Projet ReactCamera
date: 2017-12-11
description: 
img: theme/RVRA-Theme.jpg # Add image post (optional)
tags: [Projet Scolaire, Réalité augmentée]
author: Thibaut Monseigne # Add name author (optional)
---

* TOC
{:toc}
{: .toc-post}

[Github du projet](https://github.com/adelpeyroux/rvra-project){:target="_blank"} 

Le but de ce court projet était de réaliser une application en Réalité virtuelle ou réalité augmentée. Nous avons choisi avec [Arnaud Delpeyroux](https://adelpeyroux.github.io/){:target="_blank"} et [Sébastien Pouteau](http://sebastien.pouteau.emi.u-bordeaux.fr/#){:target="_blank"} de nous concentrer sur la réalité augmentée. 

# Introduction

Notre projet se base sur le principe de la [ReacTable ](http://reactable.com).

![Reactable](/assets/img/ReactCamera/Reactable.png){:style="max-width:50%"}

La ReacTable est une table tactile permettant, à l'aide de différents nœuds, de générer du son. Il existe une multitude de nœuds différents selon les sons que l'on souhaite obtenir:
- Nœud de synthèse sonore (génère des sinusoïdes)
- Nœud de traitement du signal (filtre, synthèse AM, synthèse FM)
- etc.

Notre projet est de reproduire son fonctionnement à l'aide d'une simple caméra et de marqueur [ArUco](https://docs.opencv.org/3.1.0/d5/dae/tutorial_ArUco_detection.html){:target="_blank"} . Vous trouverez également une liste des marqueurs utilisés [ici](https://github.com/adelpeyroux/rvra-project/tree/master/markers){:target="_blank"} .

Les objectifs attendus:
- détecter des marqueurs ArUco et les identifier
- Générer un résultat sonore en fonction des marqueurs utilisés
- Visualiser les liaisons entre les marqueurs pour simplifier la manipulation

# Réalisation

Dans ce projet, nous allons utiliser un nombre limité de types de marqueur:
- Les sources : Sinusoïde (`Si`), Square (`Sq`), Saw (`Sa`), Triangle (`T`), Lecture de fichiers sonores (`F0`, `F1`, `F2`, `F3`), Noise (`R`) et Numérique (`N`)
- Les filtres : AM (`A`), FM (`F`), Add (`+`)

## Traitement des marqueurs

Tout d'abord, voici les marqueurs que nous utilisons:

|<a href="/assets/img/ReactCamera/Marker1.jpg" data-lightbox="ReactCamera" data-title="Marqueurs 1"><img src="/assets/img/ReactCamera/Marker1.jpg" alt="Marqueurs 1" style="max-width:100%;"/></a>|<a href="/assets/img/ReactCamera/Marker2.jpg" data-lightbox="ReactCamera" data-title="Marqueurs 2"><img src="/assets/img/ReactCamera/Marker2.jpg" alt="Marqueurs 2" style="max-width:100%;"/></a>|<a href="/assets/img/ReactCamera/Marker3.jpg" data-lightbox="ReactCamera" data-title="Marqueurs 3"><img src="/assets/img/ReactCamera/Marker3.jpg" alt="Marqueurs 3" style="max-width:100%;"/></a>|


Nous les avons collés directement sur des cubes pour éviter de les masquer lors de la manipulation.

Nous utilisons ArUco et OpenCV pour permettre de repérer ces marqueurs. ArUco nous renvoie une structure de données contenant l'orientation du marqueur, sa position et son identifiant.

À partir de ces informations, nous avons choisi de créer un graphe dont la racine commence au centre de l'affichage.
Un noeud source ne peut pas avoir de parent. Un noeud interne peut avoir n parents et n fils.
Pour générer les liaisons de notre graphe, nous avons opté pour des liaisons par proximité.

{% highlight C++ %}
// sources : tableau contenant toutes les sources
// effects : tableau contenant tous les noeuds d'effet.
for (int id : sources) {
	Node current(_markers[id], id, time);
	Node tmp;
	bool find;
	do {
		find = FindProximity(current, effects, tmp); // retourne si un noeud est entre le noeud actuel et le centre, s'il y a un noeud alors il est stocké dans tmp
		if (find) {
			AddEdge(current.GetMarkerIndex(), tmp.GetMarkerIndex());
			tmp.AddInput(current);
			current = tmp;
			find = false;
		}
	} while (find);
	AddEdge(current.GetMarkerIndex(), _root.GetMarkerIndex());

	_root.AddInput(current);
}
{% endhighlight %}

Voici une capture d’écran d'un graphe généré.

<a href="/assets/img/ReactCamera/Graph.png" data-lightbox="ReactCamera" data-title="Graphe Généré"><img src="/assets/img/ReactCamera/Graph.png" alt="Graphe Généré" style="max-width:50%;"/></a>

Un des problèmes les plus importants dans cette partie fut de gérer les disparitions des marqueurs dus à la qualité de la caméra. En effet, de temps en temps avec les changements de luminosité, ArUco n'arrive plus à détecter un marqueur, ce phénomène ne dure qu'un bref instant. Pour contrer ce problème, nous avons mis en place une rémanence de chaque marqueur dans le temps. Cela signifie que si un marqueur disparaît de l'écran il faut attendre un bref instant avant qu'il soit supprimé du graphe. Ce principe évite donc la suppression et réapparition soudaine des marqueurs.



## Génération des sons

Nous devons générer une sortie sonore à partir des différents éléments du graphe. Tout d'abord nous allons commencer par détailler les actions de chaque noeud.

Qu'est-ce qu'une source ?  
Une source est un noeud qui va générer un signal sonore caractérisé par son type (un tableau qui sera transmis directement à la carte son).

$$s=amplitude\times \sin{(2\pi \times f \times t + \phi)}$$

Avec les paramètres qui varient selon l'orientation des marqueurs.

Pour les différents effets, nous avons réutilisé les formules basiques du traitement du son, en les adaptant à notre problème. 

Nous sommes tombés sur deux problèmes majeurs dans cette partie :
- le temps de génération (44100 échantillons par seconde).
- le suivi de phase.

### temps de synthèse sonore

Pour obtenir un son fluide, il nous faut générer 44100 échantillons par seconde.
Dans notre première implémentation, les parties (reconnaissance, génération du graphe, la synthèse du son) s'exécutaient dans le même thread, cette version ne permettait pas d'obtenir le nombre d'échantillons voulus. Pour résoudre ce problème, nous avons choisi d'exécuter la partie synthèse sonore dans un thread indépendant.

### le suivi de phase

Lorsque le suivi de phase n'est pas respecté, nous pouvons constater des clics dans le signal. Ce phénomène n'est pas agréable à l'utilisateur. Nous avons dû mettre en place un suivi de phase. Pour chaque source sonore, nous sauvegardons la phase pour permettre de générer le bon échantillon et ainsi éviter les clics dans le signal.


## Interface de visualisation

L'interface du projet a été vue comme une classe à part ayant ses propres paramètres, membres et méthodes. Au vu des technologies employées, il a été décidé d'utiliser OpenCV. Cette bibliothèque ayant déjà été utilisée pour l'acquisition vidéo. 

La classe peut être divisée en deux parties, l'affichage fixe et l'affichage dynamique. 

- La partie fixe correspond au nœud central vers lequel vont converger toutes les sources ainsi que la possibilité de segmenter notre écran, cette option n’est pas utilisée dans notre exemple, mais elle pourrait permettre à l’utilisateur de séparer virtuellement son espace de travail.
- La partie dynamique correspond à l’affichage des liaisons entre les marqueurs ainsi qu’à un affichage supplémentaire sur les marqueurs.

Sur l’ensemble de l’affichage, on peut également définir un niveau de transparence de l’interface. Cela nous permet, par exemple, de conserver un visuel de la réalité derrière la surimpression.

Les marqueurs quant à eux sont, pour le moment, représenté par un code couleur et un caractère en fonction de leur type.
- <span style="color:Crimson;"><b>ROUGE</b></span> : Sinusoïde, lecture d'un fichier sonore, saw, square, triangle.
- <span style="color:Green;"><b>VERT</b></span> : Noise.
- <span style="color:DarkBlue;"><b>BLEU</b></span> : Numérique.
- <span style="color:Gold;"><b>JAUNE</b></span> : AM.
- <span style="color:Magenta;"><b>MAGENTA</b></span> : FM.
- <span style="color:Turquoise;"><b>CYAN</b></span> : ADD.

 De plus, ils possèdent un cercle les entourant indiquant l’orientation du marqueur. Cette orientation permet de régler le paramètre associé au type de marqueur (par exemple la fréquence d’un oscillateur).

|<a href="/assets/img/ReactCamera/vide.png" data-lightbox="ReactCamera" data-title="Vide"><img src="/assets/img/ReactCamera/vide.png" alt="Vide" style="max-width:100%;"/></a>|<a href="/assets/img/ReactCamera/simple.png" data-lightbox="ReactCamera" data-title="Simple"><img src="/assets/img/ReactCamera/simple.png" alt="Simple" style="max-width:100%;"/></a>|<a href="/assets/img/ReactCamera/Graph.png" data-lightbox="ReactCamera" data-title="Complexe"><img src="/assets/img/ReactCamera/Graph.png" alt="Complexe" style="max-width:100%;"/></a>|


# Conclusion

Ce projet est fonctionnel en état et permet de produire des sons plus ou moins complexes.
Dans ce projet nous avons pu mettre en application à la fois les connaissances en RVRA, mais également des connaissances issues d'UE telles que le traitement du son. Il nous a permis de nous confronter aux applications temps réel avec les contraintes que cela implique.
 
<!--Voici une vidéo montrant notre projet en action

<video src="https://github.com/adelpeyroux/rvra-project/blob/master/demo/demo.mp4" controls>Votre navigateur ne gère pas l'élément <code>video</code>.</video>
-->


## Améliorations possibles

Nous avons pensé à diverses améliorations:
- modifier les liaisons entre les différents nœuds pour observer les sinusoïdes produites
- Obtenir un rendu directement sur la scène en utilisant un vidéo projecteur au lieu d'utiliser un écran externe
- Exporter l'affichage sur des lunettes de réalité augmentée et ainsi rajouter les liaisons directement
