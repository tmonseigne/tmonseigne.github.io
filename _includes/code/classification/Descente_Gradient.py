"""Illustre l’apprentissage d’une régression linéaire par descente de gradient sur mini-lots."""

import matplotlib.pyplot as plt
import numpy as np

# Générer un jeu de données (données aléatoires pour x et y)
features = 2 * np.random.rand(100, 1)
y = 4 + 3 * features + np.random.randn(100, 1)

# Ajouter une colonne de 1 à x pour le biais
features_with_bias = np.c_[np.ones((100, 1)), features]

# Configuration des hyperparamètres
eta = 0.1  # taux d'apprentissage
n_iterations = 1000  # nombre d'itérations
m = 100  # taille du batch (nombre d'échantillons du sous-ensemble)

# Initialiser les poids aléatoirement
theta = np.random.randn(2, 1)

# Boucle d'entraînement par mini-batch
for _iteration in range(n_iterations):
	# Sélectionner un mini-batch aléatoire
	indices = np.random.randint(m, size=m)
	batch_features = features_with_bias[indices]
	y_batch = y[indices]

	# Calculer le gradient
	gradients = 2 / m * batch_features.T.dot(batch_features.dot(theta) - y_batch)

	# Mettre à jour les poids
	theta = theta - eta * gradients

# Afficher les poids obtenus
print(theta)

# Générer les prédictions pour le graphique
new_features = np.array([[0], [2]])
new_features_with_bias = np.c_[np.ones((2, 1)), new_features]
y_predict = new_features_with_bias.dot(theta)

# Afficher le graphique
plt.plot(new_features, y_predict, "r-", label="Prédictions")
plt.plot(features, y, "b.", label="Données")
plt.legend()
plt.show()
