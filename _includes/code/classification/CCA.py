"""Illustre l’analyse de corrélation canonique entre deux ensembles de caractéristiques."""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_decomposition import CCA

# Générer des données aléatoires
np.random.seed(42)

n_samples = 1000
n_features_1 = 2
n_features_2 = 2

first_features = np.random.rand(n_samples, n_features_1)
second_features = np.random.rand(n_samples, n_features_2)

# Introduire une corrélation entre les deux ensembles de données
second_features[:, 0] = 0.8 * first_features[:, 0] + 0.2 * first_features[:, 1]

# Appliquer l'analyse de corrélation canonique
cca = CCA(n_components=1)
cca.fit(first_features, second_features)

# Obtenir les scores pour chaque ensemble de données
first_scores, second_scores = cca.transform(first_features, second_features)

# Tracer les scores pour chaque ensemble de données
plt.scatter(first_scores, second_scores)
plt.xlabel("Scores ensemble de données 1")
plt.ylabel("Scores ensemble de données 2")
plt.show()
