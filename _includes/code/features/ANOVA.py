"""Compare les caractéristiques des espèces d’iris par analyse de variance à un facteur."""

from scipy.stats import f_oneway
from sklearn.datasets import load_iris

# Chargement du jeu de données Iris
iris = load_iris()
features = iris.data
y = iris.target

# Séparation des données par classe d'espèce d'iris
X_setosa = features[y == 0]
X_versicolor = features[y == 1]
X_virginica = features[y == 2]

# Application de l'ANOVA sur les caractéristiques
anova_results = []

for i in range(features.shape[1]):
	feature_anova = [X_setosa[:, i], X_versicolor[:, i], X_virginica[:, i]]
	_, p_value = f_oneway(*feature_anova)
	anova_results.append(p_value)

# Affichage des résultats
for i, feature_name in enumerate(iris.feature_names):
	print(f"Caractéristique : {feature_name}, p-value : {anova_results[i]}")
