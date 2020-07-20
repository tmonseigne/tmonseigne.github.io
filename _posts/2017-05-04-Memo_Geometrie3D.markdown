---
layout: post
title: Mémo Géometrie dans l'espace
date: 2017-05-04
description: Mémo Géometrie dans l'espace
img: theme/Memo-Theme.png # Add image post (optional)
tags: [Mémos]
author: Thibaut Monseigne # Add name author (optional)
---

* TOC
{:toc}
{: .toc-post}

## Quelques Conventions / Définitions

Voici quelques définitions d'objets généraux utilisé par la suite.

|Origine : |$$\mathcal{O}$$&nbsp;&nbsp;&nbsp;|Centre : |$$\mathcal{C}$$.|Direction : |$$\mathcal{D}$$|Rayon (cercle, sphère) : $$\mathcal{r}$$|Diamètre (cercle, sphère) : $$\mathcal{d}$$|
|Point : |$$\mathcal{P}$$|Normale : |$$\mathcal{N}$$&nbsp;&nbsp;&nbsp;|Vecteurs : |$$V$$ ou $$\vec{v}$$&nbsp;&nbsp;&nbsp;|Coordonnées dans l'espace : |$$(x,y,z)$$ ou $$(\vec{u},\vec{v},\vec{w})$$|

|Espace quelconque : |$$\mathcal{E}$$|
|Espace muni d'un repère orthonormé direct $$(\mathcal{O},\vec{i},\vec{j},\vec{k})$$ : |$$\mathcal{E_\bot}$$|

|Rayon : |$$\mathcal{R}$$|Origine : |$$\mathcal{R_O}$$ &nbsp;&nbsp;&nbsp;|Direction : |$$\mathcal{R_D}$$ &nbsp;&nbsp;&nbsp;|Equation : |$$\mathcal{R}(t) = \mathcal{R_D}\times t + \mathcal{R_O}$$&nbsp;&nbsp;&nbsp;|
|Sphère : |$$\mathcal{S}$$ &nbsp;&nbsp;&nbsp;|Centre : |$$\mathcal{S_C}$$ &nbsp;&nbsp;&nbsp;|Rayon : |$$\mathcal{S_r}$$ &nbsp;&nbsp;&nbsp;|Equation : |$${\lVert p-\mathcal{S_C}\rVert}^2-\mathcal{S_r}^2 = 0$$|
|Plan : |$$\mathcal{P}$$|Origine : |$$\mathcal{P_O}$$ &nbsp;&nbsp;&nbsp;|Normale : |$$\mathcal{P_N}$$ &nbsp;&nbsp;&nbsp;|Equation : |$$\left( p-\mathcal{P_O} \right)\cdot \mathcal{P_N} = 0$$|

$$\times$$ correspond à multiplier sauf lorsque l'un a deux vecteurs, il s'agit du produit croisés, on utilisera * à la place.

[Mémo Trigonométrie](../Memo-Trigonometrie/){:target="_blank"}  
[Mémo Espace vectoriel](../Memo-Vecteurs/){:target="_blank"}

## Intersection
Pour calculer une intersection à partir d’équation, il suffit de trouver un point commun à ces équations.  
L’ensemble des points d’un rayon $$\mathcal{R}$$ obéi à la fonction affine $$\mathcal{R}(t) = \mathcal{R_D}\times t + \mathcal{R_O}$$ où $$t$$ pourrait être symbolisé comme le temps passé sur le rayon (demi-droite, car t ne doit pas être inférieur à 0).

### Rayon (demi-droite) / Sphère
Voici l’équation de l’ensemble des points $$\mathcal{p}$$ d’une sphère de centre $$\mathcal{S_C}$$ et de rayon $$\mathcal{S_r}$$ : $${\lVert \mathcal{p}-\mathcal{S_C}\rVert}^2-\mathcal{S_r}^2 = 0$$  
On substitue $$\mathcal{p}$$ par $$\mathcal{R}(t)$$ :

