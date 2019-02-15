---
layout: post
title: Mémo Espace Vectoriel
date: 2017-05-04
description: Mémo Espace Vectoriel
img: theme/Memo-Theme.png # Add image post (optional)
tags: [Mémos]
author: Thibaut Monseigne # Add name author (optional)
---

* TOC
{:toc}
{: .toc-post}

**Nota Bene :** 

|Vecteurs : |$$V$$ ou $$\vec{v}$$|
|Coordonnées dans l'espace : |$$(x,y,z)$$ ou $$(\vec{u},\vec{v},\vec{w})$$|
|Espace quelconque : |$$\mathcal{E}$$|
|Espace muni d'un repère orthonormé direct $$(\mathcal{O},\vec{i},\vec{j},\vec{k})$$ : &nbsp;&nbsp;&nbsp;|$$\mathcal{E_\bot}$$|

$$\times$$ correspond à multiplier sauf lorsque l'un a deux vecteurs, il s'agit du produit croisés, on utilisera $$*$$ à la place.

# Norme Euclidienne
## Définition
La norme euclidienne d'un vecteur $$\overrightarrow{AB}$$ est la distance qui sépare $$A$$ de $$B$$ c'est donc un nombre. En général, elle est notée $$\left\lVert \overrightarrow{AB} \right\rVert$$. Elle est égale à la racine de la somme des coordonnées au carrées ou au produit scalaire du vecteur avec lui-même.

$$\left\lVert \vec{v} \right\rVert = \sqrt{x^2+y^2+z^2} = \sqrt{\vec{v} \cdot \vec{v}}$$

## Propriétés

|:----|:----|:----|:----|:----|:----|:----|
|$$\left\lVert k\times\vec{v} \right\rVert $$|$$=$$|$$ \lvert k \rvert\times\left\lVert \vec{v} \right\rVert $$|$$ \quad \quad \quad $$|$$ \left\lVert -\vec{v} \right\rVert $$|$$=$$|$$ \left\lVert \vec{v} \right\rVert$$|
|$${\left\lVert \vec{v} \right\rVert}_1 $$|$$=$$|$$ \lvert x \rvert + \lvert y \rvert + \lvert z \rvert $$|$$ \quad \quad \quad $$|$$ {\left\lVert \vec{v} \right\rVert}_p $$|$$=$$|$$ {\left( x^p + y^p + z^p \right)}^p $$|$$ \quad \quad \quad $$|$$ {\left\lVert \vec{v} \right\rVert}_\infty $$|$$=$$|$$ \max{\left( x, y, z \right)}$$|

# Produit Scalaire
## Définition
Dans l’espace orthonormé direct $$\mathcal{E_\bot}$$. Soient $$\vec{u}$$ et $$\vec{v}$$ deux vecteurs de l'espace. Alors le produit scalaire de  $$\vec{u}$$ et $$\vec{v}$$ noté  $$\vec{u} \cdot \vec{v}$$ est le nombre réel défini par :


|:----|:----|:----|:----|:----|:----|:----|
|$$\vec{u} \cdot \vec{v} $$|$$=$$|$$ \langle \vec{u}, \vec{v} \rangle $$|$$=$$|$$ \left\lVert \vec{u} \right\rVert \times \left\lVert \vec{v} \right\rVert \times \cos{\left( \widehat{\vec{u}, \vec{v}} \right)} $$|
||||$$=$$|$$ \frac{1}{2} \times \left( {\left\lVert \vec{u} \right\rVert}^2 + {\left\lVert \vec{v} \right\rVert}^2 + {\left\lVert \vec{u}-\vec{v} \right\rVert}^2 \right) $$|
||||$$=$$|$$ u_1v_1 + u_2v_2 + u_3v_3 $$|

## Propriétés

|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|$$ \vec{u} \cdot \vec{v} $$|$$=$$|$$ \vec{v} \cdot \vec{u} $$|$$ \quad \quad \quad $$|$$ \vec{u} \cdot \vec{u} $$|$$=$$|$$ \vec{u}^2 = {\left\lVert \vec{u} \right\rVert}^2 $$|$$ \quad \quad \quad $$|$$ \vec{u} \cdot \vec{v} $$|$$=$$|$$ 0 \iff \vec{u} \bot \vec{v} $$|
|$$ \left( \lambda\times\vec{u} \right) \cdot \vec{v} $$|$$=$$|$$ \lambda\times\left(\vec{u} \cdot \vec{v}\right) $$|$$ \quad \quad \quad $$|$$ \cos{\left( \widehat{\vec{u}, \vec{v}} \right)} $$|$$=$$|$$ \frac{\vec{u} \cdot \vec{v}}{\left\lVert \vec{u} \right\rVert \times \left\lVert \vec{v} \right\rVert} $$|$$ \quad \quad \quad $$|$$ \left( \vec{u} + \vec{v} \right) \cdot \vec{w} $$|$$=$$|$$ \vec{u} \cdot \vec{w} + \vec{v} \cdot \vec{w}$$|
|$$ {\left( \vec{u} + \vec{v} \right)}^2 $$|$$=$$|$$ \vec{u}^2 + 2 \times \vec{u} \cdot \vec{v} + \vec{v}^2 $$|$$ \quad \quad \quad $$|$$ {\left( \vec{u} - \vec{v} \right)}^2 $$|$$=$$|$$ \vec{u}^2 - 2 \times \vec{u} \cdot \vec{v} + \vec{v}^2 $$|$$ \quad \quad \quad $$|$$ {\left( \vec{u} + \vec{v} \right)}{\left( \vec{u} - \vec{v} \right)} $$|$$=$$|$$ \vec{u}^2 - \vec{v}^2 $$|

# Produit Vectoriel 3D ou Produit croisé 3D (Cross Product)
## Définition
D'un point de vue géométrique, le produit vectoriel de deux vecteurs $$\vec{u}$$ et $$\vec{v}$$ non colinéaires se définit comme l'unique vecteur $$\vec{w}$$ tel que :
- Le vecteur $$\vec{w}$$ est orthogonal aux deux vecteurs donnés.
- La base $$(\vec{u},\vec{v},\vec{w})$$ est de sens direct.
- $$\left\lVert \vec{w} \right\rVert = \left\lVert \vec{u} \right\rVert \times \left\lVert \vec{v} \right\rVert \times \left\lvert \sin{\left( \widehat{\vec{u}, \vec{v}} \right)} \right\rvert $$.

$$ \vec{u} \times \vec{v} = \vec{u} \wedge \vec{v} = \begin{bmatrix} u_2v_3 - u_3v_2 \\ u_3v_1 - u_1v_3 \\ u_1v_2 - u_2v_1 \end{bmatrix} $$

## Propriétés

|:----|:----|:----|:----|:----|
|$$\vec{u} \times \vec{v} $$|$$=$$|$$ - \vec{v} \times \vec{u}$$|
|$$\lambda * \left( \vec{u} \times \vec{v} \right) $$|$$=$$|$$ \lambda * \vec{u} \times \vec{v} $$|$$=$$|$$ \vec{u} \times \lambda * \vec{v}$$|
|$$\vec{u} \times \left( \vec{v} + \vec{w} \right) $$|$$=$$|$$ \vec{u} \times \vec{v} + \vec{u} \times \vec{w}$$|
