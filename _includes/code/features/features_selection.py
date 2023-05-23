""" Fichier définissant plusieurs fonctions basiques de sélection de features. """

import numpy as np

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel


##################################################
def remove_low_variance_features(X, threshold):
    # Calcule la variance de chaque feature
    variances = np.var(X, axis=0)
    
    # Sélectionne les features avec une variance supérieure au seuil
    selected_features = np.where(variances > threshold)[0]
    
    # Retourne les données avec les features sélectionnées
    return X[:, selected_features]

##################################################
def remove_highly_correlated_features(X, threshold):
    # Calcule la matrice de corrélation
    corr_matrix = pd.DataFrame(X).corr().abs()
    
    # Sélectionne les features non corrélées
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    correlated_features = [column for column in upper.columns if any(upper[column] > threshold)]
    selected_features = [i for i in range(X.shape[1]) if i not in correlated_features]
    
    # Retourne les données avec les features sélectionnées
    return X[:, selected_features]

from sklearn.feature_selection import SelectKBest, f_classif

##################################################
def select_k_best_features(X, y, k):
    # Applique le test ANOVA pour sélectionner les k meilleures features
    selector = SelectKBest(score_func=f_classif, k=k)
    X_new = selector.fit_transform(X, y)
    
    # Retourne les données avec les features sélectionnées
    return X_new


##################################################
def rfe_feature_selection(X, y, n_features):
    # Initialise le modèle de classification
    model = LogisticRegression()
    
    # Sélectionne les n_features meilleures features à l'aide de RFE
    rfe = RFE(estimator=model, n_features_to_select=n_features)
    X_new = rfe.fit_transform(X, y)
    
    # Retourne les données avec les features sélectionnées
    return X_new

##################################################
def feature_importances(X, y, threshold):
	# Appliquer un modèle basé sur des arbres (Random Forest)
	model = RandomForestClassifier()
	model.fit(X, y)
	# Obtenir l'importance des features
	importances = model.feature_importances_
	
	# Sélectionne les features avec une importance supérieure au seuil
	selected_features = np.where(importances > threshold)[0]

	# Retourne les données avec les features sélectionnées
	return X[:, selected_features]

##################################################
def l1_regularization(X, y):
	# Appliquer la régression logistique avec pénalité L1
	model = LogisticRegression(penalty='l1', solver='liblinear')
	model.fit(X, y)

	# Sélectionner les features avec des coefficients non nuls
	sfm = SelectFromModel(model, prefit=True)

	# Retourne les données avec les features sélectionnées
	return sfm.transform(X)

##################################################
# Chargement du jeu de données d'iris
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Variable cible

# Standardisation des features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Features d'origine :", X_scaled.shape[1])

# 1. Variance
threshold = 0.1  # Seuil de variance
X_filtered_variance = remove_low_variance_features(X, threshold)
print("Features après sélection de variance :", X_filtered_variance.shape[1])

# 2. Corrélation
threshold = 0.7  # Seuil de corrélation
X_filtered_correlation = remove_highly_correlated_features(X_scaled, threshold)
print("Features après sélection de corrélation :", X_filtered_correlation.shape[1])

# 3. Univariate Selection (ANOVA)
k = 2  # Nombre de features à sélectionner
X_selected_features = select_k_best_features(X_scaled, y, k)
print("Features sélectionnées par ANOVA :", X_selected_features.shape[1])

# 4. Recursive Feature Elimination (RFE)
n_features = 3  # Nombre de features à sélectionner
X_rfe_features = rfe_feature_selection(X_scaled, y, n_features)
print("Features sélectionnées par RFE :", X_rfe_features.shape[1])

# 5. Feature Importance
threshold = 0.05 # Seuil d'importance des features
X_features_importance = feature_importances(X_scaled, y, threshold)
print("Features sélectionnées par importance :", X_features_importance.shape[1])

# 6. L1 Regularization
X_l1_regularization = l1_regularization(X_scaled, y)
print("Features sélectionnées par L1 Regularization :", X_l1_regularization.shape[1])
