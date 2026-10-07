"""Illustre plusieurs méthodes de sélection de caractéristiques sur le jeu de données Iris."""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE, SelectFromModel, SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


# --------------------------------------------------
def remove_low_variance_features(features: np.ndarray, threshold: float) -> np.ndarray:
	"""
	Conserve les caractéristiques dont la variance dépasse le seuil.

	:param features: Matrice des échantillons en lignes et des caractéristiques en colonnes.
	:param threshold: Seuil strict de variance pour conserver une caractéristique.
	:return: Matrice des échantillons limitée aux caractéristiques sélectionnées.
	"""
	# Calcule la variance de chaque caractéristique
	variances = np.var(features, axis=0)

	# Sélectionne les caractéristiques avec une variance supérieure au seuil
	selected_features = np.where(variances > threshold)[0]

	# Retourne les données avec les caractéristiques sélectionnées
	return features[:, selected_features]


# --------------------------------------------------
def remove_highly_correlated_features(features: np.ndarray, threshold: float) -> np.ndarray:
	"""
	Élimine les caractéristiques trop corrélées à une colonne précédente.

	:param features: Matrice des échantillons en lignes et des caractéristiques en colonnes.
	:param threshold: Seuil strict de corrélation absolue entre zéro et un.
	:return: Matrice des échantillons limitée aux caractéristiques sélectionnées.
	"""
	# Calcule la matrice de corrélation
	corr_matrix = pd.DataFrame(features).corr().abs()

	# Sélectionne les caractéristiques non corrélées
	upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
	correlated_features = [column for column in range(features.shape[1]) if any(upper.iloc[:, column] > threshold)]
	selected_features = [i for i in range(features.shape[1]) if i not in correlated_features]

	# Retourne les données avec les caractéristiques sélectionnées
	return features[:, selected_features]


# --------------------------------------------------
def select_k_best_features(features: np.ndarray, labels: np.ndarray, k: int) -> np.ndarray:
	"""
	Sélectionne les meilleures caractéristiques selon le test ANOVA.

	:param features: Matrice des échantillons en lignes et des caractéristiques en colonnes.
	:param labels: Identifiant de classe pour chaque échantillon.
	:param k: Nombre de caractéristiques à conserver.
	:return: Matrice des échantillons limitée aux caractéristiques sélectionnées.
	"""
	# Applique le test ANOVA pour sélectionner les k meilleures caractéristiques
	selector = SelectKBest(score_func=f_classif, k=k)
	selected_features = selector.fit_transform(features, labels)

	# Retourne les données avec les caractéristiques sélectionnées
	return selected_features


# --------------------------------------------------
def rfe_feature_selection(features: np.ndarray, labels: np.ndarray, n_features: int) -> np.ndarray:
	"""
	Sélectionne les caractéristiques par élimination récursive avec une régression logistique.

	:param features: Matrice des échantillons en lignes et des caractéristiques en colonnes.
	:param labels: Identifiant de classe pour chaque échantillon.
	:param n_features: Nombre de caractéristiques à conserver.
	:return: Matrice des échantillons limitée aux caractéristiques sélectionnées.
	"""
	# Initialise le modèle de classification
	model = LogisticRegression()

	# Sélectionne les n_caractéristiques meilleures caractéristiques à l'aide de RFE
	rfe = RFE(estimator=model, n_features_to_select=n_features)
	selected_features = rfe.fit_transform(features, labels)

	# Retourne les données avec les caractéristiques sélectionnées
	return selected_features


# --------------------------------------------------
def feature_importances(features: np.ndarray, labels: np.ndarray, threshold: float) -> np.ndarray:
	"""
	Sélectionne les caractéristiques importantes selon une forêt aléatoire.

	:param features: Matrice des échantillons en lignes et des caractéristiques en colonnes.
	:param labels: Identifiant de classe pour chaque échantillon.
	:param threshold: Seuil strict d’importance pour conserver une caractéristique.
	:return: Matrice des échantillons limitée aux caractéristiques sélectionnées.
	"""
	# Appliquer un modèle basé sur des arbres (Random Forest)
	model = RandomForestClassifier()
	model.fit(features, labels)
	# Obtenir l'importance des caractéristiques
	importances = model.feature_importances_

	# Sélectionne les caractéristiques avec une importance supérieure au seuil
	selected_features = np.where(importances > threshold)[0]

	# Retourne les données avec les caractéristiques sélectionnées
	return features[:, selected_features]


# --------------------------------------------------
def l1_regularization(features: np.ndarray, labels: np.ndarray) -> np.ndarray:
	"""
	Sélectionne les caractéristiques par une régression logistique pénalisée en norme L1.

	:param features: Matrice des échantillons en lignes et des caractéristiques en colonnes.
	:param labels: Identifiant de classe pour chaque échantillon.
	:return: Matrice des échantillons limitée aux caractéristiques sélectionnées.
	"""
	# Appliquer la régression logistique avec pénalité L1
	model = LogisticRegression(penalty="l1", solver="liblinear")
	model.fit(features, labels)

	# Sélectionner les caractéristiques avec des coefficients non nuls
	sfm = SelectFromModel(model, prefit=True)

	# Retourne les données avec les caractéristiques sélectionnées
	return sfm.transform(features)


# --------------------------------------------------
# Chargement du jeu de données d'iris
iris = load_iris()
features = iris.data  # Features
labels = iris.target  # Variable cible

# Standardisation des caractéristiques
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

print("Caractéristiques d'origine :", scaled_features.shape[1])

# 1. Variance
threshold = 0.1  # Seuil de variance
variance_features = remove_low_variance_features(features, threshold)
print("Caractéristiques après sélection de variance :", variance_features.shape[1])

# 2. Corrélation
threshold = 0.7  # Seuil de corrélation
uncorrelated_features = remove_highly_correlated_features(scaled_features, threshold)
print("Caractéristiques après sélection de corrélation :", uncorrelated_features.shape[1])

# 3. Univariate Selection (ANOVA)
k = 2  # Nombre de caractéristiques à sélectionner
anova_features = select_k_best_features(scaled_features, labels, k)
print("Caractéristiques sélectionnées par ANOVA :", anova_features.shape[1])

# 4. Recursive Feature Elimination (RFE)
n_features = 3  # Nombre de caractéristiques à sélectionner
rfe_features = rfe_feature_selection(scaled_features, labels, n_features)
print("Caractéristiques sélectionnées par RFE :", rfe_features.shape[1])

# 5. Feature Importance
threshold = 0.05  # Seuil d'importance des caractéristiques
important_features = feature_importances(scaled_features, labels, threshold)
print("Caractéristiques sélectionnées par importance :", important_features.shape[1])

# 6. L1 Regularization
l1_features = l1_regularization(scaled_features, labels)
print("Caractéristiques sélectionnées par L1 Regularization :", l1_features.shape[1])