|:---|:---|:---|
|$${\lVert \mathcal{R}(t)-\mathcal{S_C}\rVert}^2-\mathcal{S_r}^2$$|$$=$$|$$0$$|
|$${\lVert \mathcal{R_D}\times t + \mathcal{R_O}-\mathcal{S_C}\rVert}^2-\mathcal{S_r}^2$$|$$=$$|$$0$$|

On n’oublie pas que $$t$$ et $$\mathcal{S_r}$$ ne sont que des nombres et le reste des vecteurs. Mais aussi qu’une norme carrée n’est rien de plus qu’un produit scalaire d’un vecteur par lui-même et la distributivité fonctionne comme pour une multiplication normale. On va prendre $$\mathcal{OC} = \mathcal{R_O}-\mathcal{S_C}$$

|:---|:---|:---|
|$${\lVert \mathcal{R_D}\times t\rVert}^2 + 2\times t \times \mathcal{R_D} \cdot \mathcal{OC} + {\lVert\mathcal{OC}\rVert}^2-\mathcal{S_r}^2$$|$$=$$|$$0$$|
|$${\lVert \mathcal{R_D} \rVert}^2 \times t^2 + 2 \times \left( \mathcal{R_D} \cdot \mathcal{OC} \right) \times t  + {\lVert\mathcal{OC}\rVert}^2-\mathcal{S_r}^2$$|$$=$$|$$0$$|

On a une équation de la forme $$ax^2+bx+c=0$$ avec :
$$\begin{cases} a & = & {\lVert \mathcal{R_D} \rVert}^2\\ b & = & 2 \times \left( \mathcal{R_D} \cdot \mathcal{OC} \right)\\ c & = & {\lVert\mathcal{OC}\rVert}^2-\mathcal{S_r}^2\end{cases}$$

Pour la résoudre il nous faut un delta tel que : $$\Delta = b^2-4ac$$.  
On a trois cas de figure :

* $$\Delta < 0$$ : Il n’y a aucune solution (dans notre cas, pas d’intersection).
* $$\Delta = 0$$ : Il n’y a qu’une solution : $$t = -\frac{b}{2a}$$.
* $$\Delta > 0$$ : Il y a deux solutions : $$t_1 = -\frac{b-\sqrt{\Delta}}{2a}$$ et $$t_2 = -\frac{b+\sqrt{\Delta}}{2a}$$

Si $$t<0$$ on ne le prend pas, car il se situe avant l'origine du rayon.

### Rayon (demi-droite) / Plan

Voici l’équation de l’ensemble des points $$\mathcal{p}$$ du plan qui possède le point $$\mathcal{P_O}$$ et la normale $$\mathcal{P_N}$$ : $$\left( p-\mathcal{P_O} \right)\cdot \mathcal{P_N} = 0$$  
On substitue $$\mathcal{p}$$ par $$\mathcal{R}(t)$$ :

|:---|:---|:---|
|$$\left(\mathcal{R}(t)-\mathcal{P_O} \right)\cdot \mathcal{P_N}$$|$$=$$|$$0$$|
|$$\left(\mathcal{R_D}\times t + \mathcal{R_O}-\mathcal{P_O} \right)\cdot \mathcal{P_N}$$|$$=$$|$$0$$|$$\quad$$|avec : | $$\mathcal{RP} = \mathcal{R_O}-\mathcal{P_O}$$|
|$$\left(\mathcal{R_D}\times t \right) \cdot \mathcal{P_N} + \mathcal{RP} \cdot \mathcal{P_N}$$|$$=$$|$$0$$|
|$$ t \times \left(\mathcal{R_D} \cdot \mathcal{P_N}\right) + \left(\mathcal{RP} \cdot \mathcal{P_N}\right)$$|$$=$$|$$0$$|

$$t=\frac{\mathcal{RP} \cdot \mathcal{P_N}}{\mathcal{R_D} \cdot \mathcal{P_N}}$$

On a quatre cas de figure :

