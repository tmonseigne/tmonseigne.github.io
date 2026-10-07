"""Compare l’interpolation bilinéaire et bicubique d’une image gaussienne de type PSF."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import RectBivariateSpline, RegularGridInterpolator

# --- Création d'une image PSF 2D (cloche gaussienne) ---
GRID_RADIUS = 2
x = np.linspace(-GRID_RADIUS, GRID_RADIUS, GRID_RADIUS * 3 + 1)
y = np.linspace(-GRID_RADIUS, GRID_RADIUS, GRID_RADIUS * 3 + 1)
x_grid, y_grid = np.meshgrid(x, y, indexing="ij")
image = np.exp(-(x_grid**2 + y_grid**2))  # forme en cloche

# --- Approximation par spline bicubique ---
spline2d = RectBivariateSpline(x, y, image)

# Évaluation sur une grille fine
xfine = np.linspace(-GRID_RADIUS, GRID_RADIUS, GRID_RADIUS * 100)
yfine = np.linspace(-GRID_RADIUS, GRID_RADIUS, GRID_RADIUS * 100)
spline_image = spline2d(xfine, yfine)

# Coefficients spline (pondérations des fonctions de base)
coeffs = spline2d.get_coeffs().reshape(image.shape)

# --- Approximation bilinéaire ---
interp_linear = RegularGridInterpolator((x, y), image, method="linear", bounds_error=False, fill_value=0)
# Grille fine
fine_x_grid, fine_y_grid = np.meshgrid(xfine, yfine, indexing="ij")
pts_fine = np.stack([fine_x_grid.ravel(), fine_y_grid.ravel()], axis=-1)
# Interpolation linéaire
linear_image = interp_linear(pts_fine).reshape(fine_x_grid.shape)

# --- Affichage ---
fig, axs = plt.subplots(1, 3, figsize=(15, 5), constrained_layout=True)

axs[0].imshow(image, extent=(-GRID_RADIUS, GRID_RADIUS, -GRID_RADIUS, GRID_RADIUS), origin="lower", cmap="viridis")
axs[0].set_title("Image 2D (ex: PSF)")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")

axs[1].imshow(coeffs, extent=(-GRID_RADIUS, GRID_RADIUS, -GRID_RADIUS, GRID_RADIUS), origin="lower", cmap="coolwarm")
axs[1].set_title("Coefficients spline $c_{i,j}$")
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")

axs[2].imshow(spline_image, extent=(-GRID_RADIUS, GRID_RADIUS, -GRID_RADIUS, GRID_RADIUS), origin="lower", cmap="viridis")
axs[2].set_title("Approximation spline")
axs[2].set_xlabel("x")
axs[2].set_ylabel("y")

plt.show()

fig, axs = plt.subplots(1, 3, figsize=(15, 5), constrained_layout=True)

axs[0].imshow(image, extent=(-GRID_RADIUS, GRID_RADIUS, -GRID_RADIUS, GRID_RADIUS), origin="lower", cmap="viridis")
axs[0].set_title("Image 2D (ex: PSF)")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")

axs[1].imshow(linear_image, extent=(-GRID_RADIUS, GRID_RADIUS, -GRID_RADIUS, GRID_RADIUS), origin="lower", cmap="viridis")
axs[1].set_title("Approximation linéaire")
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")

axs[2].imshow(spline_image, extent=(-GRID_RADIUS, GRID_RADIUS, -GRID_RADIUS, GRID_RADIUS), origin="lower", cmap="viridis")
axs[2].set_title("Approximation spline")
axs[2].set_xlabel("x")
axs[2].set_ylabel("y")

plt.show()
