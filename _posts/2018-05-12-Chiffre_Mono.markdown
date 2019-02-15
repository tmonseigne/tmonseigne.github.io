---
layout: post
title: Chiffrement Monoalphabétique
date: 2018-05-12
description: Explication du Chiffrement Monoalphabétique suivi d'un petit code JavaScript pour chiffrer/déchiffrer
img: theme/Chiffrement-Theme.png # Add image post (optional)
tags: [Chiffrement, Chiffrement Monoalphabétique, Explication, Exemple]
author: Thibaut Monseigne # Add name author (optional)
---

* TOC
{:toc}
{: .toc-post}

Le chiffrement monoalphabétique ou chiffrement par substitution est une des plus anciennes méthodes de chiffrement. Elle consiste à remplacer chaque lettre d’un texte par un symbole donné (ce symbole peut être une autre lettre de l’alphabet). Sachant que deux lettres distinctes doivent être chiffrées en deux signes distincts pour permettre un déchiffrement du message sans ambiguïté.

# Alphabet désordonné
L'alphabet désordonné est la manière la plus classique de chiffrer des messages, il consiste à remplacer une lettre par une autre. Cela donne par exemple la grille de chiffrement ci-dessous :

<form><table style="width:100%" border="1">
	<tr align="center">
		<th width="15%" align="left">Original</th>
		<td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
	</tr>
	<tr align="center" bgcolor="#F0F0F0">
		<th width="15%" align="left">Chiffrement</th>
		<td>P</td><td>O</td><td>S</td><td>D</td><td>F</td><td>U</td><td>G</td><td>N</td><td>Z</td><td>Q</td><td>V</td><td>E</td><td>I</td><td>Y</td><td>H</td><td>W</td><td>A</td><td>X</td><td>C</td><td>B</td><td>R</td><td>J</td><td>K</td><td>L</td><td>M</td><td>T</td>
	</tr>
</table></form>

## Code de César
Le chiffre de César (ou code de César ou alphabet décalé) est un type d'alphabet désordonné qui consiste à décaler les lettres de l'alphabet de quelques crans vers la droite ou la gauche. Par exemple, Jules César (qui a donné son nom à ce code) décalait les lettres de 3 rangs vers la gauche : 

<form><table style="width:100%" border="1">
	<tr align="center">
		<th width="15%" align="left">Original</th>
		<td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
	</tr>
	<tr align="center" bgcolor="#F0F0F0">
		<th width="15%" align="left">Chiffrement</th>
		<td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td><td>A</td><td>B</td><td>C</td>
	</tr>
</table></form>

L'avantage de ce chiffrement est que la clef de chiffrement est un nombre et qu'il est possible (plus simple) de déchiffrer le message sans avoir de grille de déchiffrement à côté.  
L'inconvénient majeur est qu'il n'existe que 25 permutations possibles. Il suffit donc d'essayer tous les décalages pour trouver le bon. Cette technique s'appelle la recherche exhaustive des clefs.

## Alphabet réversible
Les alphabets réversibles sont des alphabets désordonnés particuliers qui comme leur nom l'indique permettent de retrouver le message initial si on le chiffre deux fois de suite. Les plus connus sont les chiffres `Atbash`, `Albam`, `Atbah` utilisés par les anciens Hébreux.  
Adapté à notre alphabet, le chiffre `Atbash` consiste simplement à inverser l'ordre des lettres. Le mot "Atbash" est composé à partir des lettres aleph, tau, beth et shin, les deux premières et les deux dernières de l'alphabet hébreu.  
Le chiffre `Albam` décale les lettres de l'alphabet de 13 positions. Il est réapparu en 1984 sous le nom de `ROT13` dans un programme permettant de lire les "News" de USENET.  
Les grilles de chiffrement, pour ces trois alphabets réversibles, donne ceci :