* $$\mathcal{R_D} \cdot \mathcal{P_N} = 0$$ : Il n’y a aucune solution les vecteurs sont orthogonaux il n'y a donc pas d'intersection.
* $$\mathcal{R_D} \cdot \mathcal{P_N} \approx 0$$ : Il n’y a aucune solution, car $$t$$ est proche de l’infini.
* $$ t < 0 $$ : On ne le prend pas, car il se situe avant l'origine du rayon.
* $$ t > 0 $$ : On a notre solution

### Rayon (demi-droite) / Triangle

Pour ce faire nous allons utiliser la méthode de Möller-Trumbore : On a $$A$$, $$B$$ et $$C$$ les points du triangle, $$\mathcal{R_O}$$ l'origine du rayon, $$\mathcal{R_D}$$ sa direction.  
On commence par translater le triangle pour le ramener à l'origine (on soustrait $$C$$ à $$A$$ et $$B$$ mais aussi à $$\mathcal{R_O}$$ pour avoir un $$t$$ translaté également. Ensuite on aura besoin de différents déterminants de trois vecteurs.

**Rappel Déterminant** : $$\left\lvert A \quad B \quad C \right\rvert = -\left(A \times B \right) \cdot C = -\left(C \times B \right) \cdot A$$

<a href = "/assets/img/Memo/Moller_Trumbore.png" data-lightbox = "Memo" data-title = "Méthode de Möller-Trumbore"><img src = "/assets/img/Memo/Moller_Trumbore.png" alt = "Méthode de Möller-Trumbore" style = "max-width:75%;"/></a>

avec $$\begin{cases} E_1 & = & A-C\\ E_2 & = & B-C\\ T & = & \mathcal{R_O}-C\end{cases}$$, on a :

$$\begin{bmatrix} t\\ u\\ v\end{bmatrix}=\frac{1}{\left\lvert -D \quad E_1 \quad E_2 \right\rvert}*\begin{bmatrix} \left\lvert T \quad E_1 \quad E_2 \right\rvert\\ \left\lvert -D \quad T \quad E_2 \right\rvert\\ \left\lvert -D \quad E_1 \quad T \right\rvert\end{bmatrix}=\frac{1}{\left(D \times E_2 \right) \cdot E_1}*\begin{bmatrix} \left(T \times E_2 \right) \cdot E_1\\ \left(D \times E_2 \right) \cdot T\\ \left(T \times E_1 \right) \cdot D\end{bmatrix}$$

On a trois cas de figure :

* $$t < 0$$ : On ne le prend pas, car il se situe avant l'origine du rayon.
* $$t > 0$$ : On a notre solution mais
  * $$u < 0$$ ou $$v < 0$$ ou $$u + v > 1$$ : On est en dehors du triangle
  * $$u > 0$$ et $$v > 0$$ et $$u + v < 1$$ : On est dans le triangle et on a ses coordonnées de mapping.

## Transformation

Pour effectuer une transformation dans l’espace, il suffit de faire le produit matriciel du Point 3D $$\mathcal{P}$$ avec une matrice de transformation $$\mathcal{M}$$. On va pondérer le point 3D avec une quatrième coordonnée $$w$$. Cet ajout permettra d’effectuer une translation avec un produit matriciel. Pour retrouver le point 3D on divise chaque coordonnée par w (normalement au fil des transformations il doit rester à 1).

### Rappel Matrice Identité et enchainement

La matrice Identité est une matrice qui multiplié à un point donne le même point. $$\mathcal{M}_{Id}\begin{pmatrix}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}$$

La multiplication de différentes matrices de transformation permet d'obtenir une nouvelle matrice qui sera l’application de toute ses transformations successives. Evidemment, changer l’ordre des transformations peut changer le résultat.

### Translation

Pour déplacer un point $$\mathcal{P}$$ par le vecteur $$\vec{T}$$, la matrice de translation sera :	$$\mathcal{M}_\vec{T}\begin{pmatrix}1&0&0&x_T\\0&1&0&y_T\\0&0&1&z_T\\0&0&0&1\end{pmatrix}$$

