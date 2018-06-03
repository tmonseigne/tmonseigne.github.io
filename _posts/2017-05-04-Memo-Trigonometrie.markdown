---
layout: post
title: Mémo Trigonométrie
date: 2017-05-04
description: Mémo Trigonométrie
img: theme/Memo-Theme.jpg # Add image post (optional)
tags: [Mémos]
author: Thibaut Monseigne # Add name author (optional)
---

* TOC
{:toc}
{: .toc-post}

# Définition
<a href = "/assets/img/Memo/triangle.png" data-lightbox = "Memo" data-title = "Triangle"><img src = "/assets/img/Memo/triangle.png" alt = "Triangle" style = "max-width:25%;"/></a>
Une définition de la trigonométrie se base sur les triangles rectangles. 
Dans ce cas, on a :

$$\sin\alpha = \frac{a}{c} \quad\quad\quad \cos\alpha = \frac{b}{c} \quad\quad\quad \tan\alpha = \frac{a}{b}$$

|Pythagore ∶ &nbsp;&nbsp;&nbsp;|$$a^2+b^2 = c^2$$|
|Al-Kashi ∶ &nbsp;&nbsp;&nbsp;|$$a = \sqrt{b^2+c^2-2\times b\times c\times \cos\alpha}$$|
|Thalès ∶ &nbsp;&nbsp;&nbsp;|$$\frac{AD}{AB} = \frac{AE}{AC} = \frac{DE}{BC}$$|

# Identités Remarquables
Quel que soit l’angle $$\alpha$$, on a (d’après le théorème de Pythagore) : $$\cos^2⁡\alpha + \sin^2\alpha = 1$$

## Formules d’addition et de différence des arcs :

|:---|:---|:---|:---|:---|:---|:---|
|$$\sin⁡(\alpha -\beta ) $$|$$=$$|$$ \sin⁡\alpha \times \cos⁡\beta - \cos⁡\alpha \times \sin⁡\beta $$|$$ \quad \quad \quad $$|$$ \sin⁡(\alpha + \beta ) $$|$$=$$|$$ \sin⁡\alpha \times \cos⁡\beta + \cos⁡\alpha \times \sin⁡\beta\quad$$|
|$$\cos(\alpha -\beta ) $$|$$=$$|$$ \cos\alpha \times \cos⁡\beta + \sin\alpha \times \sin⁡\beta $$|$$ \quad \quad \quad $$|$$ \cos(\alpha + \beta ) $$|$$=$$|$$ \cos\alpha \times \cos⁡\beta - \sin\alpha \times \sin⁡\beta\quad$$|
|$$\tan(\alpha -\beta ) $$|$$=$$|$$ \left(\tan\alpha - \tan\beta\right)/\left(1 + \tan\alpha \times \tan\beta\right) $$|$$ \quad \quad \quad $$|$$ \tan(\alpha + \beta ) $$|$$=$$|$$ \left(\tan\alpha - \tan\beta\right)/\left(1 + \tan\alpha \times \tan\beta\right)\quad$$|

## Formules de duplication des arcs :

|:---|:---|:---|:---|:---|:---|:---|
|$$\cos(2\alpha) $$|$$=$$|$$ \begin{cases} \cos^2⁡\alpha - \sin^2\alpha \\ 2\times \cos^2⁡\alpha - 1 \\ 1 - 2 \times \sin^2\alpha \end{cases} $$|$$ \quad \quad \quad $$|$$ \cos(3\alpha) $$|$$=$$|$$ 4\times \cos^3⁡\alpha-3 \times \cos\alpha$$|
|$$\sin(2\alpha) $$|$$=$$|$$ 2\times \sin \alpha\times \cos\alpha $$|$$ \quad \quad \quad $$|$$ \sin(3\alpha) $$|$$=$$|$$ 3 \times \sin \alpha - 4 \times \sin^3⁡\alpha$$|
|$$\tan⁡(2\alpha) $$|$$=$$|$$ \left(2 \times \tan⁡\alpha\right)/\left(1-\tan^2⁡\alpha\right) $$|$$ \quad \quad \quad $$|$$ \tan⁡(3\alpha) $$|$$=$$|$$ \left(3 \times \tan⁡\alpha - \tan^3⁡\alpha\right)/\left(1 - 3 \times \tan^2⁡\alpha\right)\quad\quad\quad$$|

## Formules d’addition et de différence de deux sinus et de deux cosinus converties en produit :

