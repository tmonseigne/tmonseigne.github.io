import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Générer des données aléatoires
X, y = make_blobs(n_samples=200, centers=2, random_state=42)

# Diviser les données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer un objet de classification SVM avec un noyau linéaire
clf = SVC(kernel='linear')

# Entraîner le modèle SVM
clf.fit(X_train, y_train)

# Prédire la classe des données de test
y_pred = clf.predict(X_test)

# Afficher l'exactitude du modèle
accuracy = np.mean(y_test == y_pred)
print("Precision :", accuracy)

# Afficher le graphique
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Créer une grille pour évaluer le modèle
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
XX, YY = np.meshgrid(xx, yy)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# Afficher les frontières de décision et les marges
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100, linewidth=1, facecolors='none', edgecolors='k')
plt.show()