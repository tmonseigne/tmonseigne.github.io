import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline, splrep, splev

# 1. Signal brut
x = np.arange(9)
fx = np.array([0, 1, 3, 7, 9, 7, 3, 1, 0])

# 2. Spline cubique
tck = splrep(x, fx, k=3)  # knots, coefficients, degree
spline_curve = splev(np.linspace(0, 8, 400), tck)
knots, coeffs, degree = tck

coeffs = coeffs[:9]

# 3. Calcul des bases B-spline individuelles
basis_x = np.linspace(0, 8, 400)
basis_functions = []
for i in range(len(coeffs)):
    c = np.zeros_like(coeffs)
    c[i] = 1
    b = BSpline(knots, c, degree)
    basis_functions.append(b(basis_x))

# 4. Plot
fig, axs = plt.subplots(3, 1, figsize=(8, 12), constrained_layout=True)
# Plot 1 : signal brut
axs[0].plot(x, fx, 'ko-', label='signal')
axs[0].set_title("Signal brut (discret)")
axs[0].set_xlabel("x")
axs[0].set_ylabel("f(x)")
axs[0].grid(True, linestyle='--', linewidth=0.75)

# Plot 2 : fonctions de base seules
colors = plt.cm.tab10(np.linspace(0, 1, len(coeffs)))
for i, b in enumerate(basis_functions):
    axs[1].plot(basis_x, b, label=f"$B_{{{i}}}(x)$", color=colors[i])
axs[1].set_title("Fonctions de base B-spline $B_i(x)$")
axs[1].set_xlabel("x")
axs[1].set_ylabel("$B_i(x)$")
axs[1].legend(ncol=4, fontsize="small", loc='upper right')
axs[1].grid(True, linestyle='--', linewidth=0.75)

# Plot 3 : combinaison spline
axs[2].plot(basis_x, spline_curve, 'b-', label="approximation spline")
axs[2].plot(np.arange(len(coeffs)), coeffs, 'ro', label="coefficients $c_i$")
axs[2].set_title("Approximation spline et coefficients")
axs[2].set_xlabel("x")
axs[2].set_ylabel("f(x)")
axs[2].grid(True, linestyle='--', linewidth=0.75)
axs[2].legend()
plt.show()

# 4. Plot
fig, axs = plt.subplots(1, 2, figsize=(32, 9), constrained_layout=True)

# Plot 2 : fonctions de base seules
colors = plt.cm.tab10(np.linspace(0, 1, len(coeffs)))
for i, b in enumerate(basis_functions):
    axs[0].plot(basis_x, b, label=f"$B_{{{i}}}(x)$", color=colors[i])
axs[0].set_title("Fonctions de base B-spline $B_i(x)$")
axs[0].set_xlabel("x")
axs[0].set_ylabel("$B_i(x)$")
axs[0].legend(ncol=4, fontsize="small", loc='upper right')
axs[0].grid(True, linestyle='--', linewidth=0.75)

for i, b in enumerate(basis_functions):
    axs[1].plot(basis_x, coeffs[i]*b, label=f"$B_{{{i}}}(x)$", color=colors[i])
axs[1].set_title("Fonctions de base B-spline pondérées $c_i \cdot B_i(x)$")
axs[1].set_xlabel("x")
axs[1].set_ylabel("$B_i(x)$")
axs[1].legend(ncol=4, fontsize="small", loc='upper right')
axs[1].grid(True, linestyle='--', linewidth=0.75)
plt.show()

# 4. Plot
fig, axs = plt.subplots(1, 1, figsize=(16, 9), constrained_layout=True)
axs.plot(x, fx, 'ko--', label='signal', linewidth=0.75)
axs.plot(basis_x, spline_curve, '-', label="approximation spline")
axs.plot(np.arange(len(coeffs)), coeffs, 'o:', label="coefficients $c_i$", linewidth=0.75)
axs.set_title("Approximation spline et coefficients")
axs.set_xlabel("x")
axs.set_ylabel("f(x)")
axs.grid(True, linestyle='--', linewidth=0.75)
axs.legend()
plt.show()