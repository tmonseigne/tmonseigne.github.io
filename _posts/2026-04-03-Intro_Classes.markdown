---
layout: post
title: (Très) courte introduction aux classes
date: 2026-04-03
description: Comprendre les classes en Python et la programmation orientée objet
img: theme/Programmation-Theme.png
tags: [Explication]
author: Thibaut Monseigne
---

* TOC
{:toc}
{: .toc-post}

## Avant-propos : la programmation orientée objet

La **programmation orientée objet (POO)** est un paradigme de programmation qui consiste à organiser le code autour d’**objets**.  
Un objet regroupe des **données** (membres, variables), et des **comportements** (méthodes, fonctions).  

En pratique, la plupart des projets modernes mélangent plusieurs approches (procédurale, fonctionnelle, événementielle…).

L’outil central de la POO est : **la classe**.

<figure id="Fig1">
 <a href = "/assets/img/Classes/POO.svg" data-lightbox = "Memo" data-title = "Les Fondements de la POO"><img src = "/assets/img/Classes/POO.svg" alt = "Les Fondements de la POO" style = "max-width:100%;"/></a>
</figure>

## Les classes : définition et intérêt

**Définition** : Une **classe** est un modèle permettant de créer des objets. Un objet créé à partir d’une classe est appelé une **instance**.

**Intérêt** : Les classes permettent de structurer le code, regrouper des données et des fonctions liées, rendre le code plus lisible et maintenable.

**Quand utiliser une classe ?**  
On utilise une classe lorsque : plusieurs fonctions manipulent les mêmes données, on veut représenter une entité (ex. : image, matrice, particule…), on veut conserver un état et éviter de passer constamment les mêmes paramètres aux fonctions.  
À l’inverse, une simple fonction suffit si : le traitement est simple, il n’y a pas d’état à conserver.

## Exemple : une classe Matrix et calcul de la transposition

On va utiliser un exemple fil rouge : une matrice en python (dans un monde sans numpy).

### Version fonctionnelle (sans classe)

```python
def transpose(matrix: list) -> list: return list(map(list, zip(*matrix)))

l = [[1, 2], [3, 4], [5, 6]]
print(l)
>> [[1, 2], [3, 4], [5, 6]]

print(transpose(l))
>> [[1, 3, 5], [2, 4, 6]]
```

**Inconvénient** : aucune structure, aucune vérification, difficile à étendre.

### Version orientée objet

```python
class Matrix:
    def __init__(self, data: list):
        """
        Initialise une matrice.

        :param data: Liste de listes représentant la matrice
        """
        self.data: list = data
        self.rows:int = len(data)
        self.cols:int = len(data[0])

    def transpose(self):
        """ Retourne la transposée de la matrice. """
        return Matrix(list(map(list, zip(*self.data))))

m = Matrix([[1, 2], [3, 4], [5, 6]])
mt = m.transpose()
print(m.data)
>> [[1, 2], [3, 4], [5, 6]]

print(mt.data)
>> [[1, 3, 5], [2, 4, 6]]
```

**Avantage** : logique regroupée (`m.transpose()`), plus lisible, extensible.

La classe permet de stocker un **état interne**.
L’objet contient : des données (`data`) et des propriétés (`rows`, `cols`)

### Piège Python : mutabilité

```python
data = [[1, 2], [3, 4]]
m = Matrix(data)

data[0][0] = 999
print(m.data)
>> [[999, 2], [3, 4]]
```

Il a copié le lien vers le tableau d'origine et non le tableau en lui-même, résultat l’objet est modifié sans contrôle.

La solution consiste à copier le tableau au lieu de l'assigner :

```python
self.data: list = data
# devient
self.data: list = copy.deepcopy(data)
```

## Encapsulation : protéger les données

```python
class Matrix:
    def __init__(self, data: list):
        self._data: list = data

    @property
    def data(self): return self._data

m = Matrix([[1, 2], [3, 4]])
print(m.data)     # Fonctionne
m.data[0][0] = 0  # Affiche une erreur
```

Il existe une différence entre membre privé et public (et protégé pour certains langages). Un membre public peut être disponible à tout moment. Un membre privé n'est disponible qu'au sein de la classe. En python la convention veut que le membre (ou la méthode) commence par `_`. Dans cet exemple data ne peut être modifié directement, mais peut être lu sans problème.

**Remarque :** En réalité Python autorisera l'utilisation en faisant `m._data[0][0] = 0`, mais l'éditeur vous signalera que vous tentez d'accéder à un membre privé. Pour interdire absolument son appel, il faut mettre `__`, mais cela est rarement utilisé, car le débogage et les tests nécessitent parfois de vérifier ou modifier les valeurs à la volée.

## Surcharge d’opérateurs

Une classe permet de redéfinir le comportement des opérateurs (`+`, `-`, `*`, `[]`, etc.).

### Exemple : addition de matrices

