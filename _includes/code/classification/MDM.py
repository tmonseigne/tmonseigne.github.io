"""Illustre la classification par distance euclidienne aux moyennes des classes."""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

# chargement des données iris
iris = datasets.load_iris()

# sélection des deux premières caractéristiques (pour la visualisation)
features = iris.data[:, :2]
y = iris.target

# calcul des moyennes pour chaque classe
mean_vectors = []
for cl in range(3):
	mean_vectors.append(np.mean(features[y == cl], axis=0))


# fonction de calcul de la distance euclidienne entre deux vecteurs
# --------------------------------------------------
def euclidean_distance(x1: np.ndarray, x2: np.ndarray) -> np.floating:
	"""
	Calcule la distance euclidienne entre deux vecteurs de même taille.

	:param x1: Premier vecteur de caractéristiques.
	:param x2: Second vecteur de caractéristiques.
	:return: Distance euclidienne entre les vecteurs.
	"""
	return np.sqrt(np.sum((x1 - x2) ** 2))


# prédiction de la classe pour un ensemble de nouveaux échantillons
# --------------------------------------------------
def predict(features: np.ndarray, mean_vectors: list[np.ndarray]) -> list[int]:
	"""
	Attribue à chaque échantillon la classe dont la moyenne est la plus proche.

	:param features: Matrice des échantillons en lignes et des caractéristiques en colonnes.
	:param mean_vectors: Moyennes des classes, dans l’ordre de leurs identifiants.
	:return: Identifiant de classe prédit pour chaque échantillon.
	"""
	y_pred = []
	for x in features:
		distances = [euclidean_distance(x, mean_vec) for mean_vec in mean_vectors]
		min_dist = np.min(distances)
		min_dist_idx = distances.index(min_dist)
		y_pred.append(min_dist_idx)
	return y_pred


# prédiction pour un meshgrid de points pour la visualisation
xx, yy = np.meshgrid(np.arange(4, 8, 0.02), np.arange(1.5, 4.5, 0.02))
predicted_labels = np.array(predict(np.c_[xx.ravel(), yy.ravel()], mean_vectors))
predicted_labels = predicted_labels.reshape(xx.shape)

# affichage des résultats
plt.contourf(xx, yy, predicted_labels, alpha=0.2)
plt.scatter(features[:, 0], features[:, 1], c=y, alpha=1)
plt.xlabel("Longueur du sépale (cm)")
plt.ylabel("Largeur du sépale (cm)")
plt.title("Classification par distance minimale à la moyenne (iris)")
plt.show()
