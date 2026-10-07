"""Compare quatre méthodes de mise à l’échelle sur des données avec et sans valeur aberrante."""

import numpy as np
from scipy.stats import iqr

# Jeu de données fictif
data1 = np.array([10, 20, 30, 40, 50])
data2 = np.array([10, 20, 30, 40, 500])  # Avec une valeur aberrante


# Normalisation min-max (mise à l'échelle)
# --------------------------------------------------
def min_max_normalization(data: np.ndarray) -> np.ndarray:
	"""
	Ramène les données entre zéro et un par une transformation min-max.

	:param data: Tableau non constant de valeurs numériques.
	:return: Données mises à l’échelle entre zéro et un.
	"""
	min_val = np.min(data)
	max_val = np.max(data)
	normalized_data = (data - min_val) / (max_val - min_val)
	return normalized_data


# Normalisation z-score (standardisation)
# --------------------------------------------------
def z_score_normalization(data: np.ndarray) -> np.ndarray:
	"""
	Centre les données et les réduit par leur écart-type.

	:param data: Tableau de valeurs numériques dont l’écart-type est non nul.
	:return: Données centrées et réduites.
	"""
	mean = np.mean(data)
	std = np.std(data)
	normalized_data = (data - mean) / std
	return normalized_data


# Normalisation par décimales
# --------------------------------------------------
def decimal_scaling_normalization(data: np.ndarray) -> np.ndarray:
	"""
	Divise les données par une puissance de dix liée à leur amplitude maximale.

	:param data: Tableau de valeurs numériques non toutes nulles.
	:return: Données mises à l’échelle par une puissance de dix.
	"""
	max_val = np.max(np.abs(data))
	scaling_factor = 10 ** (np.ceil(np.log10(max_val)))
	normalized_data = data / scaling_factor
	return normalized_data


# Normalisation robuste


# --------------------------------------------------
def robust_normalization(data: np.ndarray) -> np.ndarray:
	"""
	Centre les données sur leur médiane et les réduit par leur écart interquartile.

	:param data: Tableau de valeurs numériques dont l’écart interquartile est non nul.
	:return: Données centrées et réduites de manière robuste.
	"""
	median = np.median(data)
	iqr_val = iqr(data)
	normalized_data = (data - median) / iqr_val
	return normalized_data


print("Datas 1 : ", data1)
print("    Min-Max Normalization :", min_max_normalization(data1))
print("    Z-Score Normalization :", z_score_normalization(data1))
print("    Decimal Scaling Normalization :", decimal_scaling_normalization(data1))
print("    Robust Normalization :", robust_normalization(data1))

print("Datas 2 : ", data2)
print("    Min-Max Normalization :", min_max_normalization(data2))
print("    Z-Score Normalization :", z_score_normalization(data2))
print("    Decimal Scaling Normalization :", decimal_scaling_normalization(data2))
print("    Robust Normalization :", robust_normalization(data2))
