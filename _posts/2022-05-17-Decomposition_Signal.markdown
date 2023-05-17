---
layout: post
title: Décomposition du Signal
date: 2022-05-17
description: Décomposition du Signal (Transformée de fourier, ondelette, cepstre de fréquence mel)
img: theme/Geo3D-Theme.png # Add image post (optional)
tags: [Explication]
author: Thibaut Monseigne # Add name author (optional)
---

* TOC
{:toc}
{: .toc-post}

![WIP](/assets/img/WIP.png){:style="max-width:50%;"}

## Transformée de fourier rapide (FFT)

**Définition** : La transformée de Fourier est une technique mathématique utilisée pour analyser les signaux en domaines de fréquences. Elle permet de représenter un signal dans le domaine des fréquences en décomposant le signal en une somme de sinusoïdes de différentes fréquences. La transformée de Fourier rapide est un algorithme de calcul de la transformation de Fourier discrète pouvant être exprimé de cette façon :

$$
X(k) = \sum_{n=0}^{N-1} x(n) \cdot e^{-\frac{i \cdot 2 \pi \cdot k \cdot n}{N}}
$${: .Formule}

Dans cette formule, $$x(n)$$ est le signal d'entrée, $$X(k)$$ est le spectre de fréquences obtenu après la transformation, $$N$$ est la taille du signal d'entrée et $$exp()$$ est la fonction exponentielle complexe. La formule calcule les coefficients de fréquence $$X(k)$$ pour différentes valeurs de $$k$$ qui représentent les composantes fréquentielles du signal. La partie réelle, magnitude de $$X(k)$$ (c'est-à-dire $$\lvert X(k)\rvert$$), correspond à l'amplitude du signal sur chaque fréqeunce et la partie imaginaire, l'argument (ou angle) de $$X(k)$$ (c'est-à-dire $$\arg(X(k))$$), correspond à sa phase.

**Utilisations** : La FFT est une base essentielle très souvent utilisé pour l'analyse et le traitement de signaux (quel que soit le nombre de dimensions : 1D pour le son, 2D pour l'image) pour principalement détecter les composantes fréquentielles d'un signal. Elle permet également d'identifier les harmoniques, extraire des caractéristiques et effectuer des opérations de filtrage (supprimer certaines fréquences)... Pour le traitement d'images, La FFT est appliquée pour effectuer des opérations de filtrage fréquentiel, comme le lissage, la détection des contours et l'amélioration de la netteté. La compression des données peut aussi utiliser la FFT comme pour les formats `MP3` ou `JPEG`.

**Exemple python** : [Fichier Python](../_includes/code/signal_processing/FFT.py)

```python
{% include code/signal_processing/FFT.py %}
```

## Décomposition en ondelettes

**Définition** : Les ondelettes sont une autre méthode de décomposition de signal largement utilisée. Contrairement à la transformée de Fourier, qui utilise des sinusoïdes comme fonctions de base, les ondelettes utilisent des fonctions de base plus complexes appelées "ondelettes". Les ondelettes sont des signaux de durée finie et localisés dans le temps et la fréquence.

Pour effectuer la décomposition en ondelettes, il est nécessaire de choisir une fonction mère (aussi appelée ondelette mère) qui sera utilisée pour composer le signal. Les ondelettes mères sont définies par des familles d'ondelettes, et il existe différentes familles d'ondelettes disponibles dans des bibliothèques comme `pywavelets` en Python.

La bibliothèque pywavelets offre une gamme d'ondelettes populaires telles que les ondelettes de Haar, Daubechies, Symlets, entre autres. Chaque famille d'ondelettes a ses propres caractéristiques et propriétés, ce qui les rend adaptées à différentes applications et types de signaux (voir [https://wavelets.pybytes.com/](https://wavelets.pybytes.com/)).

Il est important de choisir la bonne ondelette mère en fonction des spécificités de votre signal et des objectifs de votre analyse. Chaque ondelette mère aura des propriétés de régularité, de parcimonie, de résolution temporelle et de résolution fréquentielle différentes.

**Remarque :** On pourrait grossièrement simplifier une transformée de Fourier comme étant une décomposition en ondelette avec pour ondelette mère un sinus, mais moins flexible et ne prenant pas en compte le domaine temporel.
{: .Note}

**Utilisations** : La décomposition en ondelettes est particulièrement adaptée à l'analyse de signaux non stationnaires ou transitoires. Elle est utilisée dans de nombreux domaines tels que le traitement du signal, la compression de données, l'analyse d'images et la détection de motifs.

**Exemple python** : [Fichier Python](../_includes/code/signal_processing/Wavelet.py)

```python
{% include code/signal_processing/Wavelet.py %}
```

## Les coefficients cepstraux de fréquence Mel (MFCC)

**Définition** : Les coefficients MFC (Mel Frequency Cepstral Coefficients) sont utilisés dans le domaine de la reconnaissance automatique de la parole et du traitement du signal audio. Ils sont basés sur la perception humaine des différentes fréquences dans le spectre sonore.

La méthode MFCC consiste en plusieurs étapes :

* Prétraitement : Le signal audio est divisé en petites fenêtres de temps, et pour chaque fenêtre, on applique une fonction de fenêtrage, généralement une fenêtre de type Hamming, pour atténuer les effets de bord.
* Calcul de la transformée de Fourier : Pour chaque fenêtre, on calcule la transformée de Fourier pour obtenir le spectre de fréquences.
* Filtrage de Mel : On applique un ensemble de filtres de Mel qui sont des filtres triangulaires espacés de manière non linéaire dans l'échelle de fréquence Mel, qui simule la perception humaine de la fréquence.
* Calcul des logarithmes des filtres Mel : Les valeurs des filtres de Mel sont converties en échelle logarithmique (en lien avec la perception auditive humaine).
* Transformation en cosinus discrète : On applique une transformation en cosinus discrète (DCT) aux valeurs des filtres Mel logarithmiques pour obtenir les coefficients MFCC finaux.

**Utilisations** : Les coefficients MFC sont souvent utilisés dans la reconnaissance automatique de la parole, l'identification des locuteurs et d'autres tâches liées au traitement du signal audio.

**Exemple python** : [Fichier Python](../_includes/code/signal_processing/MFCC.py)

```python
{% include code/signal_processing/MFCC.py %}
```
