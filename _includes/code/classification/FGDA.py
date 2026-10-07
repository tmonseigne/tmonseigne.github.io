"""Illustre une analyse discriminante après lissage local par les voisins pondérés."""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import NearestNeighbors

# Génération de données aléatoires
features, y = make_blobs(n_samples=100, centers=3, random_state=42)

# Calcul des voisins pondérés
k = 5
neigh = NearestNeighbors(n_neighbors=k)
neigh.fit(features)
distances, indices = neigh.kneighbors(features)

weighted_points = []
for i in range(features.shape[0]):
	weights = np.exp(-(distances[i] ** 2) / (2 * np.var(distances[i])))
	weights /= np.sum(weights)
	weighted = np.sum([weights[j] * features[indices[i][j]] for j in range(k)], axis=0)
	weighted_points.append(weighted)

weighted_neighbours = np.array(weighted_points)

# Vérification du nombre de classes
n_classes = len(np.unique(y))
if n_classes <= k:
	k = n_classes - 1

# Filtrage géodésique avec analyse discriminante de Fisher
lda = LinearDiscriminantAnalysis(n_components=2)
discriminant_filter = lda.fit(weighted_neighbours, y[indices[:, 0]])
transformed_features = discriminant_filter.transform(features)

# Affichage des données
plt.scatter(transformed_features[:, 0], transformed_features[:, 1], c=y, cmap=plt.cm.Set1)
plt.show()
