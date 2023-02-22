import numpy as np
import matplotlib.pyplot as plt

# Générer un dataset (données aléatoires pour x et y)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Ajouter une colonne de 1 à x pour le biais
X_b = np.c_[np.ones((100, 1)), X]

# Configuration des hyperparamètres
eta = 0.1  # taux d'apprentissage
n_iterations = 1000  # nombre d'itérations
m = 100  # taille du batch (nombre d'échantillons du sous-ensemble)

# Initialiser les poids aléatoirement
theta = np.random.randn(2, 1)

# Boucle d'entraînement par mini-batch
for iteration in range(n_iterations):
    # Sélectionner un mini-batch aléatoire
    indices = np.random.randint(m, size=m)
    X_batch = X_b[indices]
    y_batch = y[indices]
    
    # Calculer le gradient
    gradients = 2/m * X_batch.T.dot(X_batch.dot(theta) - y_batch)
    
    # Mettre à jour les poids
    theta = theta - eta * gradients

# Afficher les poids obtenus
print(theta)

# Générer les prédictions pour le graphique
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta)

# Afficher le graphique
plt.plot(X_new, y_predict, "r-", label="Prédictions")
plt.plot(X, y, "b.", label="Données")
plt.legend()
plt.show()