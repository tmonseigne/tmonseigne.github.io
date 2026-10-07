"""Illustre la régression par arbre de décision et la visualisation de l’arbre appris."""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree

# Générer des données aléatoires
np.random.seed(42)
x1 = np.random.rand(100)
x2 = 0.5 * x1 + np.random.normal(0, 0.03, size=100)
x3 = 0.8 * x2 + np.random.normal(0, 0.05, size=100)
y = 2 * x1 + 3 * x2 + 4 * x3 + np.random.normal(0, 0.1, size=100)

# Regroupement de l'ensemble de données en une seule matrice
features = np.column_stack((x1, x2, x3))

# Division des données en ensembles d'entraînement et de test
train_features, test_features, y_train, y_test = train_test_split(features, y, test_size=0.2, random_state=42)

# Création et entraînement d'un arbre de décision de régression
tree_reg = DecisionTreeRegressor(max_depth=3)
tree_reg.fit(train_features, y_train)

# Prédiction sur l'ensemble de test
y_pred = tree_reg.predict(test_features)

# Calcul de l'erreur quadratique moyenne
mse = np.mean((y_test - y_pred) ** 2)

print("MSE:", mse)

# Visualisation de l'arbre de décision entraîné
plt.figure(figsize=(15, 10))
plot_tree(tree_reg, filled=True)
plt.show()
