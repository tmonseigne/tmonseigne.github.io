---
layout: post
title: Mémo Classification
date: 2018-10-05
description: Mémo Classification
img: theme/Classif-Theme.png # Add image post (optional)
tags: [Mémos, Machine Learning]
author: Thibaut Monseigne # Add name author (optional)
---

* TOC
{:toc}
{: .toc-post}

<!---
**sources principales :** [fr.wikipedia.org/wiki/Apprentissage_automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique)-->

## Définitions et notions de base

L'**apprentissage automatique** (ou *machine learning*) consiste à apprendre à une machine à résoudre des tâches difficiles par des algorithmes classiques. L'apprentissage automatique est utilisé pour la classification : étiqueter chaque donnée en l'associant à une classe.

Un **classifieur** est un ensemble d’opérations qui permettent de définir à quelle classe appartient un élément.

**Apprentissage supervisé** : L'apprentissage s'effectue grâce à des exemples déjà classés. On suppose cette base d'apprentissage représentative d'une population d'échantillons plus large et le but des méthodes d'apprentissage supervisé est de bien généraliser, c'est-à-dire d'apprendre une fonction qui fasse des prédictions correctes sur des données non présentes dans l'ensemble d'apprentissages. Il s’agit d’apprendre à classer un nouvel élément parmi un ensemble de classes prédéfinies: on connaît les classes à priori.

**Apprentissage semi-supervisé** : L'apprentissage s'effectue grâce à des exemples déjà classés et d'autres non. Le nombre de classes ou leur définition peuvent être prédéfinis.

**Apprentissage non-supervisé** : L'apprentissage s'effectue grâce à des exemples non classés. Il s'agit, pour un logiciel, de trouver des structures sous-jacentes à partir de données non étiquetées. Le nombre et la définition des classes ne sont pas donnés à priori.

**classification linéaire** : La classification linéaire vise à trouver une séparation linéaire entre les différentes classes d'observations. Autrement dit, elle consiste à tracer une ligne (dans un espace à deux dimensions), un plan (dans un espace à trois dimensions), ou un hyperplan (dans des espaces de dimension supérieure) qui permet de séparer les observations de chaque classe.

**classification quadratique** : La classification quadratique est une méthode de classification qui suppose que les données appartiennent à des distributions gaussiennes et que les frontières de décision entre les différentes classes sont des paraboles, d'où le terme "quadratique". Cette méthode est une extension de la classification linéaire qui permet de modéliser des données non linéairement séparables en utilisant des fonctions polynomiales d'ordre supérieur pour décrire les frontières de décision.

### Espérance, Variance, Écart type, Loi Normale

On va considérer le poids de chaque donnée uniforme pour les différentes formules (si une valeur est plus présente, elle est juste répétée).

#### Espérance ($$\mu$$)

En théorie des probabilités, l’espérance mathématique d’une variable aléatoire réelle est, intuitivement, la valeur que l’on s’attend à trouver, en moyenne, si l’on répète un grand nombre de fois la même expérience aléatoire. Elle se note $$\operatorname{E}(X)$$ et se lit « espérance de X ».

Elle correspond à une moyenne pondérée des valeurs que peut prendre cette variable.

$$ \operatorname{E}(X) = \bar{x} = \frac{1}{n} \times \sum_{i=1}^n x_i $${: .Formule}

#### Variance ($$v$$), Ecart type ($$\sigma$$)

En probabilité, l’écart type est une mesure de la dispersion d’une variable aléatoire. En statistique, il est une mesure de dispersion de données. Il est défini comme la racine carrée de la variance, ou de manière équivalente comme la moyenne quadratique des écarts par rapport à la moyenne. Il a la même dimension que la variable aléatoire ou la variable statistique en question.