<form><table style="width:100%" border="1">
	<tr align="center">
		<th width="15%" align="left">Original</th>
		<td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
	</tr>
	<tr align="center" bgcolor="#F0F0F0">
		<th width="15%" align="left">Atbash</th>
		<td>Z</td><td>Y</td><td>X</td><td>W</td><td>V</td><td>U</td><td>T</td><td>S</td><td>R</td><td>Q</td><td>P</td><td>O</td><td>N</td><td>M</td><td>L</td><td>K</td><td>J</td><td>I</td><td>H</td><td>G</td><td>F</td><td>E</td><td>D</td><td>C</td><td>B</td><td>A</td>
	</tr>
	<tr align="center" bgcolor="#F0F0F0">
		<th width="15%" align="left">Albam</th>
		<td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td>
	</tr>
	<tr align="center" bgcolor="#F0F0F0">
		<th width="15%" align="left">Atbah</th>
		<td>I</td><td>H</td><td>G</td><td>F</td><td>N</td><td>D</td><td>C</td><td>B</td><td>A</td><td>R</td><td>Q</td><td>P</td><td>O</td><td>E</td><td>M</td><td>L</td><td>K</td><td>J</td><td>Z</td><td>Y</td><td>X</td><td>W</td><td>V</td><td>U</td><td>T</td><td>S</td>
	</tr>
</table></form>

## Mot-Clef
### Grille Horizontale
Au lieu de retenir l'ensemble de la grille (ce qui est relativement difficile à moins d'avoir une mémoire remarquable), il est possible de la construire à partir d'un mot-clef. Les lettres le composant seront mises dans la deuxième ligne de la grille dans l'ordre d'apparition. Évidemment, il faut supprimer les doublons, les signes de ponctuation, les espaces et accents). On ajoutera ensuite les lettres n'apparaissant pas dans le mot-clef par ordre alphabétique.  
Voici un exemple avec `Mot-Clef !`

<form><table style="width:100%" border="1">
	<tr align="center">
		<th width="15%" align="left">Original</th>
		<td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
	</tr>
	<tr align="center" bgcolor="#F0F0F0">
		<th width="15%" align="left">Chiffrement</th>
		<td>M</td><td>O</td><td>T</td><td>C</td><td>L</td><td>E</td><td>F</td><td>A</td><td>B</td><td>D</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>N</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
	</tr>
</table></form>

On remarque que lorsque les différentes lettres du mot-clef sont apparues la fin de la grille correspond à l’alphabet standard (à partir de la lettre `U` dans notre cas, `T` étant la plus éloignée). Évidemment, comme précisés précédemment, les signes de ponctuations et espaces n'ont pas été pris en compte.

### Grille Verticale
Afin de pallier au problème précédent, une méthode de construction de grille consiste à écrire le reste de l'alphabet dans un carré de largeur égale au nombre de lettres du mot clef et de lire les lettres colonne par colonne.
Exemple avec `Mot-Clef !` et `Salut` : 


<form><center><table style="width:30%">
	<tr>
		<td style="width:100%">
			<table  border="1">
				<tr align="center" bgcolor="#F0F0F0">
					<td>M</td><td>O</td><td>T</td><td>C</td><td>L</td><td>E</td><td>F</td>
				</tr>
				<tr align="center" bgcolor="#F0F0F0">
					<td>A</td><td>B</td><td>D</td><td>G</td><td>H</td><td>I</td><td>J</td>
				</tr>
				<tr align="center" bgcolor="#F0F0F0">
					<td>K</td><td>N</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>U</td>
				</tr>
				<tr align="center" bgcolor="#F0F0F0">
					<td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td><td> </td><td> </td>
				</tr>
			</table>
		</td>
		<td style="width:100%"> </td>
		<td style="width:100%">
			<table  border="1">
				<tr align="center" bgcolor="#F0F0F0">
					<td>S</td><td>A</td><td>L</td><td>U</td><td>T</td>
				</tr>
				<tr align="center" bgcolor="#F0F0F0">
					<td>B</td><td>C</td><td>D</td><td>E</td><td>F</td>
				</tr>
				<tr align="center" bgcolor="#F0F0F0">
					<td>G</td><td>H</td><td>I</td><td>J</td><td>K</td>
				</tr>
				<tr align="center" bgcolor="#F0F0F0">
					<td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td>
				</tr>
				<tr align="center" bgcolor="#F0F0F0">
					<td>R</td><td>V</td><td>W</td><td>X</td><td>Y</td>
				</tr>
				<tr align="center" bgcolor="#F0F0F0">
					<td>Z</td><td> </td><td> </td><td> </td><td> </td>
				</tr>
			</table>
		</td>
	</tr>