|:---|:---|:---|:---|:---|:---|:---|
|$$ \cos(\alpha + \beta ) - \cos(\alpha - \beta ) $$|$$=$$|$$ - 2 \times \sin\alpha \times \sin\beta $$|$$ \quad \quad \quad $$|$$ \cos(\alpha + \beta ) + \cos(\alpha - \beta ) $$|$$=$$|$$ 2 \times \cos\alpha \times \cos⁡\beta\quad\quad\quad$$|
|$$ \sin(\alpha + \beta ) - \sin(\alpha - \beta ) $$|$$=$$|$$ 2 \times \cos\alpha \times \sin\beta $$|$$ \quad \quad \quad $$|$$ \sin(\alpha + \beta ) + \sin(\alpha - \beta ) $$|$$=$$|$$ 2 \times \sin\alpha \times \cos\beta\quad\quad\quad$$|

## Identités trigonométrique :

$$\tan\alpha = \frac{\sin\alpha}{\cos\alpha} \quad\quad\quad \cos^2⁡\alpha + \sin^2\alpha = 1 \quad\quad\quad \tan^2⁡\alpha + 1 = \frac{1}{\cos^2\alpha}$$

## Relation entre les fonctions trigonométriques :

$$\cos\alpha = \sqrt{1-\sin^2\alpha} = \frac{1}{\sqrt{1+\tan^2\alpha}}\\
\sin\alpha = \sqrt{1-\cos^2\alpha} = \frac{\tan\alpha}{\sqrt{1+\tan^2\alpha}}\\
\tan\alpha = \frac{\sqrt{1-\cos^2\alpha}}{\cos\alpha} = \frac{\sin\alpha}{\sqrt{1-\sin^2\alpha}}\\$$

# Cercle Trigonométrique
<a href = "/assets/img/Memo/Cercle_Trigo.png" data-lightbox = "Memo" data-title = "Cercle Trigonométrique"><img src = "/assets/img/Memo/Cercle_Trigo.png" alt = "Cercle Trigonométrique" style = "max-width:50%;"/></a>


<form><table style="width:100%; border-collapse:collapse;" border="1">
	<tr align="center">
		<th width="7%" align="left">Radian</th>
		<td>$$0$$</td> <td>$$\frac{\pi}{6}$$</td> <td>$$\frac{\pi}{4}$$</td> <td>$$\frac{\pi}{3}$$</td> <td>$$\frac{\pi}{2}$$</td> <td>$$\frac{2\pi}{3}$$</td> <td>$$\frac{3\pi}{4}$$</td> <td>$$\frac{5\pi}{6}$$</td> <td>$$\pi$$</td> <td>$$\frac{7\pi}{6}$$</td> <td>$$\frac{5\pi}{4}$$</td> <td>$$\frac{4\pi}{3}$$</td> <td>$$\frac{3\pi}{2}$$</td> <td>$$\frac{5\pi}{3}$$</td> <td>$$\frac{7\pi}{4}$$</td> <td>$$\frac{11\pi}{6}$$</td> <td>$$2\pi$$</td>
	</tr>
	<tr align="center" bgcolor="#D3D3D3">
		<th width="7%" align="left">Degré</th>
		<td>$$\ 0\ $$</td> <td>$$30$$</td> <td>$$45$$</td> <td>$$60$$</td> <td>$$90$$</td> <td>$$120$$</td> <td>$$135$$</td> <td>$$150$$</td> <td>$$180$$</td> <td>$$210$$</td> <td>$$225$$</td> <td>$$240$$</td> <td>$$270$$</td> <td>$$300$$</td> <td>$$315$$</td> <td>$$330$$</td> <td>$$360$$</td>
	</tr>
	<tr align="center" bgcolor="#FFD3FF">
		<th width="7%" align="left">$$\sin$$</th>
		<td>$$0$$</td> <td>$$\frac{1}{2}$$</td> <td>$$\frac{\sqrt{2}}{2}$$</td> <td>$$\frac{\sqrt{3}}{2}$$</td> <td>$$1$$</td> <td>$$\frac{\sqrt{3}}{2}$$</td> <td>$$\frac{\sqrt{2}}{2}$$</td> <td>$$\frac{1}{2}$$</td> <td>$$0$$</td> <td>$$-\frac{1}{2}$$</td> <td>$$-\frac{\sqrt{2}}{2}$$</td> <td>$$-\frac{\sqrt{3}}{2}$$</td> <td>$$-1$$</td> <td>$$-\frac{\sqrt{3}}{2}$$</td> <td>$$-\frac{\sqrt{2}}{2}$$</td> <td>$$-\frac{1}{2}$$</td> <td>$$0$$</td>
	</tr>
	<tr align="center" bgcolor="#D3FFFF">
		<th width="7%" align="left">$$\cos$$</th>
		<td>$$1$$</td> <td>$$\frac{\sqrt{3}}{2}$$</td> <td>$$\frac{\sqrt{2}}{2}$$</td> <td>$$\frac{1}{2}$$</td> <td>$$0$$</td> <td>$$-\frac{1}{2}$$</td> <td>$$-\frac{\sqrt{2}}{2}$$</td> <td>$$-\frac{\sqrt{3}}{2}$$</td> <td>$$-1$$</td> <td>$$-\frac{\sqrt{3}}{2}$$</td> <td>$$-\frac{\sqrt{2}}{2}$$</td> <td>$$-\frac{1}{2}$$</td> <td>$$0$$</td> <td>$$\frac{1}{2}$$</td> <td>$$\frac{\sqrt{2}}{2}$$</td> <td>$$\frac{\sqrt{3}}{2}$$</td> <td>$$1$$</td>
	</tr>
	<tr align="center" bgcolor="#FFFFD3">
		<th width="7%" align="left">$$\tan$$</th>
		<td>$$0$$</td> <td>$$\frac{1}{\sqrt{3}}$$</td> <td>$$1$$</td> <td>$$\sqrt{3}$$</td> <td>$$-$$</td> <td>$$-\sqrt{3}$$</td> <td>$$-1$$</td> <td>$$-\frac{1}{\sqrt{3}}$$</td> <td>$$0$$</td> <td>$$\frac{1}{\sqrt{3}}$$</td> <td>$$1$$</td> <td>$$\sqrt{3}$$</td> <td>$$-$$</td> <td>$$-\sqrt{3}$$</td> <td>$$-1$$</td> <td>$$-\frac{1}{\sqrt{3}}$$</td> <td>$$0$$</td>
	</tr>
