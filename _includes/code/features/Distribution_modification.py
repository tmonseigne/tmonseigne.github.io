"""Compare des transformations de distributions simulées et enregistre leurs graphiques."""

import os
from collections.abc import Callable
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.axes import Axes
from scipy import stats


# --------------------------------------------------
def set_failed(ax: Axes, title: str):
	"""
	Signale graphiquement l’échec d’une transformation.

	:param ax: Sous-graphique dans lequel afficher le message.
	:param title: Titre de la transformation concernée.
	"""
	ax.set_title(title)
	ax.text(0.5, 0.5, "Failed", fontsize=40, ha="center", va="center", bbox={"facecolor": "red", "edgecolor": "none", "pad": 10}, color="white")


# --------------------------------------------------
def cub(data: np.ndarray) -> np.ndarray:
	"""
	Élève chaque valeur des données au cube.

	:param data: Tableau de valeurs numériques.
	:return: Cube de chaque valeur.
	"""
	return data**3


# --------------------------------------------------
def inv(data: np.ndarray) -> np.ndarray:
	"""
	Calcule l’inverse de chaque valeur des données.

	:param data: Tableau de valeurs numériques non nulles.
	:return: Inverse de chaque valeur.
	"""
	return 1 / data


# --------------------------------------------------
def standard(data: np.ndarray) -> np.ndarray:
	"""
	Centre les données et les réduit par leur écart-type.

	:param data: Tableau de valeurs numériques dont l’écart-type est non nul.
	:return: Données centrées et réduites.
	"""
	return (data - np.mean(data)) / np.std(data)


# --------------------------------------------------
path = os.path.join(os.path.dirname(__file__), "Figures")
os.makedirs(path, exist_ok=True)  # Créer le dossier des figures (la première fois, il n'existe pas)

np.random.seed(0)
SAMPLE_COUNT = 10000

# Partie des fonctions de distribution possible avec NumPy
functions: list[tuple[str, np.ndarray]] = [
	("Beta Distribution", np.random.beta(1, 1, SAMPLE_COUNT)),
	("Chi-square Distribution", np.random.chisquare(2, SAMPLE_COUNT)),
	("Exponential Distribution", np.random.exponential(1, SAMPLE_COUNT)),
	("F Distribution", np.random.f(1, 48, SAMPLE_COUNT)),
	("Gamma Distribution", np.random.gamma(2, 2, SAMPLE_COUNT)),
	("Gumbel Distribution", np.random.gumbel(0, 0.1, SAMPLE_COUNT)),
	("Laplace Distribution", np.random.laplace(0, 1, SAMPLE_COUNT)),
	("Logistic Distribution", np.random.logistic(10, 1, SAMPLE_COUNT)),
	("Log-normal Distribution", np.random.lognormal(3, 1, SAMPLE_COUNT)),
	("Negative binomial Distribution", np.random.negative_binomial(1, 0.1, SAMPLE_COUNT)),
	("Noncentral chi-square Distribution", np.random.noncentral_chisquare(3, 20, SAMPLE_COUNT)),
	("Noncentral F Distribution", np.random.noncentral_f(3, 20, 3, SAMPLE_COUNT)),
	("Normal (Gaussian) Distribution", np.random.normal(0, 1, SAMPLE_COUNT)),
	("Power Distribution", np.random.power(5, SAMPLE_COUNT)),
	("Rayleigh Distribution", np.random.rayleigh(3, SAMPLE_COUNT)),
	("Triangular Distribution", np.random.triangular(-3, 0, 8, SAMPLE_COUNT)),
	("Von Mises Distribution", np.random.vonmises(0, 4, SAMPLE_COUNT)),
	("Wald, or inverse Gaussian, Distribution", np.random.wald(3, 2, SAMPLE_COUNT)),
	("Weibull Distribution", np.random.weibull(5, SAMPLE_COUNT)),
]

# Les transformations renvoient un tableau, ou un couple tableau/lambda pour Box-Cox.
transformations: list[tuple[str, Callable[..., Any]]] = [
	("Transformation logarithmique", np.log),
	("Transformation Exponentielle", np.exp),
	("Transformation de Box-Cox", stats.boxcox),
	("Standardisation", standard),
	("Transformation des rangs", stats.rankdata),
	("Transformation racine carrée", np.sqrt),
	("Transformation de puissance cubique", cub),
	("Transformation de puissance inverse", inv),
]

# --------------------------------------------------
for f in functions:
	print(f[0])
	# Génération de données
	data = f[1]

	# Création de sous-graphiques
	fig, axes = plt.subplots(3, 3, figsize=(16, 10))
	axes = axes.ravel()

	# Distribution d'origine
	sns.histplot(data, kde=True, ax=axes[0])
	k, s = np.round(stats.kurtosis(data), 2), np.round(stats.skew(data), 2)
	axes[0].set_title(f"{f[0]} (k={k}, s={s})")
	normal_data = np.random.normal(np.mean(data), np.std(data), SAMPLE_COUNT)
	sns.histplot(normal_data, kde=True, ax=axes[0])
	axes[0].legend(["Datas", "Normal"], title="Distribution")

	plt.show()

	i = 1
	for t in transformations:
		try:
			if t[0] == "Transformation de Box-Cox":
				transformed, lambda_ = t[1](data)
				lambda_value, k, s = np.round(lambda_, 2), np.round(stats.kurtosis(transformed), 2), np.round(stats.skew(transformed), 2)
				if np.isnan(lambda_value) or np.isnan(k) or np.isnan(s):
					set_failed(axes[i], t[0])
					i += 1
					continue
				axes[i].set_title(f"Transformation de Box-Cox (lambda={lambda_value}, k={k}, s={s})")
			else:
				transformed = t[1](data)
				k, s = np.round(stats.kurtosis(transformed), 2), np.round(stats.skew(transformed), 2)
				if np.isnan(k) or np.isnan(s):
					set_failed(axes[i], t[0])
					i += 1
					continue
				axes[i].set_title(f"{t[0]} (k={k}, s={s})")

			sns.kdeplot(transformed, ax=axes[i])
		except ValueError:
			set_failed(axes[i], t[0])
			i += 1
			continue

		normal_data = np.random.normal(np.mean(transformed), np.std(transformed), SAMPLE_COUNT)
		sns.kdeplot(normal_data, ax=axes[i])
		axes[i].legend(["Datas", "Normal"], title="Distribution")
		i += 1

	# Ajustement des espacements entre les sous-graphiques
	plt.tight_layout()
	plt.savefig(os.path.join(path, f"{f[0]}.png"), bbox_inches="tight")
