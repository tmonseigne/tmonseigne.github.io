import os

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

##################################################
def set_failed(ax, title):
    ax.set_title(title)
    ax.text(0.5, 0.5, "Failed", fontsize=40, ha='center', va='center', bbox=dict(facecolor='red', edgecolor='none', pad=10), color='white')

def cub(data): return data ** 3
def inv(data): return 1 / data
def standard(data): return (data - np.mean(data)) / np.std(data)

##################################################
path = os.path.join(os.path.dirname(__file__), "Figures")
os.makedirs(path, exist_ok=True)  # Créer le dossier de samples (la première fois, il n'existe pas)

np.random.seed(0)
N = 10000

# Partie des fonctions de distribution possible avec Numpy
functions = [
        ("Beta Distribution", np.random.beta(1, 1, N)),
        ("Chi-square Distribution", np.random.chisquare(2, N)),
        ("Exponential Distribution", np.random.exponential(1, N)),
        ("F Distribution", np.random.f(1, 48, N)),
        ("Gamma Distribution", np.random.gamma(2, 2, N)),
        ("Gumbel Distribution", np.random.gumbel(0, 0.1, N)),
        ("Laplace Distribution", np.random.laplace(0, 1, N)),
        ("Logistic Distribution", np.random.logistic(10, 1, N)),
        ("Log-normal Distribution", np.random.lognormal(3, 1, N)),
        ("Negative binomial Distribution", np.random.negative_binomial(1, 0.1, N)),
        ("Noncentral chi-square Distribution", np.random.noncentral_chisquare(3, 20, N)),
        ("Noncentral F Distribution", np.random.noncentral_f(3, 20, 3, N)),
        ("Normal (Gaussian) Distribution", np.random.normal(0, 1, N)),
        ("Power Distribution", np.random.power(5, N)),
        ("Rayleigh Distribution", np.random.rayleigh(3, N)),
        ("Triangular Distribution", np.random.triangular(-3, 0, 8, N)),
        ("Von Mises Distribution", np.random.vonmises(0, 4, N)),
        ("Wald, or inverse Gaussian, Distribution", np.random.wald(3, 2, N)),
        ("Weibull Distribution", np.random.weibull(5, N))
        ]

transformations = [
        ("Transformation logarithmique", np.log), ("Transformation Exponentielle", np.exp),
        ("Transformation de Box-Cox", stats.boxcox), ("Standardisation", standard),
        ("Transformation des rangs", stats.rankdata), ("Transformation de puissance carrée", np.sqrt),
        ("Transformation de puissance cubique", cub), ("Transformation de puissance inverse", inv)
        ]

##################################################
for f in functions:
    print(f[0])
    # Génération de données
    data = f[1]

    # Création de sous-plots
    fig, axes = plt.subplots(3, 3, figsize=(16, 10))
    axes = axes.ravel()

    # Distribution d'origine
    sns.histplot(data, kde=True, ax=axes[0])
    k, s = np.round(stats.kurtosis(data), 2), np.round(stats.skew(data), 2)
    axes[0].set_title(f"{f[0]} (k={k}, s={s})")
    normal_data = np.random.normal(np.mean(data), np.std(data), N)
    sns.histplot(normal_data, kde=True, ax=axes[0])
    axes[0].legend(["Datas", "Normal"], title="Distribution")

    plt.show()

    i = 1
    for t in transformations:
        try:
            if t[0] == "Transformation de Box-Cox":
                transformed, lambda_ = t[1](data)
                l, k, s = np.round(lambda_, 2), np.round(stats.kurtosis(transformed), 2), np.round(stats.skew(transformed), 2)
                if np.isnan(l) or np.isnan(k) or np.isnan(s):
                    set_failed(axes[i], t[0])
                    i += 1
                    continue
                axes[i].set_title(f"Transformation de Box-Cox (lambda={l}, k={k}, s={s})")
            else:
                transformed = t[1](data)
                k, s = np.round(stats.kurtosis(transformed), 2), np.round(stats.skew(transformed), 2)
                if np.isnan(k) or np.isnan(s):
                    set_failed(axes[i], t[0])
                    i += 1
                    continue
                axes[i].set_title(f"{t[0]} (k={k}, s={s})")

            sns.kdeplot(transformed, ax=axes[i])
        except ValueError as e:
            set_failed(axes[i], t[0])
            i += 1
            continue

        normal_data = np.random.normal(np.mean(transformed), np.std(transformed), N)
        sns.kdeplot(normal_data, ax=axes[i])
        axes[i].legend(["Datas", "Normal"], title="Distribution")
        i += 1

    # Ajustement des espacements entre les sous-graphiques
    plt.tight_layout()
    plt.savefig(os.path.join(path, f"{f[0]}.png"), bbox_inches="tight")