</table></center></form>

<form><table style="width:100%" border="1">
	<tr align="center">
		<th width="15%" align="left">Original</th>
		<td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
	</tr>
	<tr align="center" bgcolor="#F0F0F0">
		<th width="15%" align="left">Mot-Clef !</th>
		<td>M</td><td>A</td><td>K</td><td>V</td><td>O</td><td>B</td><td>N</td><td>W</td><td>T</td><td>D</td><td>P</td><td>X</td><td>C</td><td>G</td><td>Q</td><td>Y</td><td>L</td><td>H</td><td>R</td><td>Z</td><td>E</td><td>I</td><td>S</td><td>F</td><td>J</td><td>U</td>
	</tr>
	<tr align="center" bgcolor="#F0F0F0">
		<th width="15%" align="left">Salut</th>
		<td>S</td><td>B</td><td>G</td><td>M</td><td>R</td><td>Z</td><td>A</td><td>C</td><td>H</td><td>N</td><td>V</td><td>L</td><td>D</td><td>I</td><td>O</td><td>W</td><td>U</td><td>E</td><td>J</td><td>P</td><td>X</td><td>T</td><td>F</td><td>K</td><td>Q</td><td>Y</td>
	</tr>
</table></form>

## Décryptage
### Recherche exhaustive des clefs
Comme nous l'avons indiqué pour le chiffre de César, une recherche exhaustive des clefs est possible, car il n'y a que 25 permutations possibles. Dans le cas d'un alphabet désordonné plus complexe, nous avons $$26!-1$$ ($$\approx 4.033•10^{26}$$) possibilités.....

### Analyse des Fréquences d'apparition
Avec quelques astuces, nous pouvons réduire ce chiffre. La première étape consiste à connaître la langue utilisée et la fréquence d'apparition des lettres. Si nous prenons pour exemple les résultats du laboratoire CLLE-ERSS qui a recensé tous les mots des pages françaises de Wikipedia en 2008<sup>[1](https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d%27apparition_des_lettres_en_fran%C3%A7ais#Fr%C3%A9quence_des_caract%C3%A8res_dans_le_corpus_de_Wikip%C3%A9dia_en_fran%C3%A7ais){:target="_blank"}, [2](http://redac.univ-tlse2.fr/corpus/wikipedia.html){:target="_blank"}</sup> nous avons le résultat suivant exprimé en pourcentage (j'ai regroupé les caractères accentués vers leur lettre non accentuée) : 

<form><table style="width:100%" border="1">
	<tr align="center">
		<td>E</td><td>A</td><td>I</td><td>S</td><td>N</td><td>R</td><td>T</td><td>O</td><td>L</td><td>U</td><td>D</td><td>C</td><td>M</td><td>P</td><td>G</td><td>B</td><td>V</td><td>H</td><td>F</td><td>Q</td><td>Y</td><td>X</td><td>J</td><td>K</td><td>W</td><td>Z</td>
	</tr>
	<tr align="center" bgcolor="#F0F0F0">
		<td>14.44</td><td>7.46</td><td>6.64</td><td>6.51</td><td>6.39</td><td>6.07</td><td>5.92</td><td>5.07</td><td>4.96</td><td>4.54</td><td>3.67</td><td>3.24</td><td>2.62</td><td>2.49</td><td>1.23</td><td>1.14</td><td>1.11</td><td>1.11</td><td>1.11</td><td>0.65</td><td>0.46</td><td>0.38</td><td>0.34</td><td>0.29</td><td>0.17</td><td>0.15</td>
	</tr>
</table></form>

