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

![WIP](/assets/img/WIP.png){:style="max-width:50%;"}

# Definitions et notions de base
L'**apprentissage automatique** (ou *machine learning*) consiste à apprendre à une machine à résoudre des tâches difficiles par des algorithmes classiques. L'apprentissage automatique est utilisé pour la classification : étiqueter chaque donnée en l'associant à une classe.

Un **classifieur** est un ensemble d’opérations qui permettent de définir à quelle classe appartient un élément.

**Apprentissage supervisé** : L'apprentissage s'effectue grâce à des exemples déjà classsés. On suppose cette base d'apprentissage représentative d'une population d'échantillons plus large et le but des méthodes d'apprentissage supervisé est de bien généraliser, c'est-à-dire d'apprendre une fonction qui fasse des prédictions correctes sur des données non présentes dans l'ensemble d'apprentissage. Il s’agit d’apprendre à classer un nouvel élément parmi un ensemble de classes prédéfinies: on connaît les classes à priori.

**Apprentissage semi-supervisé** : L'apprentissage s'effectue grâce à des exemples déjà classsés et d'autres non. Le nombre de classe ou leur définition peuvent être prédifinies.

**Apprentissage non-supervisé** : L'apprentissage s'effectue grâce à des exemples non classé. Il s'agit, pour un logiciel, de trouver des structures sous-jacentes à partir de données non étiquetées. Le nombre et la définition des classes n’est pas données à priori.


## Espérance, Variance, Écart type, Loi Normale
On va considérer le poids de chaque donnée uniforme pour les différentes formules (si une valeur est plus présente, elle est juste répétée).
### Espérance ($$\mu$$)
En théorie des probabilités, l’espérance mathématique d’une variable aléatoire réelle est, intuitivement, la valeur que l’on s’attend à trouver, en moyenne, si l’on répète un grand nombre de fois la même expérience aléatoire. Elle se note $$\operatorname{E}(X)$$ et se lit « espérance de X ».

Elle correspond à une moyenne pondérée des valeurs que peut prendre cette variable. 

$$ \operatorname{E}(X) = \bar{x} = \frac{1}{n} \times \sum_{i=1}^n x_i $$

### Variance ($$v$$), Ecart type ($$\sigma$$)
En probabilité, l’écart type est une mesure de la dispersion d’une variable aléatoire ; en statistique, il est une mesure de dispersion de données. Il est défini comme la racine carrée de la variance, ou de manière équivalente comme la moyenne quadratique des écarts par rapport à la moyenne. Il a la même dimension que la variable aléatoire ou la variable statistique en question.

$$ \sigma_x = \sqrt{\frac{1}{n} \times \sum_{i=1}^n{\left(x_i-\bar{x}\right)^2}} = \sqrt{\frac{1}{n} \times \left(\sum_{i=1}^n{(x_i^2}\right) - \bar{x}^2} $$

### Loi Normale ($$\mathcal{N}(\mu,\sigma^2)$$)
C’est une loi de probabilité absolument continue qui dépend de deux paramètres : son espérance, un nombre réel noté μ, et son écart type, un nombre réel positif noté σ. La densité de probabilité de la Loi Normale est donnée par :

$$ f(x)=\frac{1}{\sigma\sqrt{2\pi}}\times\mathrm{e}^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2} = \frac{1}{\sigma\sqrt{2\pi}}\times\mathrm{e}^{\frac{-\left(x-\mu\right)^2}{2\sigma^2}}$$

Note : $$\frac{1}{\sigma\sqrt{2\pi}}$$ assure que la fonction intègre à 1. (C’est une constante donc elle ne change pas l’aspect de la courbe.)
La courbe de cette densité est appelée courbe de Gauss ou courbe en cloche, entre autres. C’est la représentation la plus connue de cette loi. La Loi Normale de moyenne nulle et d’écart type unitaire est appelée loi normale centrée réduite ou loi normale standard.

