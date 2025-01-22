---
layout: post
title: Bases des bonnes pratiques de programmation
date: 2024-01-30
description: Quelques informations de base sur de bonnes pratiques de programmation
img: theme/Programmation-Theme.png
tags: [Explication]
author: Thibaut Monseigne
---

* TOC
{:toc}
{: .toc-post}

**Avant-propos** :  
Il n'existe pas de bonnes ou mauvaises pratiques **absolues** en programmation. Cependant, adopter des conventions largement reconnues et s'adapter au contexte est essentiel.  
Par exemple, tout comme nous avons chacun nos tics de langage à l’oral, nos habitudes de codage reflètent notre style.  
Dans un projet, établir des règles claires assure la cohérence et la collaboration en équipe. Ces règles, souvent définies par un **lead développeur** ou une charte interne, servent de guide pour écrire un code lisible, maintenable et pérenne.
{: .Note}

## Les règles de codage (Coding Rules)

Adopter un style de codage cohérent est essentiel pour maintenir un projet compréhensible. Quelques pratiques de base :

* Indentation : Choisir entre espaces ou tabulations et s'y tenir. En Python, on utilise généralement 4 espaces.
* Nom des variables et fonctions :
  * Privilégier des noms explicites : def calculer_taxe(prix): est plus clair que def ct(p):.
  * Respecter les conventions : [snake_case](https://fr.wikipedia.org/wiki/Snake_case) pour Python, camelCase pour JavaScript, etc.
* Commentaires et docstrings :
  * On doit comprendre de suite à quoi sert un code.
  * Utiliser des docstrings pour documenter les fonctions et classes en Python.
* Outils d’analyse :
  * Utiliser un linter comme `flake8` (Python) ou `eslint` (JavaScript) pour détecter les erreurs de style.
  * Automatiser ces vérifications avec des hooks Git comme `pre-commit`.
  
## Le versionning

Le versionning est une pratique essentielle pour tout projet, qu’il soit individuel ou collaboratif. Voici quelques bonnes pratiques :

* Utiliser un système de gestion de versions (VCS) : Git est le plus populaire. Il permet de suivre les modifications, de collaborer et de revenir à des états antérieurs si nécessaire (voir la [(Très) courte introduction à Git](../Intro_Git/){:target="_blank"}).
* Respecter une [convention de nommage](https://fr.wikipedia.org/wiki/Convention_de_nommage) des branches : main ou master pour la branche principale et une convention de nommage type [dash-case](https://en.wikipedia.org/wiki/Letter_case#Kebab_case).
* Commits clairs et fréquents :
  * Un commit doit être petit et cohérent.
  * Les messages de commit doivent être explicites, par exemple : fix: correction du bug de connexion ou feat: ajout de l'authentification OAuth.
  * L'utilisation [Gitmoji](https://gitmoji.dev/) permet de structurer visuellement les commits.
* Tags et releases : Utiliser les tags Git pour marquer des versions stables (v1.0.0, v2.1.0), en suivant une nomenclature comme [SemVer](https://semver.org/lang/fr/).


## L'intégration continue et les tests

L'intégration continue (CI) garantit que votre code fonctionne toujours correctement après des modifications. Quelques étapes clés :

* Configurer une CI : Utiliser des plateformes comme `GitHub Actions`, `GitLab CI` ou `Jenkins`.
* Automatiser les tests :
  * Exécuter les tests unitaires et d’intégration à chaque modification.
  * S'assurer que le code ne casse pas les fonctionnalités existantes.
* Déployer automatiquement : Configurer un pipeline pour automatiser les livraisons sur un environnement de test ou de production.

Le principe de base est de vérifier si la routine d'installation et de lancement de tests fonctionne dans un environnement *propre* (sans aucune installation préalable).

## La couverture de code

La couverture de code mesure quelle proportion de votre base de code est testée. Voici comment l'aborder :

* Utiliser un outil adapté : `pytest-cov` pour Python, `GoogleTest` en C++, `Jest` en JavaScript...
* Interpréter la couverture : Un taux élevé (>80%) est souvent un bon objectif, mais il ne garantit pas l'absence de bugs.
* Prioriser les tests critiques : Testez en priorité les fonctionnalités essentielles et les cas limites.

## La documentation

Une bonne documentation est aussi importante que le code lui-même. Quelques conseils :

* Structurer la documentation :
  * Introduction, tutoriels, API, et FAQ.
  * Utiliser des outils comme `Sphinx` (Python) ou Doxygen (multilangage, mais originellement pour du C++).
* Inclure des exemples : Montrez comment utiliser votre code avec des cas concrets.
* Mettre à jour régulièrement : La documentation doit évoluer avec le projet.

## Exemple pratique avec un plugin Napari en Python

Nous utiliserons un [template](https://github.com/napari/napari-plugin-template) de plugin proposé par Napari qui propose ou impose certains points comme la structure de projet ou l'utilisation de Tox et Pytest pour les tests.
{: .Note}

### Le versionning

Le versionning pour ce plugin se fera sous Git avec [GitHub](https://github.com/), la branche principale suffira la plupart du temps à elle seule.  
Le cas d'ajout de fonctionnalité pourra se faire sur des branches annexes déployées automatiquement par l'intermédiaire d'une *Issue* sur le dépôt. Cette méthode sera de plus en plus utilisée à mesure du grossissement du projet.  
Les fusions avec la branche principale se feront par l'intermédiaire des `merge request` associés à l'issue initiatrice de la branche.  
Des branches de tests pourront être créées à la volée avec comme nomenclature `test-nom-du-test`. Elles ne seront jamais fusionnées telles quelles, seules les branches venant d'une *Issue* seront fusionnées (la création d'une issue et un nettoyage des commits devra donc être effectuée).  
Les [Gitmoji](https://gitmoji.dev/) seront utilisés dans les noms de commits et issue.

### Les règles de codage (Coding Rules)

#### Python et PEP8

Python est l'un des rares langages à avoir un coding style prédéfini largement répandu, il s'agit de [PEP 8](https://peps.python.org/pep-0008/). Certains linters comme [Black](https://github.com/psf/black) imposent un respect strict de ses règles, parfois un peu désuètes. Par exemple une ligne ne doit pas dépasser 88 caractères. À notre époque, la taille des écrans permet de dépasser cette limite sans que cela soit gênant.

Avec Python, nous pouvons utiliser [Pycharm](https://www.jetbrains.com/fr-fr/pycharm/), un [Environnement de développement](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement). Il permet de régler soi-même un certain nombre de comportements lors de l'écriture du code pour forcer le respect des règles ou avertir l'utilisateur d'une entorse aux conventions. Nous pouvons, par exemple, décider d'utiliser les tabulations pour l'indentation au lieu des espaces ce qui est incompatible avec PEP8, mais courant chez de nombreux développeurs.

#### Les précommits

Le précommit est un outil qui vous permet de configurer et d'exécuter automatiquement des scripts ou des vérifications (appelés "hooks") chaque fois que vous effectuez certaines actions sur votre dépôt Git, comme un commit ou un push. Ces hooks permettent d'assurer que votre code respecte des standards de qualité ou des conventions spécifiques avant d'être soumis au dépôt.

Pour être utilisé, vous devez d'abord installer `Pre-commit` dans votre environnement Python :

```bash
pip install pre-commit
```

La configuration se fait dans un fichier nommé `.pre-commit-config.yaml`.
Ensuite, il faut installer les hooks pour le dépôt actuel avec :

```bash
pre-commit install
```

Une fois configurés, les hooks s'exécutent automatiquement à chaque commit. Si un hook échoue, le commit est bloqué jusqu'à la correction.

Il est possible de lancer le processus de précommit en ligne de commande sur tous les fichiers sans spécialement faire de commit.

```bash
pre-commit run --all-files                                                                      
```

Avec le template du plugin Napari, un fichier de config est déjà présent.

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: check-docstring-first
      - id: end-of-file-fixer
      - id: trailing-whitespace
        exclude: ^\.napari-hub/.*
      - id: check-yaml # checks for correct yaml syntax for GitHub actions ex.
  # I'm not agree with PEP8 so black and ruff are skipped
  #  - repo: https://github.com/astral-sh/ruff-pre-commit
  #    rev: v0.8.1
  #    hooks:
  #      - id: ruff
  #  - repo: https://github.com/psf/black
  #    rev: 24.10.0
  #    hooks:
  #      - id: black
  - repo: https://github.com/tlambert03/napari-plugin-checks
    rev: v0.3.0
    hooks:
      - id: napari-plugin-checks
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.9.0
    hooks:
      - id: mypy
```

### L'intégration continue et les tests

#### GitHub Actions

Avec GitHub, il existe un environnement d'intégration continue qui est le GitHub action. Il suffit d'avoir un fichier `yaml` qui sera détecté par GitHub lors des mises à jour du dépôt. Ce fichier est détaillé plus bas.

#### Pytest

[Pytest](https://docs.pytest.org/en/stable/) est un framework de test unitaire.  
Pour être utilisé, vous devez d'abord installer `Pytest` dans votre environnement Python :

```bash
pip install pytest
```

Il faut prendre en considération que les tests servent avant tout à tester le comportement de votre code dans des situations contrôlées.
Si l'on prend pour exemple une fonction qui inverse un nombre donc $$x$$ deviendra $$1/x$$.  
vous écrivez un test où vous lui donnez $$2$$ et vous voyez s'il sort $$0.5$$ le test passe.

voici ma fonction :

```python
def ma_fonction(x: int) -> int:
  """ Retourne l'inverse d'un nombre. """
  return 1/x
```

```python
def test_fonction_inverse():
  """ Test basique de ma fonction. """
  res = ma_fonction(2)
  assert res == 0.5, f"Le résultat est {res} au lieu de 0.5"
```

Le test ne fonctionne pas et j'ai le message `Le résultat est 0 au lieu de 0.5`.

Je modifie ma fonction, car j'ai typé ma fonction pour des entiers alors que les décimales devraient être utilisées.

```python
def ma_fonction(x: float) -> float:
  """ Retourne l'inverse d'un nombre. """
  return 1/x
```

Le test passe maintenant.

Même lorsque la fonction est complexe, il est préférable de trouver des valeurs en entrée qui permettent de connaitre la sortie. Un traitement d'image complexe pourrait se faire sur une image plus petite entièrement noire ou avec un damier.

Les tests unitaires servent aussi, et surtout, à vérifier les comportements gênants.
Sur l'exemple précédent, que faire si en entrée on reçoit $$0$$, on va considérer que dans ce cas, il nous retourne l'infini.

```python
def test_fonction_inverse_bad_input():
  """ Test de ma fonction avec une entrée invalide. """
  res = ma_fonction(0)
  assert res == np.inf, f"Le résultat est {res} au lieu de infini"
```

La fonction plante et ne me renvoie aucun message, je n'ai pas prévu le cas où une division par 0 est possible et Python plante dans ce cas là. Je modifie donc ma fonction.

```python
def ma_fonction(x: float) -> float:
  """
  Retourne l'inverse d'un nombre.
  Si x = 0, renvoie np.inf pour éviter une division par zéro.
  """
  if x == 0: return np.inf
  return 1/x
```

Maintenant, mon test passe.

Une méthode de création de tests est de les créer avant de coder la fonction, de prendre en compte tous les cas bizarres qui puissent arriver et considérer que le code est complet quand les tests passent.

On peut utiliser un fichier `pytest.ini` pour configurer les arguments lors du lancement de la commande `pytest` (et ne pas avoir à les réécrire à chaque fois), en voici un exemple :

```bash
[pytest]
# Indiquer où chercher les tests
testpaths = mon_module/_tests/ # Dossier des tests
python_files = test_*.py       # format de fichiers contenant les tests

# Définir des options de ligne de commande par défaut
addopts = -s -v --color=yes
          --cov=. --cov-report=xml:reports/coverage.xml
          --cov-config=.coveragerc
          --json-report --json-report-file=reports/test_report.json
          --capture=tee-sys
```

Ici, on lui demande d'être explicite dans la sortie des tests, de stocker les résultats dans un fichier `json`, on récupère également la couverture de code que l'on détaille dans la partie suivante.

On peut utiliser un fichier `conftest.py` pour modifier le comportement de pytest en intervenant au début de chaque test, au début de la session, à la fin...
Dans notre exemple, nous ajoutons un monitoring des ressources système avec le code suivant :

```python
import json
import platform

import cpuinfo
import psutil
import pytest
from pytest_metadata.plugin import metadata_key

from mon_module.Tools import Monitoring, print_warning

all_tests_monitoring = Monitoring()


##################################################
def cpu_infos() -> str:
  info = cpuinfo.get_cpu_info()
  res = info.get('processor', 'Unknown Processor')
  try:  # En cas e problème notamment sur mac
    cpu_info = psutil.cpu_freq(percpu=False)
    res += f" ({cpu_info.current / 1000} GHz - {psutil.cpu_count(logical=False)} Cores ({psutil.cpu_count(logical=True)} Logical))"
  except RuntimeError: res += "(No CPU Infos)"
  return res


##################################################
def add_to_json(path, datas_name, datas):
  try:
    with open(path, "r") as f: data = json.load(f)
    data[datas_name] = datas
    with open(path, "w") as f: json.dump(data, f, indent=4)
  except FileNotFoundError: print_warning("Json File not found.")


##################################################
# Fonction pour configurer les métadonnées du rapport
@pytest.hookimpl
def pytest_metadata(metadata):
  metadata['System'] = platform.system()
  metadata['Platform'] = platform.platform()
  metadata['CPU'] = cpu_infos()
  metadata['RAM'] = f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB"

  ## Ajout de la carte graphique si disponible
  try:
    import GPUtil
    gpus = GPUtil.getGPUs()
    if gpus: metadata['GPU'] = f"{gpus[0].name} (Memory: {gpus[0].memoryTotal}MB)"
    else: metadata['GPU'] = 'No GPU found'
  except ImportError:
    metadata['GPU'] = 'GPUtil not installed'


##################################################
@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
  global all_tests_monitoring
  all_tests_monitoring.start(0.1)


##################################################
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
  global all_tests_monitoring
  all_tests_monitoring.stop()
  for ext in ["png", "html", "json", "txt"]:
    all_tests_monitoring.save(f"reports/monitoring.{ext}")
  add_to_json("reports/test_report.json", "metadata", session.config.stash[metadata_key])


##################################################
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_protocol(item, nextitem):
  """ Capture les informations sur chaque test """
  global all_tests_monitoring
  all_tests_monitoring.add_test_info(item.nodeid)
  return None

```

### La couverture de code

Avec python, il est très simple de mesurer la couverture de code, car Pytest possède une option permettant d'avoir en sortie un rapport complet.
Il regarde chaque ligne du code (excluant les lignes vides et les commentaires), puis indique si l'on passe à un moment durant les tests sur cette ligne ou non et aussi dans le cas d'une condition, vérifie si la condition est toujours identique et l'indique. Par exemple, sur notre code précédent, si on ne teste jamais le cas où $$x=0$$. la ligne sera indiqué comme semi valide, car on n'a jamais validé cette condition.

comme pour les tests, on peut utiliser un fichier `.coveragerc` pour configurer le comportement de la couverture de code, en voici un exemple :

```bash
[coverage:run]
branch = True
source = mon_module  # Analyse seulement ce module

[coverage:report]
# Exclure toutes les lignes de code dans les fichiers de test, exemples, le main et les init. Ils ne sont là qu'en support et ne forment pas le coeur du projet.
omit =
    mon_module/_tests/*
    examples/*
    main.py
    conftest.py
    **/__init__.py

exclude_lines =
    # Ces commentaires excluent des lignes spécifiques si elles sont détectées 
    pragma: no cover

exclude_also = # Les lignes ayant cette formule seront également ignorées
    if platform.system()
```

Ce fichier est mis en paramètre lors de l'exécution des tests (voir le `pytest.ini` de la section précédente).

### La documentation

Pour tout code, la documentation peut être générée par de nombreuses façons différentes, mais pour Python il est extrêmement courant d'utiliser [Sphinx](https://www.sphinx-doc.org/fr/master/). Il gère de façon presque automatique la documentation de votre code et prend en charge différents formats pour des pages personnalisées.

La documentation est générée dans une routine de l'intégration continue.
Dans notre cas, nous prenons également les rapports de tests en sortie de la routine d'exécution des tests.

### Fichier d'intégration continue complet pour le plugin Napari

Le fichier est situé ici : `.github/workflows/test_and_deploy.yml`

#### Première Partie : la configuration générale

```yaml
name: Test and Deploy # Nom de la routine

on:                   # A quel moment doit-on la lancer ?
  push:               # Lors d'une mise à jour sur les branches citées ci-dessous
    branches:
      - master
      - npe2
    tags:             # Ou Si un tag de version est ajouté
      - "v*"
  pull_request:       # Lors d'une demande de fusion vers les branches citées ci-dessous
    branches:
      - master
      - npe2
  workflow_dispatch:  # Permet d'exécuter le workflow manuellement depuis l'onglet Actions

# Autorisations supplémentaires pour la routine (utile pour la documentation)
permissions:
  contents: read
  pages: write
  id-token: write

# Option supplémentaire évitant des problèmes lors de la mise à jour de la documentation.
concurrency: 
  group: "pages"
  cancel-in-progress: false
```

#### Seconde Partie : Définition de la routine d'exécution des tests

```yaml
# Liste des routines qui seront lancées
jobs:
  Test:
    name: Tests on ${{ matrix.platform }} for Python ${{ matrix.python-version }}
    runs-on: ${{ matrix.platform }}
    timeout-minutes: 30 # Limite la durée de la routine 
    strategy:
      fail-fast: false  # Continue les autres routines si une matrice échoue.
      matrix:           # Définition de la matrice de test (ici, pour les 3 OS et les 5 versions de python donc 15 lancements)
        platform: [ ubuntu-latest, windows-latest, macos-latest ]
        python-version: ["3.9", "3.10", "3.11", "3.12", "3.13"]

    steps:
      # Récupération du dépot dans l'environnement
      - name: Checkout code
        uses: actions/checkout@v4

      # Installation de Python
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      # Installation de QT pour Linux
      - name: Set up QT For Linux (libxcb, x11...)
        uses: tlambert03/setup-qt-libs@v1

      # Installation d'OpenGL pour Windows
      - name: Install Windows OpenGL
        if: runner.os == 'Windows'
        run: |
          git clone --depth 1 https://github.com/pyvista/gl-ci-helpers.git
          powershell gl-ci-helpers/appveyor/install_opengl.ps1

      # Installation des dépendances permettant de lancer les tests
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install setuptools tox tox-gh-actions ansi2html

      # Lancement des tests par l'intermédiaire du fichier tox.ini
      - name: Run tests with tox
        uses: aganders3/headless-gui@v2
        with:
          run: python -m tox
        env:
          PLATFORM: ${{ matrix.platform }}

      # Converti les rapports de tests en un format pour la documentation en ligne
      - name: Manage Test Reports
        run: |
          python ./docs/tools/pytest_json_to_rst.py ./reports/test_report.json ./reports/test_report_ci_${{ matrix.platform }}_${{ matrix.python-version }}.rst
          mv ./reports/monitoring.html ./reports/monitoring_ci_${{ matrix.platform }}_${{ matrix.python-version }}.html
        continue-on-error: true  # Permet de continuer même si cette étape échoue

      # Conserve en mémoire les rapports de tests pour une utilisation ultérieure
      - name: Upload Test Reports as Artifacts
        uses: actions/upload-artifact@v3  # Limiter à V3 pour le moment la V4 est bugué
        with:
          name: reports
          path: |
            reports/test_report_ci_*.rst
            reports/monitoring_ci_*.html
        continue-on-error: true  # Permet de continuer même si cette étape échoue

      # Esporte le résultat de la couverture de code sur un site dédié (codecov.io)
      - name: Upload coverage reports to Codecov
        if: matrix.platform == 'ubuntu-latest' && matrix.python-version == '3.13'
        uses: codecov/codecov-action@v5
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          slug: tmonseigne/palm-tracer
```

#### Troisième Partie : Définition de la routine de déploiement de la documentation

```yaml
  Documentation:
    name: Build and Deploy Sphinx Documentation
    needs: [ Test ]  # Nécessite la reussite de la routine précédnte
    runs-on: ubuntu-latest

    steps:
      # Récupération du dépot dans l'environnement
      - name: Checkout code
        uses: actions/checkout@v4

      # Installation de Python
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      # Installation des dépendances permettant de construire la documentation
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install .[documentation]

      # Récupération des rapports générés lors des tests
      - name: Download Test Reports
        uses: actions/download-artifact@v3
        with:
          name: reports
          path: docs/reports/

      # Génération d'un fichier sommaire pour les rapports de tests et construction de la documentation.
      - name: Build documentation
        run: |
          python ./docs/tools/generate_test_reports_toc.py
          sphinx-build -b html docs/ docs/_build/html

      # Préparation des GitHub Pages.
      - name: Setup Pages
        uses: actions/configure-pages@v5

      # Conserve en mémoire le site généré pour une utilisation ultérieure
      - name: Upload documentation to GitHub Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: 'docs/_build/html'

      # Déploiement sur les GitHub Pages.
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```
