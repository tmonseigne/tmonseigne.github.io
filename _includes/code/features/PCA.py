"""Illustre la projection par composantes principales et le choix du nombre de composantes."""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# Chargement des données d'exemple
print("Chargement du jeu de données")
dataset = load_digits()

# Calcul de toutes les composantes principales ; les deux premières servent au graphique.
print("Calcul de l’ACP")
pca = PCA()
pca.fit(dataset.data)

reduced_features = pca.transform(dataset.data)
explained_var = pca.explained_variance_ratio_
cumulative_var = np.cumsum(explained_var)
weights = pca.components_.T  # Vecteurs de chargement des caractéristiques

# Affichage des résultats
print("Affichages")
fig, ax = plt.subplots(figsize=(8, 5))
scatter = ax.scatter(reduced_features[:, 0], reduced_features[:, 1], c=dataset.target, marker="o")
legend = ax.legend(*scatter.legend_elements(), loc="lower left", title="Classes")
ax.add_artist(legend)
ax.set_title("Graphique sur 2 composantes principales")
plt.show()

# Affichage de la variance cumulée
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(range(1, len(cumulative_var) + 1), cumulative_var, marker="o")
ax.set_xlabel("Nombre de composantes principales")
ax.set_ylabel("Ratio de variance expliquée cumulée")
ax.set_title("Graphique du ratio de variance expliquée")

FLATNESS_THRESHOLD = 0.001  # Seuil pour définir la planéité de la courbe
for i in range(1, len(cumulative_var)):
	x1, x2 = range(i - 1, i + 1)
	y1, y2 = cumulative_var[i - 1 : i + 1]
	slope = (y2 - y1) / (x2 - x1)
	if slope < FLATNESS_THRESHOLD:  # dès qu'on passe ce seuil
		tangent_x = np.array([0, len(cumulative_var)])
		tangent_y = slope * (tangent_x - x1) + y1
		ax.plot(tangent_x, tangent_y, linestyle="-", color="red")
		ax.vlines(x2, ymin=cumulative_var[0], ymax=1, linestyle="--", color="red")
		ax.text(x2, cumulative_var[0], f" N = {x2}", ha="left", va="bottom", color="red")
		ax.text(x2, y2 + 0.01, f"Variance = {y2:.3f}", ha="center", va="bottom", color="red")
		break

plt.show()
