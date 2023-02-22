import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Générer des données aléatoires
np.random.seed(42)
x1 = np.random.rand(100)
x2 = 0.5 * x1 + np.random.normal(0, 0.03, size=100)
x3 = 0.8 * x2 + np.random.normal(0, 0.05, size=100)
y = 2 * x1 + 3 * x2 + 4 * x3 + np.random.normal(0, 0.1, size=100)

# Regroupement de l'ensemble de données en une seule matrice
X = np.column_stack((x1, x2, x3))

# Élimination des colonnes redondantes en utilisant la décomposition QR (éviter qu'une colonne soit juste une combinaison lineaire des autres colonnes)
q, r = np.linalg.qr(X)
r_diag = np.abs(np.diag(r))
tol = r_diag.max() * X.shape[1] * np.finfo(r_diag.dtype).eps
X = X[:, r_diag > tol]

# Ajout d'une colonne de biais à X
X_b = np.c_[np.ones((100, 1)), X]

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X_b, y, test_size=0.2, random_state=42)

# Calcul des poids de la régression linéaire par système linéaire
weights = np.linalg.inv(X_train.T.dot(X_train)).dot(X_train.T).dot(y_train)

# Prédiction sur l'ensemble de test
y_pred = X_test.dot(weights)

# Calcul de l'erreur quadratique moyenne
mse = np.mean((y_test - y_pred)**2)

print("MSE:", mse)

# Tracer les valeurs prédites par rapport aux vraies valeurs
plt.scatter(y_test, y_pred)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--')
plt.xlabel('Vraies valeurs')
plt.ylabel('Valeurs prédites')
plt.show()