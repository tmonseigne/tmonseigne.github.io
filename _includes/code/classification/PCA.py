"""Illustre la projection des données sur les composantes principales."""

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Chargement des données d'exemple iris
iris = load_iris()

# Réduction de la dimension à 2 en utilisant PCA
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(iris.data)

# Affichage des résultats
fig, ax = plt.subplots()
scatter = ax.scatter(reduced_features[:, 0], reduced_features[:, 1], c=iris.target, cmap="viridis")
legend = ax.legend(*scatter.legend_elements(), loc="lower left", title="Classes")
ax.add_artist(legend)
plt.show()
