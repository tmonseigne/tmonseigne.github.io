import numpy as np
import matplotlib.pyplot as plt

from sklearn.cross_decomposition import CCA

# Générer des données aléatoires
np.random.seed(42)

n_samples = 1000
n_features_1 = 2
n_features_2 = 2

X1 = np.random.rand(n_samples, n_features_1)
X2 = np.random.rand(n_samples, n_features_2)

# Introduire une corrélation entre les deux ensembles de données
X2[:, 0] = 0.8 * X1[:, 0] + 0.2 * X1[:, 1]

# Appliquer l'analyse de corrélation canonique
cca = CCA(n_components=1)
cca.fit(X1, X2)

# Obtenir les scores pour chaque ensemble de données
X1_c, X2_c = cca.transform(X1, X2)

# Tracer les scores pour chaque ensemble de données
plt.scatter(X1_c, X2_c)
plt.xlabel("Scores ensemble de données 1")
plt.ylabel("Scores ensemble de données 2")
plt.show()