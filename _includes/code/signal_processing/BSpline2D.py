
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RectBivariateSpline, RegularGridInterpolator

# --- Création d'une image PSF 2D (cloche gaussienne) ---
N = 2
x = np.linspace(-N, N, N*3+1)
y = np.linspace(-N, N, N*3+1)
X, Y = np.meshgrid(x, y, indexing='ij')
Z = np.exp(-(X**2 + Y**2))  # forme en cloche

# --- Approximation par spline bicubique ---
spline2d = RectBivariateSpline(x, y, Z)

# Évaluation sur une grille fine
xfine = np.linspace(-N, N, N*100)
yfine = np.linspace(-N, N, N*100)
Z_spline = spline2d(xfine, yfine)

# Coefficients spline (pondérations des fonctions de base)
coeffs = spline2d.get_coeffs().reshape(Z.shape)

# --- Approximation bilinéaire ---
interp_linear = RegularGridInterpolator((x, y), Z, method='linear', bounds_error=False, fill_value=0)
# Grille fine
Xfine, Yfine = np.meshgrid(xfine, yfine, indexing='ij')
pts_fine = np.stack([Xfine.ravel(), Yfine.ravel()], axis=-1)
# Interpolation linéaire
Z_linear = interp_linear(pts_fine).reshape(Xfine.shape)

# --- Affichage ---
fig, axs = plt.subplots(1, 3, figsize=(15, 5), constrained_layout=True)

axs[0].imshow(Z, extent=(-N, N, -N, N), origin='lower', cmap='viridis')
axs[0].set_title("Image 2D (ex: PSF)")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")

axs[1].imshow(coeffs, extent=(-N, N, -N, N), origin='lower', cmap='coolwarm')
axs[1].set_title("Coefficients spline $c_{i,j}$")
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")

axs[2].imshow(Z_spline, extent=(-N, N, -N, N), origin='lower', cmap='viridis')
axs[2].set_title("Approximation spline")
axs[2].set_xlabel("x")
axs[2].set_ylabel("y")

plt.show()

fig, axs = plt.subplots(1, 3, figsize=(15, 5), constrained_layout=True)

axs[0].imshow(Z, extent=(-N, N, -N, N), origin='lower', cmap='viridis')
axs[0].set_title("Image 2D (ex: PSF)")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")

axs[1].imshow(Z_linear, extent=(-N, N, -N, N), origin='lower', cmap='viridis')
axs[1].set_title("Approximation lineaire")
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")

axs[2].imshow(Z_spline, extent=(-N, N, -N, N), origin='lower', cmap='viridis')
axs[2].set_title("Approximation spline")
axs[2].set_xlabel("x")
axs[2].set_ylabel("y")

plt.show()

