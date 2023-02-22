import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# chargement des données iris
iris = datasets.load_iris()

# sélection des deux premières caractéristiques (pour la visualisation)
X = iris.data[:, :2]
y = iris.target

# calcul des moyennes pour chaque classe
mean_vectors = []
for cl in range(3):
    mean_vectors.append(np.mean(X[y==cl], axis=0))

# fonction de calcul de la distance euclidienne entre deux vecteurs
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

# prédiction de la classe pour un nouvel échantillon
def predict(X, mean_vectors):
    y_pred = []
    for x in X:
        distances = [euclidean_distance(x, mean_vec) for mean_vec in mean_vectors]
        min_dist = np.min(distances)
        min_dist_idx = distances.index(min_dist)
        y_pred.append(min_dist_idx)
    return y_pred

# prédiction pour un meshgrid de points pour la visualisation
xx, yy = np.meshgrid(np.arange(4, 8, 0.02), np.arange(1.5, 4.5, 0.02))
Z = np.array(predict(np.c_[xx.ravel(), yy.ravel()], mean_vectors))
Z = Z.reshape(xx.shape)

# affichage des résultats
plt.contourf(xx, yy, Z, alpha=0.2)
plt.scatter(X[:, 0], X[:, 1], c=y, alpha=1)
plt.xlabel('Longueur du sepale (cm)')
plt.ylabel('Largeur du sepale (cm)')
plt.title('Classification par distance minimale à la moyenne (iris)')
plt.show()