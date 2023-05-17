import numpy as np
import matplotlib.pyplot as plt
import pywt

# Générer un signal sinusoïdal avec des fréquences précises (10, 25 et 50 Hz)
t = np.linspace(0, 1, 1024)
signal = np.sin(2 * np.pi * 10 * t) + np.sin(2 * np.pi * 25 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)

# Décomposition en ondelettes
coeffs = pywt.wavedec(signal, 'db4', level=4)

# Tracé du signal dans le domaine temporel
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.title('Signal temporel')

# Tracé des coefficients d'ondelettes
plt.subplot(2, 1, 2)
for i, c in enumerate(coeffs):
    plt.plot(np.linspace(0, 1, len(c)), c, label=f'Niveau {i+1}')
plt.legend()
plt.xlabel('Temps')
plt.ylabel('Coefficient')
plt.title('Décomposition en ondelettes')
plt.tight_layout()
plt.show()
