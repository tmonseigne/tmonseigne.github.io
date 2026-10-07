"""Illustre un classifieur à vecteurs de support et les marges de sa frontière linéaire."""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Générer des données aléatoires
features, y = make_blobs(n_samples=200, centers=2, random_state=42)

# Diviser les données en ensemble d'entraînement et de test
train_features, test_features, y_train, y_test = train_test_split(features, y, test_size=0.2, random_state=42)

# Créer un objet de classification SVM avec un noyau linéaire
clf = SVC(kernel="linear")

# Entraîner le modèle SVM
clf.fit(train_features, y_train)

# Prédire la classe des données de test
y_pred = clf.predict(test_features)

# Afficher l'exactitude du modèle
accuracy = np.mean(y_test == y_pred)
print("Exactitude :", accuracy)

# Afficher le graphique
plt.scatter(features[:, 0], features[:, 1], c=y, cmap=plt.cm.Paired)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Créer une grille pour évaluer le modèle
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
x_grid, y_grid = np.meshgrid(xx, yy)
xy = np.vstack([x_grid.ravel(), y_grid.ravel()]).T
predicted_labels = clf.decision_function(xy).reshape(x_grid.shape)

# Afficher les frontières de décision et les marges
ax.contour(x_grid, y_grid, predicted_labels, colors="k", levels=[-1, 0, 1], alpha=0.5, linestyles=["--", "-", "--"])
ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100, linewidth=1, facecolors="none", edgecolors="k")
plt.show()