</table></form>

## Propriétés liées au cercle Trigonométrique

|Propriété||Sinus||||Cosinus||||Tangente|||
|:--------|:----|:------|:-------|:---|:---|:---|:---|:---|:---|:---|
|Réflexion d'axe $$a=0 $$|$$ \quad $$|$$ \sin(-\alpha)$$|$$=$$|$$-\sin\alpha  $$|$$ \quad $$|$$  \cos⁡(-\alpha)$$|$$=$$|$$\cos⁡\alpha $$|$$ \quad $$|$$ \tan(-\alpha)$$|$$=$$|$$-\tan\alpha\quad\quad$$|
|Réflexion d'axe $$a=\pi/4 $$|$$ \quad $$|$$ \sin(\pi/2-\alpha)$$|$$=$$|$$\cos⁡\alpha $$|$$ \quad $$|$$ \cos⁡(\pi/2-\alpha)$$|$$=$$|$$\sin\alpha $$|$$ \quad $$|$$ \tan(\pi/2-\alpha)$$|$$=$$|$$\cot⁡\alpha\quad\quad$$|
|Réflexion d'axe $$a=\pi/2 $$|$$ \quad $$|$$ \sin(\pi-\alpha)$$|$$=$$|$$\sin\alpha $$|$$ \quad $$|$$ \cos⁡(\pi-\alpha)$$|$$=$$|$$-\cos⁡\alpha $$|$$ \quad $$|$$ \tan(\pi-\alpha)$$|$$=$$|$$-\tan\alpha\quad\quad$$|
|Décalage de $$ \pi/2 $$|$$ \quad $$|$$ \sin(\alpha+\pi/2)$$|$$=$$|$$\cos⁡\alpha $$|$$ \quad $$|$$ \cos⁡(\alpha+\pi/2)$$|$$=$$|$$-\sin\alpha $$|$$ \quad $$|$$ \tan(\alpha+\pi/2)$$|$$=$$|$$-\cot⁡\alpha\quad\quad$$|
|Décalage de $$\pi $$|$$ \quad $$|$$ \sin(\alpha+\pi)$$|$$=$$|$$-\sin\alpha $$|$$ \quad $$|$$ \cos⁡(\alpha+\pi)$$|$$=$$|$$-\cos⁡\alpha $$|$$ \quad $$|$$ \tan(\alpha+\pi)$$|$$=$$|$$\tan\alpha\quad\quad$$|
|Décalage de $$2\pi $$|$$ \quad $$|$$ \sin(\alpha+2\pi)$$|$$=$$|$$\sin\alpha $$|$$ \quad $$|$$ \cos⁡(\alpha+2\pi)$$|$$=$$|$$\cos⁡\alpha $$|$$ \quad $$|$$ \tan(\alpha+2\pi)$$|$$=$$|$$\tan\alpha\quad\quad$$|