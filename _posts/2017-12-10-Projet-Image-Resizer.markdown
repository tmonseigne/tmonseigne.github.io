---
layout: post
title: Projet Image Resizer
date: 2017-12-10
description: 
img: theme/TI-Theme.jpg # Add image post (optional)
tags: [Projet Scolaire, Réalité augmentée]
author: Thibaut Monseigne # Add name author (optional)
---

* TOC
{:toc}
{: .toc-post}

[Github du projet](https://github.com/adelpeyroux/resize-image){:target="_blank"} 

Le but de ce court projet était d'utiliser un algorithme de traitement d'image avancé. Nous avons choisi avec [Arnaud Delpeyroux](https://adelpeyroux.github.io/){:target="_blank"} et [Sébastien Pouteau](http://sebastien.pouteau.emi.u-bordeaux.fr/#){:target="_blank"} d'utiliser la méthode présente dans l'article `Seam Carving for Content-Aware Image Resizing` de Shai Avidan et Ariel Shamir. 

Le principe est simple, on décide d'affecter un poids, une énergie à chaque pixel. Ensuite, on parcourt l'image verticalement (ou horizontalement) pour trouver le chemin qui possède le poids minimum. Il suffit ensuite de supprimer ce chemin (ou de le dupliquer si l'on veut agrandir l'image).

Sur le [Github du projet](https://github.com/adelpeyroux/resize-image){:target="_blank"}, nous proposons une implémentation de cette méthode en Matlab (compatible avec Octave) avec une interface graphique. Nous proposons plusieurs fonctions d'énergie différentes pour définir le poids des pixels.

Voici une vidéo de présentation de notre projet : 

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/249186917" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>
