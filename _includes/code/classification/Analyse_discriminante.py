import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Générer des données aléatoires
X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, n_clusters_per_class=1, random_state=42)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer un objet d'analyse discriminante linéaire et entraîner sur les données d'entraînement
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)

# Prédiction sur l'ensemble de test
y_pred = lda.predict(X_test)

# Calcul de la précision
accuracy = np.mean(y_pred == y_test)
print("Precision :", accuracy)

# Tracé des données d'entraînement et de test
fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
handles, labels = scatter.legend_elements()
ax.legend(handles, ['Classe 0', 'Classe 1'])
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Données d'entraînement")

# Tracé des frontières de décision
x_min, x_max = X_train[:, 0].min() - 0.5, X_train[:, 0].max() + 0.5
y_min, y_max = X_train[:, 1].min() - 0.5, X_train[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
Z = lda.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
ax.contourf(xx, yy, Z, alpha=0.2)
plt.show()