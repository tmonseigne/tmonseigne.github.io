"""Illustre la classification par les plus proches voisins et sa frontière de décision."""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Génération de données aléatoires
features, y = make_blobs(n_samples=200, centers=3, random_state=42)

# Division des données en ensembles d'entraînement et de test
train_features, test_features, y_train, y_test = train_test_split(features, y, test_size=0.2, random_state=42)

# Entraînement du modèle de k plus proches voisins
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(train_features, y_train)

# Prédiction sur l'ensemble de test
y_pred = knn.predict(test_features)

# Calcul de la précision du modèle
accuracy = knn.score(test_features, y_test)
print("Exactitude :", accuracy)

# Affichage de la frontière de décision
h = 0.02  # pas de la grille
x_min, x_max = features[:, 0].min() - 0.5, features[:, 0].max() + 0.5
y_min, y_max = features[:, 1].min() - 0.5, features[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
predicted_labels = knn.predict(np.c_[xx.ravel(), yy.ravel()])

# Affichage de la frontière de décision
predicted_labels = predicted_labels.reshape(xx.shape)
plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, predicted_labels, alpha=0.2)  # Affichage des zones
plt.scatter(features[:, 0], features[:, 1], c=y, s=20, edgecolor="k")  # Affichage des points
plt.title("Frontière de décision avec k plus proches voisins")
plt.xlabel("X1")
plt.ylabel("X2")
plt.show()