```python
l1 = [[1, 2], [3, 4], [5, 6]]
l2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(l1 + l2)

>> [[1, 2], [3, 4], [5, 6], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

**Inconvénient** : Python permet l'ajout entre listes, mais cela ne correspond pas à une addition de matrice. Il faut définir une fonction spécifique. De plus, dans ce cas, il faudrait stopper l'opération, car il n'est pas possible d'additionner des matrices de tailles différentes

```python
class Matrix:
    # ...
    def __add__(self, other):
        """Addition de deux matrices."""
        if self.cols != other.cols or self.rows != other.rows: raise ValueError("Les dimensions des matrices ne correspondent pas.")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)


m1 = Matrix([[1, 2], [3, 4], [5, 6]])
m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m3 = m1 + m1
print(m3.data)
>> [[2, 4], [6, 8], [10, 12]]

m3 = m1 + m2
>> ValueError: Les dimensions des matrices ne correspondent pas.
```

**Avantage** : code plus naturel (m1 + m2), plus lisible, plus proche des mathématiques et possibilité de mettre des garde-fous en cas d'erreurs.

### Exemple : représentation textuelle

On peut voir l'utilisation de m.data lors des print, car la classe matrice ne possède pas de représentation textuelle.
Voici la représentation actuelle :

```python
m = Matrix([[1, 2], [3, 4], [5, 6]])
print(m)
>> <__main__.Matrix object at 0x000002D761F05310>
```

IL faut donc définir la représentation que nous souhaitons (j'en propose une un peu travaillée pour l'exemple.)

```python
class Matrix:
    # ...
    def __repr__(self):
        """Représentation lisible de la matrice sous forme tabulaire."""

        # Conversion en string + calcul de la largeur max
        str_data = [[str(val) for val in row] for row in self.data]
        max_width = max(len(val) for row in str_data for val in row)

        lines = []
        for row in str_data:
            formatted_row = " | ".join(f"{val:>{max_width}}" for val in row)
            lines.append(f"| {formatted_row} |")

        return "\n".join(lines)


m = Matrix([[1, 2], [3, 4], [5, 6]])
print(m)
>> | 1 | 2 |
>> | 3 | 4 |
>> | 5 | 6 |

print(m.transpose())
>> | 1 | 3 | 5 |
>> | 2 | 4 | 6 |
```

## Héritage et polymorphisme

L’héritage permet de créer une classe spécialisée à partir d’une autre. Celle-ci pourra avoir des comportements particuliers, des membres et méthodes supplémentaires. Mais elle possède également toutes les méthodes de sa classe mère c'est ce que l'on appelle le polymorphisme.

### Exemple : matrice carrée

Certaines opérations ne sont définies que pour les matrices carrées (ex. : déterminant).

```python
class SquareMatrix(Matrix):
    def __init__(self, data):
        super().__init__(data)

        if self.rows != self.cols:
            raise ValueError("La matrice doit être carrée")

    def trace(self):
        """Retourne la trace de la matrice."""
        return sum(self.data[i][i] for i in range(self.rows))


m = SquareMatrix([[1, 2], [3, 4]])
print(m.trace())  # Cette méthode n'est pas disponible pour une matrice standard
>> 5

print(m)  # Polymorphisme : la representation textuelle appartenant à la classe mère existe aussi pour la classe fille
>> | 1 | 2 |
>> | 3 | 4 |

m = Matrix([[1, 2], [3, 4]])
print(m.trace())
>> AttributeError: 'Matrix' object has no attribute 'trace'
```

## Composition VS Héritage

La composition consiste à intégrer une classe à l'intérieur d'une autre, cette nouvelle classe possède un objet qui est l'ancienne. Au contraire, l'héritage est une extension d'une classe initiale.

Exemple :

```python
class Image:
    def __init__(self, matrix: Matrix):
        self.matrix = matrix
```

Ces deux notions sont donc complémentaires et dépendent du cas.

<figure id="Fig2">
 <a href = "/assets/img/Classes/Composition.svg" data-lightbox = "Memo" data-title = "Différence entre la Composition et l'Héritage"><img src = "/assets/img/Classes/Composition.svg" alt = "Différence entre la Composition et l'Héritage" style = "max-width:75%;"/></a>
</figure>

## Les dataclasses en Python

Beaucoup de classes servent uniquement à stocker des données, Python possède un outil permettant de simplifier certaines parties du code.

### Exemple classique : une classe point

```python
class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

Solution : dataclass

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```

Python génère automatiquement une partie des fonctions : l'initialisation, la représentation textuelle et la comparaison (signe ==).
Cela permet de réduire la quantité de code (souvent des éléments répétitifs) et d'améliorer la lisibilité.

## Conclusion

Les classes sont un outil puissant pour structurer un programme.

Elles permettent : d’organiser les données, de regrouper les comportements, d’écrire un code plus lisible.

Cependant : elles ne sont pas toujours nécessaires, une fonction simple peut parfois suffire.

<figure id="Fig3">
 <a href = "/assets/img/Classes/Conclusion.svg" data-lightbox = "Memo" data-title = "De la fonction à la classe"><img src = "/assets/img/Classes/Conclusion.svg" alt = "De la fonction à la classe" style = "max-width:75%;"/></a>
</figure>