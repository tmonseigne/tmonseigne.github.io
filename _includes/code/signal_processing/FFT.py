import numpy as np
import matplotlib.pyplot as plt

# Générer un signal sinusoïdal avec des fréquences précises (10, 25 et 50 Hz)
t = np.linspace(0, 8, 1024)
signal = np.sin(2 * np.pi * 10 * t) + np.sin(2 * np.pi * 25 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)

# Calcul de la transformée de Fourier
fourier_transform = np.fft.fft(signal)

# Calcul des fréquences correspondantes
sampling_rate = 1 / (t[1] - t[0])
freqs = np.fft.fftfreq(len(signal), d=1/sampling_rate)

# Tracé du signal dans le domaine temporel (seulement une seconde)
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.plot(t[:128], signal[:128])
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.title('Signal temporel')

# Tracé du signal dans le domaine fréquentiel
plt.subplot(2, 2, 2)
plt.plot(freqs[:len(freqs)//2], np.abs(fourier_transform[:len(freqs)//2]))
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Amplitude')
plt.title('Transformée de Fourier')

# Tracé de la magnitude de la transformée de Fourier
plt.subplot(2, 2, 3)
plt.plot(freqs[:len(freqs)//2], np.abs(fourier_transform[:len(freqs)//2]))
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Amplitude')
plt.title('Magnitude de la Transformée de Fourier')

# Tracé du spectre de puissance (carré de la magnitude)
plt.subplot(2, 2, 4)
power_spectrum = np.abs(fourier_transform) ** 2
plt.plot(freqs[:len(freqs)//2], power_spectrum[:len(freqs)//2])
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Puissance')
plt.title('Spectre de Puissance')

plt.tight_layout()
plt.show()