$$ \sigma_x = \sqrt{\frac{1}{n} \times \sum_{i=1}^n{\left(x_i-\bar{x}\right)^2}} = \sqrt{\frac{1}{n} \times \left(\sum_{i=1}^n{(x_i^2}\right) - \bar{x}^2} $${: .Formule}

#### Loi Normale ($$\mathcal{N}(\mu,\sigma^2)$$)

C’est une loi de probabilité absolument continue qui dépend de deux paramètres : son espérance, un nombre réel noté μ, et son écart type, un nombre réel positif noté σ. La densité de probabilité de la Loi Normale est donnée par :

$$ f(x)=\frac{1}{\sigma\sqrt{2\pi}}\times\mathrm{e}^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2} = \frac{1}{\sigma\sqrt{2\pi}}\times\mathrm{e}^{\frac{-\left(x-\mu\right)^2}{2\sigma^2}}$${: .Formule}

Note : $$\frac{1}{\sigma\sqrt{2\pi}}$$ assure que la fonction intègre à 1. (C’est une constante donc elle ne change pas l’aspect de la courbe.)
La courbe de cette densité est appelée courbe de Gauss ou courbe en cloche, entre autres. C’est la représentation la plus connue de cette loi. La Loi Normale de moyenne nulle et d’écart type unitaire est appelée loi normale centrée réduite ou loi normale standard.

##### Limites

