import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import NearestNeighbors

# Génération de données aléatoires
X, y = make_blobs(n_samples=100, centers=3, random_state=42)

# Calcul des voisins pondérés
k = 5
neigh = NearestNeighbors(n_neighbors=k)
neigh.fit(X)
distances, indices = neigh.kneighbors(X)

weighted_neighbours = []
for i in range(X.shape[0]):
    weights = np.exp(-distances[i] ** 2 / (2 * np.var(distances[i])))
    weights /= np.sum(weights)
    weighted = np.sum([weights[j] * X[indices[i][j]] for j in range(k)], axis=0)
    weighted_neighbours.append(weighted)

weighted_neighbours = np.array(weighted_neighbours)

# Vérification du nombre de classes
n_classes = len(np.unique(y))
if n_classes <= k:
    k = n_classes - 1

# Filtrage géodésique avec analyse discriminante de Fisher
lda = LinearDiscriminantAnalysis(n_components=2)
filter = lda.fit(weighted_neighbours, y[indices[:, 0]])
X_transformed = filter.transform(X)

# Affichage des données
plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y, cmap=plt.cm.Set1)
plt.show()