#### Limites
On peut noter que la loi Normale à une valeur très proche de $$0$$ si $$x=\mu \pm 4\sigma$$, on a donc une bonne représentation sur l’intervalle $$\left[\mu - 4\sigma ; \mu + 4\sigma\right]$$. (Proche de $$0$$ car $$ \lim_{x\rightarrow -\infty} \mathrm{e}^x = 0$$

$$ f(\mu \pm 4\sigma) = \frac{1}{\sigma\sqrt{2\pi}}\times\mathrm{e}^{\frac{-\left(\mu \pm 4\sigma-\mu\right)^2}{2\sigma^2}} = \frac{\mathrm{e}^{\frac{-16\sigma^2}{2\sigma^2}}}{\sigma\sqrt{2\pi}} = \frac{\mathrm{e}^{-8}}{\sigma\sqrt{2\pi}}\approx \frac{0.0003}{\sigma\sqrt{2\pi}} $$

#### Fonction Gaussienne
Une fonction gaussienne est une fonction en exponentielle de l’opposé du carré de l’abscisse (une fonction en $$\mathrm{e}^(-x^2)$$). Elle a une forme caractéristique de courbes en cloche. La loi normale est une fonction Gaussienne (univariée, car de dimension 1).

#### Loi Normale Multidimensionnelle, Multinormale, densité Gaussienne multivariée... ($$\mathcal{N}(\mu,\sigma^2)$$)
C’est une généralisation multidimensionnelle de la Loi Normale. 
On a :  
* $$ d $$ : Nombre de dimensions
* $$ x $$ : Valeurs dans un vecteur de dimension $$d$$
* $$ \mu $$ : Espérance dans un vecteur de dimension $$d$$,  
$$\operatorname{E}(X) =\begin{pmatrix} \mu_0\\ \vdots\\ \mu_d \end{pmatrix} = \frac{1}{n} \times \sum_{i=1}^n{\left(x_i \times p(x_i)\right)} $$
* $$ \operatorname{C} $$ : La matrice de covariance  
$$\operatorname{C} = \operatorname{E}\left[\left(X-\operatorname{E}\left[X\right]\right)\left(X - \operatorname{E}\left[X\right]\right)^\mathsf{T}\right] 
= \begin{pmatrix}
\sigma_{x_1}^2 & \sigma_{x_1 x_2} & \cdots & \sigma_{x_1 x_p}\\
\sigma_{x_2 x_1} & \ddots & \cdots & \vdots \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{x_p x_1} & \cdots & \cdots & \sigma_{x_p}^2
\end{pmatrix} $$
* $$ \lvert\operatorname{C}\rvert $$ : Le déterminant de la matrice de covariance
* $$ \operatorname{C}^{-1} $$ : L'inverse de la matrice

$$ p(x)= f_{(\mu,\operatorname{C})}(x) = \mathcal{N}(\mu,\sigma^2)(x) = \frac{1}{({2\pi})^{d/2} \times {\lvert\operatorname{C}\rvert}^{1/2}} \times \mathrm{e}^{-\frac{1}{2} \times \left(x-\operatorname{E}\right)^\mathsf{T}\operatorname{C}^{-1}\left(x-\operatorname{E}\right)} $$

**Note** : Comme pour la Loi Normale univariée, la première partie assure que la densité intègre à 1. 

# Descente de gradient ($$\nabla$$)
La descente de gradient nous permet de minimiser une fonction $$\mathcal{f}$$ (c’est-à-dire, trouver un minimum local à la fonction en partant d’un "point" donné).  
La plupart du temps, on se donne un point (itéré) initial $$ x_0 \in \mathcal{F} (\mathcal{F}=\{\mathcal{f}(x)\})$$, un seuil de tolérance $$\varepsilon \geq 0$$ et un coefficient d’amortissement $$\eta$$.  
L’algorithme de la descente de gradient définit une suite d’itérée. $$ x_0,x_1,x_2,\dots \in \mathcal{F} $$, jusqu’à ce qu’un test d’arrêt soit satisfait.  
Il passe de $$x_k$$ à $$x_{k+1}$$ par les étapes suivantes :
* Simulation : Calcul de la dérivée (gradient) de $$\mathcal{f}:\nabla\mathcal{f}(x_k)$$
* Tant que : $$\lvert\nabla\mathcal{f}(x_k)\rvert > \varepsilon$$
* Nouvel itéré : $$x_{k+1} = x_k - \eta \nabla\mathcal{f}(x_k)$$

À noter que le coefficient d’amortissement permet de contrôler la descente et de ne pas dépasser un minimum local dans le cas où la dérivée serait trop grande, il faut aussi faire attention à ce qu’il ne soit pas trop faible pour que la descente ne soit pas trop longue. Trouver la bonne valeur pour ce coefficient est quelque chose de difficile, empirique et fastidieux.


# Régression linéaire
La regression linéaire consiste à établir une relation linéaire entre une variable, dite expliquée, et une ou plusieurs variables, dites explicatives.

On cherche une fonction $$\mathcal{f}(x)$$ de la forme : $$\mathcal{f}(x)=w^\mathsf{T}x+w_0$$  
On va prendre $$W=\left[w_0 ~~ w\right]$$  
On cherche donc à trouver un $$W$$, pour ce faire on va définir une fonction $$J(W)$$ tel que : $$J(W)={\lVert \mathcal{f}(x) – Y \rVert}^2$$ (On peut reconnaître ici la forme des moindres carrés.)

## Par Système Linaire
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
$$

## Par Descente de Gradient
Pour résoudre ce problème et trouver $$W$$, nous pouvons utiliser une descente de gradient sur $$J(W)$$. Avec ceci nous pourrons aisément faire tourner l’algorithme de la descente de gradient et donc obtenir un $$W$$ à la fin. Pour ce faire on va définir $$J(W)$$ comme la fonction d’erreur qui correspond a la distance du point vis-à-vis de la droite représentée par $$W$$ tel que : 

$$
\begin{aligned}
J(W) & = \frac{1}{N} \times \sum_{i=1}^n{\left(\left(w_0 + w \times x_i\right) - y_i\right)}\\ 
\frac{\delta J(W)}{\delta w_0} & = \frac{2}{N} \times \sum_{i=1}^n{\left(-\left(y_i - \left(w_0 + w \times x_i\right)\right)\right)}\\ 
\frac{\delta J(W)}{\delta w} & = \frac{2}{N} \times \sum_{i=1}^n{\left(-x_i\times\left(y_i - \left(w_0 + w \times x_i\right)\right)\right)}
\end{aligned}
$$


# Arbre de décision
L'apprentissage par arbre de décision consiste à construire un arbre depuis un ensemble d'apprentissage constitué de n-uplets étiquetés. Un arbre de décision peut être décrit comme un diagramme de flux de données (ou flowchart) où chaque nœud interne décrit un test sur une variable d'apprentissage, chaque branche représente un résultat du test, et chaque feuille contient la valeur de la variable cible (une étiquette de classe pour les arbres de classification, une valeur numérique pour les arbres de régression). 

# Forêts aléatoires (RF)

# Méthode des k plus proches voisins (k-NN)
La méthode des k plus proches voisins comme son nom l'indique consiste à trouver les k plus proches (selon une fonction de distance à définir) parmis tout les éléments de la base de données d'apprentissage. La classe retenue sera celle la plus représenté par les k échantillons sélectionnés.

# Perceptron
Le perceptron peut être vu comme le type de réseau de neurones le plus simple. C'est un classifieur linéaire. Ce type de réseau neuronal ne contient aucun cycle (il s'agit d'un réseau de neurones à propagation avant). Dans sa version simplifiée, le perceptron est mono-couche et n'a qu'une seule sortie à laquelle toutes les entrées sont connectées et les entrées et la sortie sont booléennes. Plus généralement, les entrées peuvent être des nombres réels.

Un perceptron à $$n$$ entrées $$(x_{1},\dots ,x_{n})$$ et à une seule sortie $$o$$ est défini par la donnée de $$n$$ poids (ou coefficients synaptiques) $$(w_{1},\dots ,w_{n})$$ et un biais (ou seuil) $$\theta$$ par :

$$o = \begin{cases} 1 & \mathrm{si} & \sum_{i=1}^{n}w_i x_i > \theta\\0 & \mathrm{sinon} & \end{cases}$$

La sortie $$o$$ résulte alors de l'application de la fonction de Heaviside au potentiel post-synaptique $$z=\sum_{i=1}^{n} w_i x_i$$, avec:

$$ f(z) = \begin{cases} 1 & \mathrm{si} & z > 0 \\0 & \mathrm{si} & z\leq 0 \end{cases} $$

Cette fonction non linéaire est appelée fonction d'activation. Une alternative couramment employée est $$f=\tanh()$$, la tangente hyperbolique. 

# Machine à vecteurs de support (SVM)

# Analyse discriminante (DA)

# Analyse discriminante linéaire (LDA)

# Analyse en composantes principales (PCA)

# Analyse de corrélation canonique (CCA)

# Modèle de Markov caché (HMM)

# Distance minimale à la moyenne (MDM)

# Filtrage géodésique avec analyse discriminante de Fisher (FGDA)