On effectue la même opération avec le message chiffré et l'on remplace chaque lettre par sa correspondante. Le résultat final dépend évidemment des fréquences de référence, ainsi, un texte utilisant le vouvoiement de façon significative augmente la probabilité de la lettre Z par exemple. Le second paramètre évident est la taille du texte à déchiffrer, tirer des fréquences d'apparition de quelques mots est trop peu juste. Ces deux paramètres essentiels rendront le décryptage parfois approximatif, mais ce premier décryptage permettra parfois d'avoir une grille proche de la grille réelle.

### Attaque par mot probable
L'attaque par mot probable consiste à utiliser un mot dont on est sûr qu'il apparait dans le texte. Si ce mot est `oui`, nous ne pouvons tirer de règle de déduction de viable si ce n'est que trois lettres consécutives doivent être différentes. Mais si le mot est `concombre`, on remarque que : 
- La 1<sup>re</sup> et la 4<sup>e</sup> lettre sont identiques.
- La 2<sup>e</sup> et la 5<sup>e</sup> lettre sont identiques, mais différentes des lettres 1 et 4.
- Les autres lettres sont toutes différentes.
- L'ensemble de ses règles concernent une séquence de neuf lettres consécutives.

Une fois que l'on a trouvé toutes les correspondances possibles, on peut utiliser une statistique [khi carré](https://fr.wikipedia.org/wiki/Loi_du_%CF%87%C2%B2) pour déterminer laquelle est la plus probable.  

La grille de chiffrement possède une base faible, mais d'autres mots peuvent, potentiellement, être devinés et, un peu comme au sudoku, par élimination et déduction, la grille de chiffrement se constitue. En cas de blocage, le retour à une des méthodes précédentes avec le message en partie clarifié est possible.

# Le système monôme-binôme
Le système monôme-binôme consiste à remplacer chaque lettre par un ou deux chiffres à l'aide d'une grille de chiffrement de 3 lignes et 10 colonnes. Deux chiffres forment la clef de ce chiffre dont voici un exemple avec les chiffres 4 et 7.

<form><center><table style="width:50%" border="1">
	<tr align="center" bgcolor="#F0F0F0"><td> </td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr>
	<tr align="center"><td bgcolor="#F0F0F0"> </td><td>A</td><td>B</td><td>C</td><td>D</td><td bgcolor="#0F0F0F"></td><td>E</td><td>F</td><td bgcolor="#0F0F0F"></td><td>G</td><td>H</td></tr>
	<tr align="center"><td bgcolor="#F0F0F0">4</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td></tr>
	<tr align="center"><td bgcolor="#F0F0F0">7</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td><td></td><td>.</td></tr>
</table></center></form>

Le malgré le fait que certaines lettres ne sont représentées que par un seul chiffre, il est assez facile de les découper sachant que s'ils commencent par 4 ou 7 il y a deux chiffres sinon un seul.  
**Nota Bene :** Évidemment, il est possible de remplir la grille avec un alphabet désordonné.

## Décryptage
Le décryptage de ce code est plus complexe, car il faut d'abord découper les chiffres par monôme ou binôme. Sans connaître les deux chiffres clefs, le meilleur moyen consiste à calculer la fréquence d'apparition des chiffres, les deux plus (moins) fréquents sont généralement les deux chiffres des lignes (colonnes).  
Le calcul de fréquences des bigrammes permet aussi de déterminer les chiffres des colonnes.  
Lorsque les chiffres clefs sont trouvés, il faut tester en reconstituant les séparations entre les chiffres, en calculant les fréquences de l'alphabet trouvé et en vérifiant que les fréquences obtenues sont plausibles. En cas d'échec, il faut changer les chiffres clefs.

## Cas Particulier : Carré de Polybe 
Ce chiffrement vient de l'historien grec [Polybe](https://fr.wikipedia.org/wiki/Polybe). IL se base sur un carré de 25 cases (en français, la lettre W sera remplacée par la lettre V, en anglais, I deviendra J)

