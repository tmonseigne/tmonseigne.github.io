---
layout: post
title: Les risques dans la classifications
date: 2023-05-17
description: Les risques dans la classifications
img: theme/Classif-Theme.png # Add image post (optional)
tags: [Explication]
author: Thibaut Monseigne # Add name author (optional)
---

* TOC
{:toc}
{: .toc-post}

![WIP](/assets/img/WIP.png){:style="max-width:50%;"}

## Déséquilibre des classes

Un déséquilibre entre deux classes dans un jeu de données peut présenter plusieurs risques :

* Biais de classification : Lorsque les classes sont déséquilibrées, le modèle peut être enclin à attribuer une plus grande importance à la classe majoritaire, car il cherche à minimiser l'erreur globale. Cela peut entraîner un biais de classification, où le modèle a du mal à bien identifier les échantillons de la classe minoritaire.
* Performances déséquilibrées : Lorsque les classes sont déséquilibrées, les performances du modèle peuvent être biaisées en faveur de la classe majoritaire. Par exemple, si la classe majoritaire représente 90% des échantillons et la classe minoritaire seulement 10%, un modèle naïf qui prédit toujours la classe majoritaire atteindrait déjà une précision de 90% sans apprendre les motifs de la classe minoritaire.
* Erreurs coûteuses : Dans certains cas, les erreurs de classification sur la classe minoritaire peuvent être plus coûteuses que les erreurs sur la classe majoritaire. Par exemple, dans un système de détection de fraudes, une fausse alarme sur une transaction légitime est généralement moins grave que de manquer une transaction frauduleuse. Si la classe minoritaire représente les transactions frauduleuses, un déséquilibre peut entraîner des conséquences coûteuses.
* Manque de généralisation : Un déséquilibre entre les classes peut rendre difficile la généralisation du modèle à de nouvelles données ou à des scénarios différents. Le modèle peut être sur-optimisé pour la classe majoritaire et avoir du mal à bien généraliser les motifs de la classe minoritaire.

Pour atténuer ces risques, il est souvent recommandé de prendre des mesures pour équilibrer les classes, telles que l'over-sampling de la classe minoritaire, l'under-sampling de la classe majoritaire ou l'utilisation de techniques d'ensemble qui combinent les deux approches. Ces méthodes visent à fournir un jeu de données plus équilibré, permettant au modèle d'apprendre de manière plus équitable et de mieux représenter les deux classes.

### Sur-Echantillonnage (Over-sampling)

L'over-sampling, qui consiste à augmenter artificiellement le nombre d'échantillons de la classe minoritaire, peut être bénéfique pour résoudre le déséquilibre de classes dans un problème de classification.

Cependant, il y a aussi des risques associés à l'over-sampling, notamment :

* Surapprentissage : L'over-sampling peut conduire à un surapprentissage si les échantillons synthétiques générés sont trop similaires aux échantillons d'origine. Cela peut entraîner une surconfiance du modèle dans ses prédictions, ce qui le rend moins généralisable aux nouvelles données.
* Amplification du bruit : En créant des échantillons synthétiques, il existe un risque d'amplification du bruit. Si les échantillons de la classe minoritaire sont bruités ou mal étiquetés, l'over-sampling peut étendre ces erreurs et affecter négativement les performances du modèle.
* Redondance d'informations : L'over-sampling peut introduire une redondance d'informations dans le jeu de données, car les échantillons synthétiques peuvent être similaires aux échantillons existants. Cela peut entraîner une augmentation de la complexité et de la taille du modèle sans améliorer réellement sa performance.
* Biais dans les estimations : L'over-sampling peut introduire un biais dans les estimations de performance du modèle. Comme les échantillons synthétiques sont générés à partir de la classe minoritaire, le modèle peut sembler performant lors de l'évaluation, mais pourrait ne pas généraliser correctement aux données réelles.

Il est important de prendre en compte ces risques potentiels lors de l'utilisation de l'over-sampling. Il est recommandé d'évaluer attentivement les performances du modèle sur des données non vues auparavant et d'utiliser des méthodes supplémentaires, telles que la validation croisée, pour obtenir une évaluation plus robuste du modèle.

### Sous-Echantillonnage (Under-sampling)

L'under-sampling consiste à réduire le nombre d'échantillons de la classe majoritaire afin de les équilibrer avec la classe minoritaire. Cela peut aider à prévenir le surapprentissage et à améliorer les performances du modèle.

Cependant, il y a aussi des risques associés à l'under-sampling, notamment :

* Perte d'informations : En réduisant le nombre d'échantillons de la classe majoritaire, vous risquez de perdre des informations potentiellement utiles. Cela peut entraîner une diminution de la capacité du modèle à généraliser et à représenter correctement la classe majoritaire.
* Perte de variabilité : L'under-sampling peut réduire la variabilité des données, ce qui peut rendre le modèle moins robuste aux variations naturelles présentes dans les données réelles.

Une autre approche à considérer est l'utilisation de techniques d'ensemble, comme le sous-échantillonnage avec rééchantillonnage bootstrap (Bootstrap Under-Sampling, BUS), qui combine l'under-sampling avec la génération d'échantillons synthétiques. Cela peut aider à prévenir la perte d'informations tout en équilibrant les classes.

### Techniques d'ensembles

Les technique d'ensemble combinent l'under-sampling et la génération d'échantillons synthétiques.  
Les risques de cette méthode combinent, logiquement, ceux des deux précédentes.  
Pour atténuer ces risques, il est important de surveiller attentivement les performances du modèle sur des données réelles et de valider les résultats avec des métriques d'évaluation appropriées.

**Exemple python** : [Fichier Python](../_includes/code/classification/Resampling.py)

```python
{% include code/classification/Resampling.py %}
```

![Resampling](../_includes/code/classification/Resampling.png){:style="max-width:50%;"}

## Normalisation des données