### Homothétie

Pour multiplier la distance à l’origine d’un point  $$\mathcal{P}$$ par le facteur $$H$$, la matrice d’homothétie sera : $$\mathcal{M}_H\begin{pmatrix}x_H&0&0&0\\0&y_H&0&0\\0&0&z_H&0\\0&0&0&1\end{pmatrix}$$

### Rotation

Rotation d’un point P par l’angle θ centré sur l’origine, la matrice de rotation sera (autour d’un axe) :
$$\mathcal{M}_{R_x}\begin{pmatrix}1&0&0&0\\0&cos⁡θ&-sin⁡θ&0\\0&sin⁡θ&cos⁡θ&0\\0&0&0&1\end{pmatrix} \quad \quad \quad \mathcal{M}_{R_y}\begin{pmatrix}cos⁡θ&0&sin⁡θ&0\\0&1&0&0\\-sin⁡θ&0&cos⁡θ&0\\0&0&0&1\end{pmatrix} \quad \quad \quad \mathcal{M}_{R_z}\begin{pmatrix}cos⁡θ&-sin⁡θ&0&0\\sin⁡θ&cos⁡θ&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}$$

### Repère global VS Repère Local

Le repère global est le repère de l’espace, il est commun à tous les objets et ne change pas. Le repère local quant à lui est le repère de l’objet en lui-même. Lorsque l’on déplace l’objet, le repère se déplace lui aussi. Ainsi, un point qui se situe aux coordonnées $$(x,y,z)$$ du repère local aura toujours les mêmes coordonnées dans le repère local une fois déplacé.

#### Enchainement de Transformation

Si on veut effectuer une rotation et une translation, on peut multiplier les deux matrices de transformations. Mais l’ordre est important si on fait une rotation puis une translation ne donne pas le même résultat qu’une translation puis une rotation.

<form><center><table width="70%">
	<tr align="center">
		<td width="30%"><a href = "/assets/img/Memo/Geo3D_T_R.png" data-lightbox = "Memo" data-title = "Translation &rArr; Rotation"><img src = "/assets/img/Memo/Geo3D_T_R.png" alt = "Translation &rArr; Rotation" style = "max-width:100%;"/></a></td><td width="10%"></td><td width="30%"><a href = "/assets/img/Memo/Geo3D_R_T.png" data-lightbox = "Memo" data-title = "Rotation &rArr; Translation"><img src = "/assets/img/Memo/Geo3D_R_T.png" alt = "Rotation &rArr; Translation" style = "max-width:100%;"/></a></td>
	</tr>
	<tr align="center">
		<td>Translation &rArr; Rotation</td><td></td><td>Rotation &rArr; Translation</td>
	</tr>
</table></center></form>

Mais comment les enchainer et les lire ? Pour les enchaîner c’est simple, il suffit de multiplier les matrices, une multiplication de matrice carré d’ordre n donnera une matrice carré d’ordre n. Donc aucun problème. En réalité tout dépend de comment on réfléchit, Si on travaille dans le repère global, il faut lire les enchainements de transformation de droite à gauche, si on pense en repère local, il faut lire de gauche à droite.

<form><center><table width="70%">
	<tr align="center">
		<td width="30%"><a href = "/assets/img/Memo/Geo3D_Global.png" data-lightbox = "Memo" data-title = "Repère Global"><img src = "/assets/img/Memo/Geo3D_Global.png" alt = "Repère Global" style = "max-width:100%;"/></a></td><td width="10%"></td><td width="30%"><a href = "/assets/img/Memo/Geo3D_Local.png" data-lightbox = "Memo" data-title = "Repère Local"><img src = "/assets/img/Memo/Geo3D_Local.png" alt = "Repère Local" style = "max-width:100%;"/></a></td>
	</tr>
	<tr align="center">
		<td>Translation &rArr; Rotation</td><td></td><td>Rotation &rArr; Translation</td>
	</tr>
</table></center></form>