<form><center><table style="width:30%" border="1">
	<tr align="center" bgcolor="#F0F0F0"><td> </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr>
	<tr align="center"><td bgcolor="#F0F0F0">1</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr>
	<tr align="center"><td bgcolor="#F0F0F0">2</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td></tr>
	<tr align="center"><td bgcolor="#F0F0F0">3</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td></tr>
	<tr align="center"><td bgcolor="#F0F0F0">4</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td></tr>
	<tr align="center"><td bgcolor="#F0F0F0">5</td><td>U</td><td>V</td><td>X</td><td>Y</td><td>Z</td></tr>
</table></center></form>

**Nota Bene :** Évidemment, il est possible de remplir la grille avec un alphabet désordonné.

# Chiffrement par substitution (symbole)
Contrairement à l'alphabet désordonné, l'utilisation de symbole donne une complexité différente au message. Il faut d’abord isoler chacun des symboles qui contrairement aux lettres peuvent avoir des tailles et un nombre d’éléments fluctuant. Il est même possible d'envisager qu'une lettre puisse être chiffrée par plusieurs symboles différents pris aléatoirement (en gardant à l'esprit qu'un symbole ne pourra désigner qu'une et une seule lettre).

## Le Parc à cochons (Pig Pen)
Le parc à cochon est un ancien système de chiffrement aujourd'hui largement connu. Son nom vient de la forme de la table de rappel du code ci-dessous. 

<a href="/assets/img/chiffre/PigPen1.png" data-lightbox="Chiffrement MonoAlphabétique" data-title="Pig Pen"><img src="/assets/img/chiffre/PigPen1.png" alt="Pig Pen" style="max-width:25%;"/></a>


<form><table style="width:100%" border="1">
	<tr align="center">
		<th width="15%" align="left">Original</th>
		<td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
	</tr>
	<tr align="center" bgcolor="#F0F0F0" style="font-family:PigPen">
		<th width="15%" align="left" style="font-family: 'Montserrat', sans-serif;">Pig Pen</th>
		<td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
	</tr>
</table></form>

La grille ci-dessus utilise cette [Police](https://www.dafont.com/pigpen-cipher.font){:target="_blank"} venant du site [www.dafont.com](http://www.dafont.com/){:target="_blank"}.

## Le cryptogramme de La Buse
Olivier Levasseur dit "la Buse" (ou "la Bouche") est un pirate du XVIIIe siècle qui, avant d'être pendu, lança le message chiffré ci-dessous dans la foule en criant: "mes trésors à qui saura comprendre!". À l’heure actuelle, un chiffrement style parc à cochons est utilisé, mais le texte reste assez obscur. Les recherches se focalisent sur l'ile de la Réunion par Emmanuel Mezino qui a publié un livre "*Mon Trésor à qui saura le prendre : le secret du cryptogramme du pirate Olivier Levasseur dit La Buse, enfin dévoilé*" en 2014.

<a href="/assets/img/chiffre/LaBuse1.png" data-lightbox="Chiffrement MonoAlphabétique" data-title="Cryptogramme du Forban"><img src="/assets/img/chiffre/LaBuse1.png" alt="Cryptogramme du Forban" style="max-width:25%;"/></a>


## Le chiffrement des templiers
Les templiers chiffraient les lettres de crédit qu'ils mettaient en circulation entre leurs neuf mille commanderies pour éviter les transports de fonds. Leur alphabet de chiffrement était déduit de la croix dite des huit béatitudes qui constituait l'emblème de l'ordre.

<a href="/assets/img/chiffre/Templier2.png" data-lightbox="Chiffrement MonoAlphabétique" data-title="Croix des huit béatitudes"><img src="/assets/img/chiffre/Templier2.png" alt="Croix des huit béatitudes" style="max-width:25%;"/></a>
<a href="/assets/img/chiffre/Templier1.png" data-lightbox="Chiffrement MonoAlphabétique" data-title="Chiffre des templiers"><img src="/assets/img/chiffre/Templier1.png" alt="Chiffre des templiers" style="max-width:75%;"/></a>

## Voir plus loin
Il est possible de complexifier n'importe quel système de chiffrement monoalphabétique tout en gardant en mémoire que chaque symbole correspond à une et une seule lettre... Mais une lettre peut correspondre à plusieurs symboles. Lors du chiffrement, il suffit de choisir pour chaque lettre un des symboles de la liste qui lui correspond. 

Un exemple concret possible est l'utilisation de Kanji japonais avec plus de 6 000 Kanji différents (un peu moins de 2 000 sont utilisés couramment) pour chiffrer seulement 26 lettres. Plus simplement, l'utilisation des 46 Hiraganas ou Katakanas est possible (les 20 lettres les plus utilisées possèdent deux symboles et les six dernières, un seul).  
L'avantage de l'utilisation d'un alphabet étranger est l'impression d'avoir réellement affaire à un texte dans une langue étrangère.

Il est également possible de modifier la casse et l'espacement. Généralement, les messages chiffrés sont écrits par groupe de 4 ou 5 lettres majuscules. Pour les chiffrements par symbole, il est également possible de supprimer tous les espaces ou de les chiffrer avec un symbole spécifique.

## Les codages
### Le Braille
Le [braille](https://fr.wikipedia.org/wiki/Braille){:target="_blank"} n'est pas un chiffrement, mais un codage. Il suit le même principe où chaque lettre correspond à un symbole.  
Il s'agit d'un système d’écriture tactile à points saillants, à l’usage des personnes aveugles ou fortement malvoyantes. Chaque lettre est une combinaison de 6 points "activés" ou non ce qui correspond à 63 caractères ($$2^6-1$$) en plus de l'espace qui ne contient aucun point. Son nom vient du français [Louis Braille](https://fr.wikipedia.org/wiki/Louis_Braille){:target="_blank"}.  
**Nota Bene :** On utilise les termes chiffrement et déchiffrement s'il y a une volonté de protéger les données. Codage et décodage sont utilisés dans le cas d'une simple transformation des informations afin de faciliter leur transmission. Toutefois, les termes de codage et décodage peuvent être utilisés dans des situations plus complexes ou un mot peut être remplacé par un autre ou un numéro, il faut pour décoder le message un dictionnaire comme grille de conversion.

<form><table style="width:100%" border="1">
	<tr align="center">
		<th width="15%" align="left">Original</th>
		<td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
	</tr>
	<tr align="center" bgcolor="#F0F0F0" style="font-family:Braille">
		<th width="15%" align="left" style="font-family: 'Montserrat', sans-serif;">Braille</th>
		<td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
	</tr>
</table></form>

La grille ci-dessus utilise cette [Police](https://www.dafont.com/fr/braile-font.font){:target="_blank"} venant du site [www.dafont.com](http://www.dafont.com/){:target="_blank"}.




### Le Morse
Tout comme le Braille, le [Morse](https://fr.wikipedia.org/wiki/Code_Morse_international){:target="_blank"} est un codage, mais un peu plus particulier. En effet, ce code est effectué par des séries d’impulsions courtes et longues, qu’elles soient produites par des signes, une lumière, un son ou un geste. Le peu d'éléments différents (2 types de signes) implique une nomenclature dans la taille (ou durée) de chaque signe : 
- Un tiret est égal à 3 points
- L'espacement entre deux signes d'une même lettre est égal à 1 point
- L'espacement entre deux lettres d'un même mot est égal à 3 points
- L'espacement entre deux mots est égal à 7 points

<form><table style="width:100%" border="1">
	<tr align="center">
		<th width="15%" align="left">Original</th>
		<td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
	</tr>
	<tr align="center" bgcolor="#F0F0F0" style="font-family:Morse">
		<th width="15%" align="left" style="font-family: 'Montserrat', sans-serif;">Morse</th>
		<td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td>
	</tr>
</table></form>

la grille ci-dessus utilise cette [Police](https://www.dafont.com/fr/morse.font){:target="_blank"} venant du site [www.dafont.com](http://www.dafont.com/){:target="_blank"}.

# Assistant CEDA (Chiffrement Et Déchiffrement monoAlphabétique)
{% include CEDA.html %}