On peut noter que la loi Normale à une valeur très proche de $$0$$ si $$x=\mu \pm 4\sigma$$, on a donc une bonne représentation sur l’intervalle $$\left[\mu - 4\sigma ; \mu + 4\sigma\right]$$. (Proche de $$0$$ car $$ \lim_{x\rightarrow -\infty} \mathrm{e}^x = 0$$

$$ f(\mu \pm 4\sigma) = \frac{1}{\sigma\sqrt{2\pi}}\times\mathrm{e}^{\frac{-\left(\mu \pm 4\sigma-\mu\right)^2}{2\sigma^2}} = \frac{\mathrm{e}^{\frac{-16\sigma^2}{2\sigma^2}}}{\sigma\sqrt{2\pi}} = \frac{\mathrm{e}^{-8}}{\sigma\sqrt{2\pi}}\approx \frac{0.0003}{\sigma\sqrt{2\pi}} $${: .Formule}

##### Fonction Gaussienne

Une fonction gaussienne est une fonction en exponentielle de l’opposé du carré de l’abscisse (une fonction en $$\mathrm{e}^(-x^2)$$). Elle a une forme caractéristique de courbes en cloche. La loi normale est une fonction Gaussienne (univariée, car de dimension 1).

##### Loi Normale Multidimensionnelle, Multinormale, densité Gaussienne multivariée... ($$\mathcal{N}(\mu,\sigma^2)$$)

C’est une généralisation multidimensionnelle de la Loi Normale.
On a :

* $$ d $$ : Nombre de dimensions
* $$ x $$ : Valeurs dans un vecteur de dimension $$d$$
* $$ \mu $$ : Espérance dans un vecteur de dimension $$d$$,  

$$\operatorname{E}(X) =\begin{pmatrix} \mu_0\\ \vdots\\ \mu_d \end{pmatrix} = \frac{1}{n} \times \sum_{i=1}^n{\left(x_i \times p(x_i)\right)} $${: .Formule}

* $$ \operatorname{C} $$ : La matrice de covariance  

$$\operatorname{C} = \operatorname{E}\left[\left(X-\operatorname{E}\left[X\right]\right)\left(X - \operatorname{E}\left[X\right]\right)^\mathsf{T}\right]
= \begin{pmatrix}
\sigma_{x_1}^2 & \sigma_{x_1 x_2} & \cdots & \sigma_{x_1 x_p}\\
\sigma_{x_2 x_1} & \ddots & \cdots & \vdots \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{x_p x_1} & \cdots & \cdots & \sigma_{x_p}^2
\end{pmatrix} $${: .Formule}

* $$ \lvert\operatorname{C}\rvert $$ : Le déterminant de la matrice de covariance
* $$ \operatorname{C}^{-1} $$ : L'inverse de la matrice

$$ p(x)= f_{(\mu,\operatorname{C})}(x) = \mathcal{N}(\mu,\sigma^2)(x) = \frac{1}{({2\pi})^{d/2} \times {\lvert\operatorname{C}\rvert}^{1/2}} \times \mathrm{e}^{-\frac{1}{2} \times \left(x-\operatorname{E}\right)^\mathsf{T}\operatorname{C}^{-1}\left(x-\operatorname{E}\right)} $${: .Formule}

**Note** : Comme pour la Loi Normale univariée, la première partie assure que la densité intègre à 1.

## Descente de gradient ($$\nabla$$)

La descente de gradient nous permet de minimiser une fonction $$\mathcal{f}$$ (c’est-à-dire, trouver un minimum local à la fonction en partant d’un "point" donné).  
La plupart du temps, on se donne un point (itéré) initial $$ x_0 \in \mathcal{F} (\mathcal{F}=\{\mathcal{f}(x)\})$$, un seuil de tolérance $$\varepsilon \geq 0$$ et un coefficient d’amortissement $$\eta$$.  
L’algorithme de la descente de gradient définit une suite d’itérée. $$ x_0,x_1,x_2,\dots \in \mathcal{F} $$, jusqu’à ce qu’un test d’arrêt soit satisfait.  
Il passe de $$x_k$$ à $$x_{k+1}$$ par les étapes suivantes :

* Simulation : Calcul de la dérivée (gradient) de $$\mathcal{f}:\nabla\mathcal{f}(x_k)$$
* Tant que : $$\lvert\nabla\mathcal{f}(x_k)\rvert > \varepsilon$$
* Nouvel itéré : $$x_{k+1} = x_k - \eta \nabla\mathcal{f}(x_k)$$

À noter que le coefficient d’amortissement permet de contrôler la descente et de ne pas dépasser un minimum local dans le cas où la dérivée serait trop grande, il faut aussi faire attention à ce qu’il ne soit pas trop faible pour que la descente ne soit pas trop longue. Trouver la bonne valeur pour ce coefficient est quelque chose de difficile, empirique et fastidieux.

## Régression linéaire

**Définition** : La régression linéaire consiste à établir une relation linéaire entre une variable, dite expliquée, et une ou plusieurs variables, dites explicatives.

On cherche une fonction $$\mathcal{f}(x)$$ de la forme : $$\mathcal{f}(x)=w^\mathsf{T}x+w_0$$  
On va prendre $$W=\left[w_0 ~~ w\right]$$  
On cherche donc à trouver un $$W$$, pour ce faire on va définir une fonction $$J(W)$$ tel que : $$J(W)={\lVert \mathcal{f}(x) – Y \rVert}^2$$ (On peut reconnaître ici la forme des moindres carrés.)

### Par Système Linaire

Pour résoudre l’équation à l’aide d’un système linéaire, on va utiliser la formule $$J(W)$$, on va ensuite définir un $$Z$$ tel que : $$z_i=\left[1 ~~ x_i\right]$$ (C’est à dire que chaque élément de $$Z$$ correspond à chaque élément de $$X$$ auquel on a rajouté un $$1$$ au début).

Ainsi on va transformer $$J(W)$$ pour qu’elle soit de la forme : $$J(W)={\lVert Z \times W – Y \rVert}^2$$, notons que l’on doit minimiser cette fonction et donc résoudre $$J(W)=0$$ et donc on obtient :

$$
\begin{aligned}
{\lVert ZW – Y \rVert}^2 & = 0\\
Z \times W – Y & = 0\\
Z \times W & = Y\\
Z^{-1} \times Z \times W & = Z^{-1} \times Y\\
W & = Z^{-1} \times Y
\end{aligned}
$${: .Formule}

**Utilisations** : La régression par système linéaire est souvent utilisée dans des applications telles que l'économie, la finance et les sciences sociales.

**Avantages** :

* Facile à interpréter et à comprendre.
* Très rapide à entraîner pour des ensembles de données de petite à moyenne taille.
* Possibilité de visualiser les relations entre les variables d'entrée et la variable cible.

**Inconvénients** :

* Ne conviens pas pour les ensembles de données à dimensions élevées.
* Ne conviens pas pour des relations non linéaires.
* Sensibles aux données aberrantes.

**Exemple python** : [Fichier Python](../_includes/code/classification/Systeme_Lineaire.py)

```python
{% include code/classification/Systeme_Lineaire.py %}
```

### Par Descente de Gradient

Pour résoudre ce problème et trouver $$W$$, nous pouvons utiliser une descente de gradient sur $$J(W)$$. Avec ceci nous pourrons aisément faire tourner l’algorithme de la descente de gradient et donc obtenir un $$W$$ à la fin. Pour ce faire on va définir $$J(W)$$ comme la fonction d’erreur qui correspond a la distance du point vis-à-vis de la droite représentée par $$W$$ tel que :

$$
\begin{aligned}
J(W) & = \frac{1}{N} \times \sum_{i=1}^n{\left(\left(w_0 + w \times x_i\right) - y_i\right)}\\
\frac{\delta J(W)}{\delta w_0} & = \frac{2}{N} \times \sum_{i=1}^n{\left(-\left(y_i - \left(w_0 + w \times x_i\right)\right)\right)}\\
\frac{\delta J(W)}{\delta w} & = \frac{2}{N} \times \sum_{i=1}^n{\left(-x_i\times\left(y_i - \left(w_0 + w \times x_i\right)\right)\right)}
\end{aligned}
$${: .Formule}

**Utilisations** : La régression par descente de gradient est souvent utilisée dans des applications telles que l'apprentissage automatique, l'analyse de données et la reconnaissance de la parole.

**Avantages** : 

* Très efficace pour les grands ensembles de données.
* Peut gérer des relations non linéaires.
* Peut être utilisée pour l'apprentissage profond.

**Inconvénients** :

* Nécessite de trouver un bon taux d'apprentissage.
* Peut converger vers un minimum local.
* Peut être lent pour certains ensembles de données.

**Exemple python** : [Fichier Python](../_includes/code/classification/Descente_Gradient.py)

```python
{% include code/classification/Descente_Gradient.py %}
```

## Arbre de décision

**Définition** : L'apprentissage par arbre de décision consiste à construire un arbre depuis un ensemble d'apprentissage constitué de n-uplets étiquetés. Un arbre de décision peut être décrit comme un diagramme de flux de données (ou flowchart) où chaque nœud interne décrit un test sur une variable d'apprentissage, chaque branche représente un résultat du test, et chaque feuille contient la valeur de la variable cible (une étiquette de classe pour les arbres de classification, une valeur numérique pour les arbres de régression).

**Utilisations** : Les arbres de décision sont souvent utilisés dans des applications telles que la classification d'images, la reconnaissance de la parole et l'analyse des décisions.

**Avantages** : 

* Facile à comprendre et à interpréter.
* Peut gérer des données non numériques.
* Peut être utilisé pour des problèmes de classification et de régression.

**Inconvénients** :

* Peut être sensible aux données bruyantes.
* Peut être sujet à l'overfitting.
* Ne fonctionne pas bien pour des ensembles de données à dimensions élevées.

**Exemple python** : [Fichier Python](../_includes/code/classification/Arbre_de_decision.py)

```python
{% include code/classification/Arbre_de_decision.py %}
```

## Forêts aléatoires (RF)

**Définition** : Les forêts aléatoires (ou Random Forests en anglais) sont une technique de classification ensembliste qui consiste à entraîner plusieurs arbres de décision indépendants les uns des autres et à combiner leurs prédictions pour améliorer la précision de la classification.

Chaque arbre de décision est entraîné sur un échantillon aléatoire des données d'entraînement, avec remplacement, et en utilisant un sous-ensemble aléatoire des variables disponibles. Cette technique permet de réduire la variance des prédictions en introduisant une certaine diversité entre les arbres de décision.

Lors de la classification d'un nouvel exemple, chaque arbre de décision prédit une classe, et la classe majoritaire parmi l'ensemble des prédictions est choisie comme prédiction finale.

Les forêts aléatoires ont démontré leur efficacité dans de nombreuses applications, notamment en vision par ordinateur, en bio-informatique, et en finance. Ils sont particulièrement adaptés aux données à haute dimensionnalité et aux problèmes de classification non-linéaires.

Voici la formule pour le vote majoritaire dans les Random Forests :
$$\hat{y} = \underset{k}{\operatorname{argmax}}\sum_{i=1}^{N_{\text{trees}}} \mathbb{1}_{\{y_i^k = y\}}$$

où $$\hat{y}$$ est la prédiction finale, $$N_{\text{trees}}$$ est le nombre d'arbres de décision dans la forêt, $$y_i^k$$ est la prédiction de l'arbre $$k$$ pour l'exemple $$i$$, et $$\mathbb{1}_{\{y_i^k = y\}}$$ est une fonction indicatrice qui vaut $$1$$ si $$y_i^k = y$$ et $$0$$ sinon.

**Utilisations** : Les forêts aléatoires sont souvent utilisées dans des applications telles que la classification d'images, la reconnaissance de la parole et l'analyse des décisions.

**Avantages** : 

* Peut gérer de grands ensembles de données.
* Peut gérer des données bruyantes.
* Peut être utilisé pour des problèmes de classification et de régression.

**Inconvénients** :

* Peut être lent pour de grands ensembles de données.
* Peut être sujet à l'overfitting.
* Peut être difficile à interpréter.

**Exemple python** : [Fichier Python](../_includes/code/classification/Forets_aleatoires.py)

```python
{% include code/classification/Forets_aleatoires.py %}
```

## k plus proches voisins (k-NN)

**Définition** : La méthode des $$k$$ plus proches voisins comme son nom l'indique consiste à trouver les $$k$$ plus proches (selon une fonction de distance à définir) parmis tout les éléments de la base de données d'apprentissage. La classe retenue sera celle la plus représenté par les $$k$$ échantillons sélectionnés.

**Utilisations** : La Méthode des k plus proches voisins sont souvent utilisées pour la classification d'images, la reconnaissance de formes, la classification de documents et la bio-informatique.

**Avantages** : 

* Facile à comprendre et à implémenter.
* Peut être utilisé pour des problèmes de classification et de régression.
* Peut gérer des données bruyantes.

**Inconvénients** :

* Le temps de prédiction est lent pour les grands ensembles de données.
* Peut être sensible aux valeurs aberrantes.
* Nécessite de choisir une valeur k appropriée.

**Exemple python** : [Fichier Python](../_includes/code/classification/kNN.py)

```python
{% include code/classification/kNN.py %}
```

## Perceptron

**Définition** : Le perceptron peut être vu comme le type de réseau de neurones le plus simple. C'est un classifieur linéaire. Ce type de réseau neuronal ne contient aucun cycle (il s'agit d'un réseau de neurones à propagation avant). Dans sa version simplifiée, le perceptron est mono-couche et n'a qu'une seule sortie à laquelle toutes les entrées sont connectées et les entrées et la sortie sont booléennes. Plus généralement, les entrées peuvent être des nombres réels.

Un perceptron à $$n$$ entrées $$(x_{1},\dots ,x_{n})$$ et à une seule sortie $$o$$ est défini par la donnée de $$n$$ poids (ou coefficients synaptiques) $$(w_{1},\dots ,w_{n})$$ et un biais (ou seuil) $$\theta$$ par :

$$o = \begin{cases} 1 & \mathrm{si} & \sum_{i=1}^{n}w_i x_i > \theta\\0 & \mathrm{sinon} & \end{cases}$${: .Formule}

La sortie $$o$$ résulte alors de l'application de la fonction de Heaviside au potentiel post-synaptique $$z=\sum_{i=1}^{n} w_i x_i$$, avec:

$$ f(z) = \begin{cases} 1 & \mathrm{si} & z > 0 \\0 & \mathrm{si} & z\leq 0 \end{cases} $${: .Formule}

Cette fonction non linéaire est appelée fonction d'activation. Une alternative couramment employée est $$f=\tanh()$$, la tangente hyperbolique.

**Utilisations** : Le Perceptron est souvent utilisé dans la classification binaire et la reconnaissance de caractères.

**Avantages** : 

* Simple à comprendre et facile à implémenter.
* Efficace pour les ensembles de données linéairement séparables.
* Converge rapidement vers une solution.

**Inconvénients** :

* Ne converge pas si les données ne sont pas linéairement séparables.
* Le modèle n'est pas capable de gérer des données non linéaires.
* Sensible aux données bruyantes

**Exemple python** : [Fichier Python](../_includes/code/classification/Perceptron.py)

```python
{% include code/classification/Perceptron.py %}
```

## Machine à vecteurs de support (SVM)

**Définition** : Les machines à vecteurs de support (SVM) sont une méthode d'apprentissage supervisé pour la classification et la régression. Les SVM sont particulièrement utiles pour les problèmes de classifications non linéaires, car elles sont capables de séparer les données en utilisant une fonction de décision non linéaire.

La méthode consiste à trouver un hyperplan qui sépare les données en deux classes en maximisant la marge, c'est-à-dire la distance entre l'hyperplan et les points de chaque classe les plus proches. Les SVM ont également la possibilité d'utiliser des noyaux pour projeter les données dans un espace de dimension supérieure, où la séparation linéaire est possible.
 
Les SVM cherchent à résoudre le problème d'optimisation suivant :

$$\text{minimize}\left(\frac{1}{2}\lVert w\rVert ^2 + C \sum_{i=1}^{n} \max(0, 1 - y_i (w^T x_i + b))\right)$${: .Formule}

où $$w$$ est le vecteur de poids, $$b$$ est le biais, $$C$$ est un paramètre de régularisation, $$y_i$$ est l'étiquette de classe de l'exemple d'entraînement $$i$$ et $$x_i$$ est l'exemple d'entraînement.

L'optimisation de cette fonction de coût est effectuée à l'aide de méthodes d'optimisation convexe telles que la descente de gradient stochastique.

La formule générale d'un SVM est : $$f(x) = sign(w · x + b)$$  
où $$w$$ est le vecteur de poids, $$b$$ est le biais et $$x$$ est le vecteur de caractéristiques d'un exemple. La fonction $$sign$$ retourne $$1$$ si $$f(x)$$ est positif, $$-1$$ sinon.

**Utilisations** : Les SVM sont souvent utilisées dans des applications telles que la classification de textes, la reconnaissance d'images et la bio-informatique.

**Avantages** : 

* Efficaces pour les ensembles de données à dimensions élevées.
* Bonne généralisation et évitent l'overfitting.
* Utilisent des noyaux pour gérer les données non linéaires.

**Inconvénients** : 

* Longue durée d'apprentissage pour de grands ensembles de données.
* Sensibles aux données bruyantes.
* Difficiles à interpréter et à comprendre.

**Exemple python** : [Fichier Python](../_includes/code/classification/SVM.py)

```python
{% include code/classification/SVM.py %}
```

## Analyse discriminante (DA)

**Définition** : L'analyse discriminante (DA) est une méthode statistique qui permet de séparer des groupes de données en utilisant des variables prédictives continues. Elle est principalement utilisée pour la classification de données en deux ou plusieurs groupes, et est souvent utilisée dans les problèmes de classification où il y a une réponse binaire (0/1), tels que la détection de fraude, la segmentation de marché, etc.

Le but de l'analyse discriminante est de trouver une ou plusieurs variables qui permettent de distinguer les groupes de données en minimisant l'erreur de classification. Elle se base sur la création d'une fonction discriminante qui établit une frontière de décision entre les groupes, de sorte que les observations appartenant à un même groupe soient aussi similaires que possible, et que les observations des différents groupes soient aussi différentes que possible.

Il existe deux types d'analyse discriminante : l'analyse discriminante linéaire (LDA) et l'analyse discriminante quadratique (QDA). L'analyse discriminante linéaire est utilisée lorsque les variables prédictives sont linéairement séparables, tandis que l'analyse discriminante quadratique est utilisée lorsque les variables ne sont pas linéairement séparables.

La fonction discriminante pour l'analyse discriminante linéaire est une combinaison linéaire des variables prédictives, tandis que pour l'analyse discriminante quadratique, elle est une combinaison quadratique. L'analyse discriminante linéaire est plus simple et plus rapide à exécuter que l'analyse discriminante quadratique, mais elle peut être moins précise si les données ne sont pas linéairement séparables.

En résumé, l'analyse discriminante est une méthode de classification qui permet de trouver des variables prédictives pour séparer les groupes de données, en minimisant l'erreur de classification. Il existe deux types d'analyse discriminante : l'analyse discriminante linéaire et l'analyse discriminante quadratique, qui diffèrent dans la complexité de la fonction discriminante.

**Utilisations** : L'Analyse discriminante est souvent utilisée dans la reconnaissance de formes, la classification de documents, la bio-informatique et la surveillance de la qualité.

**Avantages** : 

* Efficace pour les ensembles de données contenant de nombreuses variables.
* Prends en compte les corrélations entre les variables.
* Permets de classer les données dans des groupes distincts.

**Inconvénients** :

* Nécessite une normalité des variables.
* Sensible aux données bruyantes.
* Ne fonctionne pas bien avec les ensembles de données de grande dimension.

**Exemple python** : [Fichier Python](../_includes/code/classification/Analyse_discriminante.py)

```python
{% include code/classification/Analyse_discriminante.py %}
```

## Analyse en composantes principales (PCA)

**Définition** : L'Analyse en Composantes Principales (PCA) est une méthode de réduction de dimensionnalité qui permet de trouver les axes principaux d'une distribution de données en maximisant la variance. Elle permet de projeter les données sur un espace de dimension inférieure tout en conservant autant d'information que possible.

Le but est de transformer un ensemble de variables corrélées en un ensemble de variables non corrélées appelées composantes principales. Ces composantes principales permettent de visualiser et d'analyser les données de manière plus simple.

**Utilisations** : L'Analyse en composantes principales est souvent utilisée dans la reconnaissance de formes, l'exploration de données, la visualisation de données et la classification de documents.

**Avantages** : 

* Permets de réduire la dimension des données.
* Préservation de l'information utile dans les données.
* Élimination des données redondantes.

**Inconvénients** :

* Nécessite des données normalisées.
* L'interprétation des résultats est souvent difficile.
* Les composantes principales peuvent ne pas être significatives.

**Exemple python** : [Fichier Python](../_includes/code/classification/PCA.py)

```python
{% include code/classification/PCA.py %}
```

## Analyse de corrélation canonique (CCA)

**Définition** : L'Analyse de corrélation canonique (CCA) est une technique d'analyse statistique qui permet de trouver les corrélations linéaires entre deux ensembles de variables. Cette méthode est souvent utilisée en analyse multivariée pour trouver des relations entre des variables dans deux ensembles différents. CCA est également utilisée en traitement du signal pour la détection de corrélations entre des signaux.

En CCA, on cherche à trouver des vecteurs qui maximisent la corrélation entre les deux ensembles de variables. On peut également chercher à maximiser la corrélation tout en minimisant la redondance entre les deux ensembles.

Pour trouver ces vecteurs, on effectue une analyse en valeurs propres sur la matrice de corrélation entre les deux ensembles de variables. Les vecteurs qui ont les plus grandes valeurs propres sont les vecteurs de corrélation canonique.

Une fois les vecteurs de corrélation canonique trouvés, on peut projeter les données dans l'espace de ces vecteurs pour trouver les relations les plus significatives entre les deux ensembles de variables.

**Utilisations** : L'analyse de corrélation canonique est souvent utilisée dans des domaines tels que la psychologie, la biologie et l'ingénierie.

**Avantages** : 

* Permets d'explorer les relations entre deux ensembles de variables.
* Permets de réduire la dimension des données.
* Permets la régression et la classification.

**Inconvénients** :

* Sensible aux valeurs aberrantes.
* Difficile à interpréter pour des ensembles de données complexes.

**Exemple python** : [Fichier Python](../_includes/code/classification/CCA.py)

```python
{% include code/classification/CCA.py %}
```

## Modèle de Markov caché (HMM)

**Définition** : Le modèle de Markov caché (HMM) est une méthode d'apprentissage automatique qui permet de modéliser des séquences de données, telles que des séquences de mots dans un discours ou des séquences d'observations dans une série temporelle. Un HMM est un modèle probabiliste qui utilise une chaîne de Markov pour modéliser les transitions entre les différents états cachés d'un système, ainsi que les observations émises à partir de ces états.

Plus précisément, un HMM est défini par un ensemble d'états cachés, chacun associé à une distribution de probabilité pour les observations émises, et une matrice de transition qui définit les probabilités de transition entre ces états. En utilisant des algorithmes de type "forward-backward" ou "Viterbi", il est possible d'inférer les séquences les plus probables des états cachés d'un HMM, ainsi que les probabilités associées à ces séquences.

**Utilisations** : Le modèle de Markov caché est souvent utilisé dans des applications telles que la reconnaissance de la parole, la reconnaissance de l'écriture manuscrite et la prédiction de séquences.

**Avantages** : 

* Facilement interprétable.
* Peut être utilisé pour modéliser des données séquentielles telles que la parole et le texte.

**Inconvénients** :

* Difficile à entraîner.
* Sensible aux données bruyantes.

**Exemple python** : [Fichier Python](../_includes/code/classification/HMM.py)

```python
{% include code/classification/HMM.py %}
```

## Distance minimale à la moyenne (MDM)

**Définition** : La distance minimale à la moyenne (MDM) est une méthode de classification supervisée. L'idée de cette méthode est de calculer la distance entre chaque observation d'un ensemble de données et la moyenne de chaque classe. La classe qui a la plus petite distance pour une observation donnée est celle à laquelle cette observation est attribuée. Plus précisément, pour une observation $$x$$, la classe à laquelle $$x$$ est attribuée est :

$$\arg\min_c\left(\lVert x - \mu_c\rVert\right)$${: .Formule}

où $$\mu_c$$ est la moyenne de la classe $$c$$, et $$\lVert \cdot \rVert$$ est une mesure de distance entre deux vecteurs.

Dans le cas de la classification binaire, il suffit de comparer les distances entre l'observation et les moyennes des deux classes et d'attribuer l'observation à la classe avec la plus petite distance.

La MDM est une méthode simple et rapide, mais elle peut être sensible aux valeurs aberrantes et ne fonctionne bien que lorsque les classes sont séparables linéairement.

**Utilisations** : La distance minimale à la moyenne est souvent utilisée dans des applications telles que la reconnaissance de caractères manuscrits et la classification d'images.

**Avantages** : 

* Facilement interprétable.
* Peut être utilisé pour la classification de données avec une faible variance.

**Inconvénients** :

* Peut être sensible aux données bruyantes.
* Peut ne pas être efficace pour les ensembles de données à grande variance.

**Exemple python** : [Fichier Python](../_includes/code/classification/MDM.py)

```python
{% include code/classification/MDM.py %}
```

## Filtrage géodésique avec analyse discriminante de Fisher (FGDA)

**Définition** : Le FGDA est une méthode de classification qui combine l'analyse discriminante de Fisher (FDA) et le filtrage géodésique (GF) pour améliorer la performance de la classification. La méthode FGDA peut être utilisée pour résoudre des problèmes de classification de données multi-classes, tels que la reconnaissance d'objets.

La méthode FGDA commence par effectuer une analyse en composantes principales (PCA) sur les données pour réduire leur dimensionnalité. Ensuite, une transformation géodésique est appliquée aux données pour les projeter sur une sphère unitaire, ce qui permet de simplifier l'espace des données et d'éviter les problèmes de singularité.

Enfin, l'analyse discriminante de Fisher est utilisée pour trouver une direction dans l'espace projeté qui maximise la séparation entre les différentes classes. Cette direction est utilisée pour projeter les données sur une droite, qui est ensuite utilisée pour effectuer la classification.

La méthode FGDA est particulièrement utile pour les données de haute dimensionnalité, où les techniques de classification standard peuvent être difficiles à appliquer en raison de la malédiction de la dimensionnalité.

**Utilisations** : Le filtrage géodésique avec analyse discriminante de Fisher est souvent utilisé dans des applications telles que la reconnaissance d'images et la détection d'objets.

**Avantages** : 

* Peut être utilisé pour extraire des caractéristiques discriminantes à partir de données brutes.
* Peut être utilisé pour la reconnaissance d'images et la détection d'objets.

**Inconvénients** :

* Peut être sensible aux données bruyantes.
* Peut être coûteux en termes de calcul.

**Exemple python** : [Fichier Python](../_includes/code/classification/FGDA.py)

```python
{% include code/classification/FGDA.py %}
```
