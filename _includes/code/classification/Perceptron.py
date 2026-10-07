"""Illustre la classification par perceptron sur des données à deux caractéristiques."""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Générer des données aléatoires à deux dimensions avec une classe bien séparée de l'autre.
features, y = make_classification(n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1, random_state=42)

# Division des données en ensembles d'entraînement et de test
train_features, test_features, y_train, y_test = train_test_split(features, y, test_size=0.2, random_state=42)

# Création et entraînement du modèle
clf = Perceptron(random_state=42)
clf.fit(train_features, y_train)

# Prédiction sur l'ensemble de test
y_pred = clf.predict(test_features)

# Calcul de la précision
accuracy = accuracy_score(y_test, y_pred)
print("Exactitude :", accuracy)

# Visualisation de la séparation de décision
x_min, x_max = features[:, 0].min() - 0.5, features[:, 0].max() + 0.5
y_min, y_max = features[:, 1].min() - 0.5, features[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
predicted_labels = clf.predict(np.c_[xx.ravel(), yy.ravel()])
predicted_labels = predicted_labels.reshape(xx.shape)
plt.contourf(xx, yy, predicted_labels, alpha=0.2)
plt.scatter(features[:, 0], features[:, 1], c=y, alpha=1)
plt.show()
