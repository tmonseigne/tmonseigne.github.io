"""Illustre la classification par analyse discriminante linéaire et sa frontière de décision."""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split

# Générer des données aléatoires
features, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, n_clusters_per_class=1, random_state=42)

# Diviser les données en ensembles d'entraînement et de test
train_features, test_features, y_train, y_test = train_test_split(features, y, test_size=0.2, random_state=42)

# Créer un objet d'analyse discriminante linéaire et entraîner sur les données d'entraînement
lda = LinearDiscriminantAnalysis()
lda.fit(train_features, y_train)

# Prédiction sur l'ensemble de test
y_pred = lda.predict(test_features)

# Calcul de la précision
accuracy = np.mean(y_pred == y_test)
print("Exactitude :", accuracy)

# Tracé des données d'entraînement et de test
fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(train_features[:, 0], train_features[:, 1], c=y_train)
handles, labels = scatter.legend_elements()
ax.legend(handles, ["Classe 0", "Classe 1"])
plt.xlabel("Caractéristique 1")
plt.ylabel("Caractéristique 2")
plt.title("Données d'entraînement")

# Tracé des frontières de décision
x_min, x_max = train_features[:, 0].min() - 0.5, train_features[:, 0].max() + 0.5
y_min, y_max = train_features[:, 1].min() - 0.5, train_features[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
predicted_labels = lda.predict(np.c_[xx.ravel(), yy.ravel()])
predicted_labels = predicted_labels.reshape(xx.shape)
ax.contourf(xx, yy, predicted_labels, alpha=0.2)
plt.show()
