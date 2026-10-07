"""Compare le suréchantillonnage, le sous-échantillonnage et leur combinaison sur des classes déséquilibrées."""

import matplotlib.pyplot as plt
import numpy as np
from imblearn.combine import SMOTEENN
from imblearn.over_sampling import ADASYN
from imblearn.under_sampling import RandomUnderSampler
from sklearn.datasets import make_classification
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Création du jeu de données déséquilibré
features, y = make_classification(
	n_samples=300, n_features=2, n_informative=2, n_redundant=0, n_classes=3, n_clusters_per_class=1, weights=[0.8, 0.15, 0.05], random_state=42
)
datasets = [{"title": "Original", "x": features, "y": y}]

# Oversampling avec ADASYN
ada = ADASYN(random_state=42)
X_ada, y_ada = ada.fit_resample(features, y)
datasets.append({"title": "Sur-Echantillonnage (ADASYN)", "x": X_ada, "y": y_ada})

# Undersampling avec RandomUnderSampler
rus = RandomUnderSampler(random_state=42)
X_rus, y_rus = rus.fit_resample(features, y)
datasets.append({"title": "Sous-Echantillonnage (RandomUnderSampler)", "x": X_rus, "y": y_rus})

# Ensemble avec SMOTEENN
smn = SMOTEENN(random_state=42)
X_smn, y_smn = smn.fit_resample(features, y)
datasets.append({"title": "Technique d'ensemble (SMOTEENN)", "x": X_smn, "y": y_smn})

# Affichages
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Comparaison des techniques d'échantillonnage", fontsize=16)

# Préparation du LDA (pour afficher les zones sur les figures)
lda = LinearDiscriminantAnalysis()
x_min, x_max = features[:, 0].min() - 1, features[:, 0].max() + 1
y_min, y_max = features[:, 1].min() - 1, features[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

for i in range(4):
	a_i, a_j = i // 2, i % 2
	lda.fit(datasets[i]["x"], datasets[i]["y"])
	predicted_labels = lda.predict(np.c_[xx.ravel(), yy.ravel()])
	predicted_labels = predicted_labels.reshape(xx.shape)
	axes[a_i, a_j].contourf(xx, yy, predicted_labels, alpha=0.2)
	axes[a_i, a_j].scatter(datasets[i]["x"][:, 0], datasets[i]["x"][:, 1], c=datasets[i]["y"])
	axes[a_i, a_j].set_title(datasets[i]["title"])

plt.tight_layout()
plt.show()
