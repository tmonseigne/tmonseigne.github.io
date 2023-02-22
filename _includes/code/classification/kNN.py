import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Génération de données aléatoires
X, y = make_blobs(n_samples=200, centers=3, random_state=42)

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle de k plus proches voisins
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Prédiction sur l'ensemble de test
y_pred = knn.predict(X_test)

# Calcul de la précision du modèle
accuracy = knn.score(X_test, y_test)
print("Precision :", accuracy)

# Affichage de la frontière de décision
h = 0.02  # pas de la grille
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

# Affichage de la frontière de décision
Z = Z.reshape(xx.shape)
plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, Z, alpha=0.2) # Affichage des zones
plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor='k') # Affichage des points
plt.title('Frontière de décision avec k plus proches voisins')
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()