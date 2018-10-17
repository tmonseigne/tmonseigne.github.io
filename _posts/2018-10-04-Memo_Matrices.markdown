---
layout: post
title: Mémo Matrices
date: 2018-10-04
description: Mémo Matrices
img: theme/Memo-Theme.jpg # Add image post (optional)
tags: [Mémos]
author: Thibaut Monseigne # Add name author (optional)
---

* TOC
{:toc}
{: .toc-post}

![WIP](/assets/img/WIP.png){:style="max-width:50%;"}

**Sources principales :** 
1. [fr.wikipedia.org/wiki/Matrice_(mathématiques)](https://fr.wikipedia.org/wiki/Matrice_(mathématiques))
2. **Petersen, Kaare Brandt and Pedersen, Michael Syskind 2012**. The Matrix Cookbook. *Technical University of Denmark*, 72.

**Outils en ligne :** 
1. [matrixcalc.org/fr/](https://matrixcalc.org/fr/)

# Formes, Transformations, Relations, Propriétés
## Formes
* Une matrice **colonne** (ligne) possède une seule colonne (ligne).
* Une matrice **carrée** possède le même nombre de ligne et de colonne.
* Une matrice **triangulaire** est une matrice carrée dont une partie triangulaire des valeurs, délimitée par la diagonale principale, est nulle.
* Une matrice **diagonale** est une matrice carrée dont les coefficients en dehors de la diagonale principale sont nuls.
* Une matrice **symétrique** est une matrice carrée qui est égale à sa propre transposée.
* Une matrice **identité** est une matrice carrée (notée $$I_n$$) avec des 1 sur la diagonale et des 0 partout ailleurs.

## Transformations
* La **transposée** d'une matrice $$M \in \mathcal{M}_{n,m}$$ (notée $$M^{\mathsf{T}}$$) est obtenue en échangeant les lignes et les colonnes de $$M$$.
* La **conjuguée** d'une matrice $$M$$ sur les complexes (notée $$\overline{M}$$) formée des éléments de A conjugués.  
Si $$A$$ est la conjuguée de $$B$$ alors $$B$$ est la conjuguée de $$A$$. On dit que $$A$$ et $$B$$ sont conjuguées.
* La **transconjuguée** (ou **adjointe**) d'une matrice $$M$$ (notée $$M^*$$) sur les complexes est la transposée de la conjuguée de $$M$$.
* Une matrice carrée $$M$$ d'ordre $$n$$ est **inversible** s'il existe une matrice inverse (notée $$M^{-1}$$) de telle sorte que $$MM^{-1}=M^{-1}M=I_n$$.
* Une matrice carrée $$M$$ d'ordre $$n$$ est **diagonalisable** s'il existe une matrice **inversible** P et une matrice **diagonale** $$D$$ de telle sorte que $$M=PDP^{-1}$$.

**Exemple :** 

$$\begin{align}
A=\begin{pmatrix}1&3&5\\2&4&6\end{pmatrix} &\quad\Rightarrow\quad A^{\mathsf{T}}=\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}\\
A=\begin{pmatrix}3+i & 5\\2-2i & i\end{pmatrix} &\quad\Rightarrow\quad \bar{A}=\begin{pmatrix}3-i & 5\\2 + 2i & -i\end{pmatrix}\\
A=\begin{pmatrix}3+i & 5\\2-2i & i\end{pmatrix} &\quad\Rightarrow\quad A^*= \bar{A}^{\mathsf{T}} = \overline{A^{\mathsf{T}}} = \begin{pmatrix}3-i & 2 + 2i\\5& -i\end{pmatrix}
\end{align}$$

## Relations 
* Deux matrices carrées A et B (de même taille) sont dites **congruentes** s'il existe une matrice inversible $$P$$ telle que : $$B = PAP^{\mathsf{T}}$$
* Deux matrices carrées A et B (de même taille) sont dites **semblables** s'il existe une matrice inversible $$P$$ telle que : $$B = PAP^-1$$

## Valeurs propres, Vecteurs propres
* Un vecteur est dit vecteur propre par une application linéaire s'il est non nul et si l'application ne fait que modifier sa taille sans changer sa direction (à ne pas confondre avec son sens !).
* Une valeur propre associée à un vecteur propre est le facteur de modification de taille, c’est-à-dire le nombre par lequel il faut multiplier le vecteur pour obtenir son image. Ce facteur peut être positif, négatif (renversement du sens du vecteur) ou nul (vecteur transformé en un vecteur de longueur nulle).
* Un espace propre associé à une valeur propre est l'ensemble des vecteurs propres qui ont une même valeur propre et le vecteur nul. Ils subissent tous la multiplication par le même facteur.

## Trace
La trace d'une matrice carrée A est définie comme la somme de ses coefficients diagonaux et est notée $$\mathrm{Tr}(A)$$. La trace peut être vue comme une forme linéaire sur l'espace vectoriel des matrices.  
Elle vérifie l'identité : $$\mathrm{Tr}(AB) = \mathrm{Tr}(BA)$$, et est en conséquence invariante par similitude.

### Trace d'une matrice carrée
Étant donnée une matrice carrée : $$ A =(a_{ij})_{1 \leq i, j \leq n} $$

$$\mathrm{Tr}(A)=\sum _{i=1}^{n}a_{ii}$$

Pour toutes matrices carrées $$A$$ et $$B$$ (de même ordre) et pour tout scalaire $$\alpha$$, les propriétés suivantes sont vérifiées : 

$$\begin{matrix}\mathrm{Tr}(A+B) &=& \mathrm{Tr}(A) + \mathrm{Tr}(B)\\
\mathrm{Tr}(\alpha A) &=& \alpha\mathrm{Tr}(A)\\
\mathrm{Tr}(A^{\mathsf{T}}) &=& \mathrm{Tr}(A)\\
\mathrm{Tr}(AB) &=& \mathrm{Tr}(BA)\\
\mathrm{Tr}(P^{-1}AP) &=& \mathrm{Tr}(A)
\end{matrix}$$

**Exemple** :

$$A=\begin{pmatrix}1&3\\2&4\end{pmatrix} \quad\Rightarrow\quad \mathrm{Tr}(A)=5$$


## Matrice de Covariance
La covariance (notée $$\operatorname{Cov}(X,Y)$$ ou $$\sigma_{XY}$$) désigne les variations simultanées de deux variables aléatoires réelles $$X$$ et $$Y$$ ayant chacune une variance , est la valeur :

La matrice de covariance d'un vecteur de p variables aléatoires $$\vec{X}=\begin{pmatrix}X_1\\\vdots \\X_p\end{pmatrix}$$ dont chacune possède une variance, est la matrice carrée dont le terme générique est donné par : $$a_{i,j} = \textrm{Cov}\left(X_i,X_j\right)$$

$$C_{\vec{X}} = 
\begin{pmatrix}
\sigma_{x_1}^2 & \sigma_{x_1 x_2} & \cdots & \sigma_{x_1 x_p}\\
\sigma_{x_2 x_1} & \ddots & \cdots & \vdots \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{x_p x_1} & \cdots & \cdots & \sigma_{x_p}^2
\end{pmatrix}$$


**Calcul de la covariance** :

$$ \operatorname{Cov}\left(X,Y\right)=\operatorname{E}\left[\left(X-\operatorname{E}\left[X\right]\right)\left(Y-\operatorname{E}\left[Y\right]\right)\right] = \operatorname{E}\left[XY\right]-\operatorname{E}\left[X\right]\operatorname{E}\left[Y\right]$$

**Propriétés** : 
* La matrice de covariance est **symétrique** ; ses éléments diagonaux sont les variances et les éléments extra-diagonaux sont les covariances des couples de variables.
* La matrice de covariance est **semi-définie positive** (ses valeurs propres sont positives ou nulles).  
Elle est **définie positive** (valeurs propres strictement positives) s'il n'existe aucune relation affine presque sûre entre les composantes du vecteur aléatoire.
* L'inverse de la matrice de covariance est parfois désignée **matrice de précision**.
* Soit une application linéaire $$F$$ de $$\mathcal{M}_{n,m}(\mathbb{R})$$  de matrice $$M$$.  
Soit $$\vec{X}=\begin{pmatrix}X_1\\\vdots \\X_p\end{pmatrix}$$ un vecteur aléatoire de matrice de covariance $$C$$ de $$\mathcal{M}_{n}(\mathbb{R})$$.  
Alors le vecteur aléatoire $$F(X)$$ a pour matrice de covariance $$MCM^{\mathsf{T}}$$.
* $$ \left\lvert\operatorname{Cov}\left(X,Y\right)\right\rvert \leq \sqrt{\operatorname{Var}{\left(X\right)}\operatorname{Var}{\left(Y\right)}}$$

## Matrice symétrique définie positive (SPD)

Soit $$M$$ une matrice symétrique réelle d'ordre $$n$$. Elle est dite définie positive si elle est positive et inversible, autrement dit si elle vérifie l'une des quatre propriétés équivalentes suivantes : 

* Pour toute matrice colonne (avec une seule colonne) non nulle $$\textbf{x}$$ à n éléments réels, on a : $$\textbf{x}^{\mathsf{T}} M \textbf{x} > 0$$
* Toutes les valeurs propres de $$M$$ (qui sont nécessairement réelles) sont strictement positives.
* La forme bilinéaire symétrique $$\mathbb{R}^{n}\times \mathbb{R}^{n} \to \mathbb{R} ,\quad (\textbf{x},\textbf{y}) \mapsto \textbf{x}^\mathsf{T} M \textbf{y}$$ est un produit scalaire sur $$\mathbb{R}^{n}$$.
* Il existe une matrice $$N \in \mathcal{M}_{n} (\mathbb{R}) $$ inversible telle que $$M = N^{\mathsf{T}}N$$ (autrement dit : $$M$$ est congruente à la matrice identité).

**Exemple :**

$$A = \begin{pmatrix}1 & 1 & 1 & 1\\ 1 & 5 & 5 & 5\\ 1 & 5 & 14 & 14 \\ 1 & 5 & 14 & 15 \end{pmatrix}$$


# Déterminant
## Formule de Leibniz
Le calcul du déterminant d'une matrice est nécessaire pour calculer l'inverse d'une matrice.

Le déterminant de la matrice carrée $$A=\begin{pmatrix}a_{1,1}&\cdots &a_{1,n}\\\vdots &\ddots &\vdots \\a_{n,1}&\cdots &a_{n,n}\end{pmatrix}$$ par la formule de Leibniz : 

$$ \det(A) = \begin{vmatrix} a_{1,1} & \cdots & a_{1,n}\\ \vdots & \ddots & \vdots\\ a_{n,1} & \cdots & a_{n,n} \end{vmatrix}=\sum_{\sigma \in \mathfrak{S}_{n}} \varepsilon(\sigma) \prod_{i=1}^{n} a_{\sigma(i),i}$$

où $$\mathfrak {S}_{n}$$ désigne l'ensemble des permutations de $${ 1 , \cdots , n }$$ et $$\varepsilon(\sigma)$$ la signature de la permutation $$\sigma$$.  
Il s'agit d'effectuer tous les produits possibles en prenant un élément par ligne et par colonne dans la matrice, de les multiplier tantôt par -1 pour chaque élément de gauche sous un élément de droite, et de faire la somme des n! termes ainsi obtenus.

**Exemple :**

$$A = \begin{pmatrix}-2 & 2 & -3\\ -1 & 1 & 3\\ 2 & 0 & -1 \end{pmatrix}$$

$$\begin{matrix}\det(A) & = &(-2)\cdot 1 \cdot (-1) & + & (-3)\cdot 0 \cdot (-1) & + & 2\cdot 3 \cdot 2 & - & (-3) \cdot 1 \cdot 2 & - & (-2) \cdot 3 \cdot 0 & - & 2 \cdot (-1) \cdot (-1)\\
& = & 2 & + & 0 & + & 12 & - & (-6) & - & 0 & - & 2\\
& = & 18 \end{matrix}$$

## Méthode de Laplace
On peut aussi calculer le déterminant d'une matrice de taille $$n$$ à l'aide de $$n$$ déterminants de matrices de taille $$n - 1$$ obtenues en enlevant à la matrice de départ une ligne et une colonne. Si $$A$$ est la matrice, pour tout $$i$$ et $$j$$, on note $$A_{i,j}$$ la matrice obtenue en enlevant à A sa $$i$$-ème ligne et sa $$j$$-ième colonne. 

$$A_{i,j}=\begin{pmatrix}a_{1,1} & \dots & a_{1,j-1} & a_{1,j+1}& \dots & a_{1,n} \\\vdots & \ddots & \vdots & \vdots& \ddots &\vdots\\ a_{i-1,1} & \dots & a_{i-1,j-1}& a_{i-1,j+1}& \dots & a_{i-1,n} \\ a_{i+1,1} & \dots & a_{i+1,j-1}& a_{i+1,j+1}& \dots & a_{i+1,n} \\ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots\\ a_{n,1} & \dots & a_{n,j-1}& a_{n,j+1}& \dots & a_{n,n}\end{pmatrix}$$

On peut alors développer le calcul du déterminant de A suivant une ligne ou une colonne.

Développement suivant la ligne $$i$$ : 

$$\det(A)=\sum_{j=1}^{n} a_{i;j} (-1)^{i+j}\det(A_{i,j})$$

**Exemple :**

$$\begin{matrix}\det(A) = \begin{vmatrix}-2 & 2 & -3\\ -1 & 1 & 3\\ 2 & 0 & -1 \end{vmatrix} & = & 2 \times (-1)^{1+2}\times \begin{vmatrix}-1 & 3\\ 2 & -1\end{vmatrix} & + & 1 \times (-1)^{2+2}\times \begin{vmatrix}-2 & -3\\ 2 & -1\end{vmatrix}\\
& = & (-2)\times((-1)\times(-1)-2 \times 3) & + & 1\times((-2)\times(-1)-2\times(-3)) \\
& = & (-2)\times(-5) & + & 8\\
& = & 18 \end{matrix}$$

**Remarque :** $$ \det(A) = \det(A^{\mathsf{T}}) $$

## Déterminant d'une matrice de dimension 2

$$\begin{vmatrix} a & b\\c & d \end{vmatrix} = a \times d - b \times c$$

## Déterminant d'une matrice de dimension 3

$$
\begin{matrix}
|A| = \begin{vmatrix}a&b&c\\d&e&f\\g&h&i\end{vmatrix} & = & a \times \begin{vmatrix}\Box &\Box &\Box \\\Box &e&f\\\Box &h&i\end{vmatrix} & - & b \times \begin{vmatrix}\Box &\Box &\Box \\d&\Box &f\\g&\Box &i\end{vmatrix} & + & c \times \begin{vmatrix}\Box &\Box &\Box \\d&e&\Box \\g&h&\Box \end{vmatrix} \\
& = & a \times \begin{vmatrix}e&f\\h&i\end{vmatrix} & - & b \times \begin{vmatrix}d&f\\g&i\end{vmatrix} & + & c \times \begin{vmatrix}d&e\\g&h\end{vmatrix}\\ 
& = & a \times (e \times i - f \times h) & + & b \times (f \times g - d \times i) & + & c \times (d \times h - e \times g)
\end{matrix}
$$

## Déterminant de Gram
Soit $$\mathcal{E}$$, un espace préhilbertien réel. Si $$x_1, \dots, x_n$$ sont $$n$$ vecteurs de $$\mathcal{E}$$, la matrice de Gram associée est la matrice symétrique de terme général $$\left(x_i \mid x_j\right)$$ (le produit scalaire des vecteurs $$x_i$$ et $$x_j$$). Le déterminant de Gram est le déterminant de cette matrice, soit : 

$$G\left(x_1, \dots ,x_n\right) = {\begin{vmatrix}\left(x_1|x_1\right) & \left(x_1|x_2\right) & \dots & \left(x_1|x_n\right)\\ \left(x_2|x_1\right) & \left(x_2|x_2\right) & \dots & \left(x_2|x_n\right)\\\vdots & \vdots & \ddots & \vdots \\ \left(x_n|x_1\right) & \left(x_n|x_2\right) & \dots & \left(x_n|x_n\right)\end{vmatrix}}$$


# Norme Matricielle
## Norme de Frobenius

La norme de Frobenius sur $$\mathrm{M}_{m,n}(K)$$ est celle qui dérive du produit scalaire ou hermitien standard sur cet espace, à savoir

$$ (A, B) \in \mathrm{M}_{m,n}(K)^{2} \mapsto \langle A, B \rangle =\operatorname{tr} (A^{*}B)=\operatorname{tr} (BA^*) $$

où $$ A^* $$ désigne la matrice adjointe de $$A$$ et $$\operatorname{tr}$$ la trace. La norme de Frobenius est souvent notée : 

$$\left\lVert A \right\rVert_{F}:=(\operatorname{tr} A^{*}A)^{1/2}=(\operatorname{tr} AA^{*})^{1/2} = {\sqrt{\sum_{1\leq i\leq m \atop 1\leq j\leq n}\left|A_{ij}\right|^{2}}}$$

C'est la norme euclidienne ou hermitienne standard de la matrice considérée comme une collection de $$mn$$ scalaires.

Si $$K=\mathbb{R}$$, le point de vue précédent permet d'en déduire le sous-différentiel de la norme de Frobenius, qui s'écrit en $$A \in \mathrm{M}_{m,n}(\mathbb{R})$$ :

$$ \partial \left(\left\lVert \cdot \right\rVert_{F}\right)(A) = \{ B \in \mathrm{M}_{m,n}(K) \mid \left\lVert B \right\rVert_{F} \leq 1,~ \langle B,A \rangle =\left| A \right|_{F} \} $$

En réalité, $$\left\lVert \cdot \right\rVert_{F}$$ est différentiable sauf en zéro où $$ \partial (\left\lVert \cdot \right\rVert_{F})(A) $$ est la boule unité pour la norme de Frobenius.

La norme de Frobenius n'est pas une norme subordonnée, parce que  $$\left\lVert I_{n} \right\rVert_{F}=\sqrt{n}$$, mais c'est une norme sous-multiplicative : $$\left\lVert AB \right\rVert_{F}\leqslant \left\lVert A \right\rVert_{F} \left\lVert B \right\rVert_{F}$$. 

# Matrice de Distance
Si $$A$$ est une matrice de distance euclidienne et les points $$x_1, x_2,\dots, x_n$$ sont définis sur un espace à $$m$$ dimensions, les éléments de $$A$$ sont donnés par : 

$${\begin{aligned} A & = (a_{ij});\\ a_{ij} & = d_{ij}^{2}\; = \; \lVert x_i-x_j \rVert_2^2\end{aligned}}$$

où $$\left\lVert \cdot \right\rVert_2$$ désigne la norme 2 sur $$\mathbb{R}^m$$.

$$ A = \begin{pmatrix}0 & d_{12}^{2} & \dots & d_{1n}^{2}\\ d_{21}^{2} & 0 & \dots & d_{2n}^{2}\\ \vdots & \vdots & \ddots & \vdots & \\d_{n1}^{2} & d_{n2}^{2} & \dots & 0 \end{pmatrix} $$

# Puissance, Exponentiel et Logarithme d'une matrice
## Racine Carrée
Soient un entier naturel $$n$$ non nul et $$M$$ une matrice carrée d'ordre $$n$$ à coefficients dans un anneau $$\mathbb{A}$$. Un élément $$R$$ de $$\mathcal{M}_{n}(\mathbb{A})$$ est une racine carrée de $$M$$ si $$R^2 = M$$.

Une matrice donnée peut n'admettre aucune racine carrée, comme un nombre fini, voire infini, de racines carrées. 

## Exponentiel et Logarithme

Pour toute matrice $$M$$, son exponentielle est donnée par: $$\exp(M) = \mathrm{e}^{M} = \sum_{k \in \mathbb{N} }{\frac{M^{k}}{k!}}$$. Comme dans le cas scalaire, le logarithme de la matrice est défini comme l'inverse de l'exponentielle.

Si D est une matrice diagonale, c'est-à-dire :

$$ D={\begin{pmatrix}d_{1}&0&\ldots &0\\0&d_{2}&\ldots &0\\\vdots &\vdots &\ddots &\vdots \\0&0&\ldots &d_{n}\end{pmatrix}} $$

alors son exponentielle est obtenue en calculant l'exponentielle de chacun des termes de la diagonale principale :

$$ \mathrm{e}^{D}={\begin{pmatrix}\mathrm{e}^{d_1} & 0 & \ldots & 0\\0 & \mathrm{e}^{d_2} & \ldots & 0\\\vdots & \vdots & \ddots & \vdots \\0 & 0 & \ldots & \mathrm{e}^{d_n}\end{pmatrix}} $$

Si A est une matrice diagonalisable, c'est-à-dire : $$ A=PDP^{-1} $$

où D est diagonale, alors : $$ \mathrm{e}^{A} = P \mathrm{e}^{D} P^{-1} $$

L'application exponentielle préserve ainsi les espaces propres, soit les sous-espaces engendrés par les vecteurs colonnes de $$P$$.

De plus, les valeurs propres de $$\mathrm{e}^{A}$$ sont les exponentielles de celles de $$A$$, soit les éléments de $$\mathrm{e}^{D}$$. 

# Identités remarquables

$$
\begin{matrix}
  \left( A^{\mathsf{T}} \right)^{-1} = \left( A^{-1} \right)^{\mathsf{T}} \quad & \quad \left( AB \right)^{-1} = B^{-1} A^{-1} \quad & \quad \left( ABC \dots \right)^{-1} = \dots C^{-1} B^{-1} A^{-1}\\ 
  \left( A + B \right)^{\mathsf{T}} = A^{\mathsf{T}} + B^{\mathsf{T}} \quad & \quad \left( AB \right)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}} \quad & \quad \left( ABC \dots \right)^{\mathsf{T}} = \dots C^{\mathsf{T}} B^{\mathsf{T}} A^{\mathsf{T}} \\ 
   \left( A + B \right)^{H} = A^{H} + B^{H} \quad & \quad \left( AB \right)^{H} = B^{H} A^{H} \quad & \quad \left( ABC \dots \right)^{H} = \dots C^{H} B^{H} A^{H}\\
\end{matrix}
$$

$$ A^{-1} B = A^{-1/2} B A^{-1/2} $$