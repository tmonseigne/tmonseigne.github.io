"""Illustre la régression par forêt aléatoire et l’importance des caractéristiques."""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Générer des données aléatoires
features, y = make_regression(n_samples=1000, n_features=10, n_informative=5, random_state=42)

# Division des données en ensembles d'entraînement et de test
train_features, test_features, y_train, y_test = train_test_split(features, y, test_size=0.2, random_state=42)

# Initialisation et entraînement du modèle Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(train_features, y_train)

# Prédiction sur l'ensemble de test
y_pred = rf.predict(test_features)

# Calcul de l'erreur quadratique moyenne
mse = np.mean((y_test - y_pred) ** 2)

print("MSE: ", mse)

# Affichage de l'importance des caractéristiques
importances = rf.feature_importances_
std = np.std([tree.feature_importances_ for tree in rf.estimators_], axis=0)
indices = np.argsort(importances)[::-1]
print("Classement des Caractéristiques :")
for f in range(features.shape[1]):
	print(f"{f + 1:d}. feature {indices[f]:d} ({importances[indices[f]]:f})")

# Affichage du graphique des importances des caractéristiques
plt.figure()
plt.title("Importances des Caractéristiques")
plt.bar(range(features.shape[1]), importances[indices], color="r", yerr=std[indices], align="center")
plt.xticks(range(features.shape[1]), [str(index) for index in indices])
plt.xlim(-1, features.shape[1])
plt.show()
