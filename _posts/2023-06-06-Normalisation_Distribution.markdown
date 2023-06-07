---
layout: post
title: Normalisation de la distribution d'un signal
date: 2023-06-06
description: Normalisation de la distribution d'un signal
img: theme/Geo3D-Theme.png
tags: [Explication]
author: Thibaut Monseigne
---

* TOC
{:toc}
{: .toc-post}

## Description

La normalité dans le contexte de la distribution d'un signal fait référence à une distribution qui suit une loi normale, également appelée distribution gaussienne. Une distribution normale est caractérisée par une forme symétrique en forme de cloche, où la majorité des observations se trouvent près de la moyenne et la dispersion décroît à mesure que l'on s'éloigne de la moyenne.

La normalité peut être utile dans différentes applications pour plusieurs raisons :

* Tests statistiques : De nombreux tests statistiques et méthodes d'inférence sont basés sur l'hypothèse que les données suivent une distribution normale. Par conséquent, si les données ne sont pas normalement distribuées, l'application de ces tests peut être invalide ou donner des résultats erronés.
* Modélisation et prévision : La normalité peut simplifier la modélisation des données et faciliter la prévision future. Les modèles statistiques, tels que la régression linéaire ou l'analyse de séries temporelles, supposent souvent que les résidus ou les erreurs suivent une distribution normale.
* Méthodes paramétriques : Les méthodes paramétriques, telles que l'estimation des paramètres ou les intervalles de confiance, peuvent être plus fiables et précises lorsque les données suivent une distribution normale. Dans ces méthodes, des hypothèses sur la distribution des données sont nécessaires, et la normalité facilite souvent les calculs et l'interprétation des résultats.
* Tests d'hypothèses : Certains tests d'hypothèses, tels que le test t de Student, supposent également une distribution normale des données pour être valides. En s'assurant que les données sont normalement distribuées, on peut garantir la validité de ces tests et prendre des décisions basées sur des résultats statistiquement fiables.

Cependant, il est important de noter que dans de nombreuses situations réelles, les données peuvent ne pas être strictement normales. Dans certains cas, des transformations appropriées peuvent être appliquées pour rendre les données plus proches d'une distribution normale, permettant ainsi l'application des méthodes statistiques basées sur cette hypothèse. Des techniques telles que les transformations logarithmiques, les transformations de Box-Cox ou les méthodes de normalisation peuvent être utilisées à cet effet.

## Méthodes

### Transformation logarithmique

**Définition** : La transformation logarithmique consiste à prendre le logarithme des valeurs d'un signal.

$$X' = log(X)$$
{: .Formule}

**Avantages** : Cette transformation peut être utile lorsque les données ont une distribution fortement asymétrique positive. Elle peut réduire la variation et rendre la distribution plus symétrique, se rapprochant potentiellement d'une distribution normale.

**Inconvénients** : La transformation logarithmique n'est pas applicable lorsque les données contiennent des valeurs négatives ou nulles, car le logarithme de ces valeurs n'est pas défini.

### Transformation exponentielle

**Définition** : La transformation exponentielle consiste à prendre l'exponentielle des valeurs d'un signal.

$$X'= e^{X}$$
{: .Formule}

**Avantages** : Cette transformation peut être utilisée pour inverser une transformation logarithmique et ramener les données à leur échelle d'origine. Elle peut également être utile lorsque les données ont une distribution fortement asymétrique négative.

**Inconvénients** : Comme pour la transformation logarithmique, la transformation exponentielle n'est pas applicable lorsque les données contiennent des valeurs négatives.

### Transformation de Box-Cox

**Définition** : La transformation de Box-Cox est une méthode qui vise à trouver la transformation optimale d'un signal en utilisant une famille de transformations paramétriques.

$$
X'= \left\{
    \begin{array}{ll}
        log(X) & \text{si} &  \lambda = 0  \\
        \frac{X^\lambda - 1}{\lambda} & \text{si } & \lambda \neq 0
    \end{array}
\right.
$$
{: .Formule}

**Avantages** : La transformation de Box-Cox peut être utilisée pour normaliser les données en trouvant la meilleure transformation paramétrique pour rendre la distribution aussi proche que possible d'une distribution normale. Elle peut gérer une variété de distributions asymétriques.

**Inconvénients** : La transformation de Box-Cox nécessite l'estimation du paramètre optimal de transformation, ce qui peut être plus complexe. De plus, elle peut ne pas fonctionner efficacement si les données contiennent des valeurs nulles ou négatives.

### Standardisation

**Définition** : La standardisation (ou z-score) consiste à soustraire la moyenne des données et à diviser par l'écart-type.

$$X'= \frac{X-\mu}{sigma}$$
{: .Formule}

**Avantages** : La standardisation permet de transformer les données pour qu'elles aient une moyenne de zéro et un écart-type de 1. Cela peut faciliter la comparaison des données et la mise en évidence des valeurs atypiques.

**Inconvénients** : La standardisation ne modifie pas la distribution des données pour les rendre normales, elle se concentre plutôt sur la mise à l'échelle des données. Elle peut également être sensible aux valeurs extrêmes.

### Transformation des rangs

**Définition** : La transformation des rangs assigne à chaque valeur son rang dans l'ensemble des données. Les valeurs sont triées puis numérotées de 1 à N.

$$X'= Rang(X)$$
{: .Formule}

Suivant la méthode, les valeurs identiques peuvent avoir le rang moyen, minimum ou maximum de ces valeurs.

**Avantages** : La transformation des rangs permet de transformer les données en une distribution uniforme où chaque valeur a un rang spécifique. Elle peut être utile lorsque les données ont une distribution très asymétrique.

**Inconvénients** : La transformation des rangs ne modifie pas la forme de la distribution, elle redistribue simplement les valeurs. Elle peut également être affectée par des valeurs identiques qui reçoivent le même rang.

### Transformation de puissance

**Définition** : La transformation de puissance consiste à appliquer une puissance aux valeurs d'un signal, comme la racine carrée ou la puissance cubique.

$$X'= X^n$$
{: .Formule}

Où $$n$$ peut être n'importe quel nombre (puissance cubique si $$n=3$$, racine carrée si $$n=\frac{1}{2}$$...).

**Avantages** : La transformation de puissance peut aider à réduire l'asymétrie et à rendre la distribution plus symétrique, en se rapprochant potentiellement d'une distribution normale.

**Inconvénients** : La transformation de puissance peut modifier considérablement la distribution des données, ce qui peut rendre l'interprétation plus difficile. De plus, le choix de la puissance doit être fait avec soin pour éviter des effets indésirables.

## Exemple

Avec de multiples distributions possibles, on calcule la nouvelle distribution selon les différentes méthodes.

**Exemple python** : [Fichier Python](../_includes/code/features/Distribution_modification.py)

```python
{% include code/features/Distribution_modification.py %}
```

<figure id="Fig1">
 <a href = "/assets/img/classification/Exponential_Distribution.png" data-lightbox = "Memo" data-title = "Transformation d'une distribution exponentielle"><img src = "/assets/img/classification/Exponential_Distribution.png" alt = "Transformation d'une distribution exponentielle" style = "max-width:50%;"/></a>
 <figcaption></figcaption>
</figure>

<figure id="Fig2">
 <a href = "/assets/img/classification/Power_Distribution.png" data-lightbox = "Memo" data-title = "Transformation d'une distribution de puissance 5"><img src = "/assets/img/classification/Power_Distribution.png" alt = "Transformation d'une distribution de puissance 5" style = "max-width:50%;"/></a>
 <figcaption></figcaption>
</figure>
