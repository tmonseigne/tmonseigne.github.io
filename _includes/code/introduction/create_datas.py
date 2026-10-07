"""Génère trois signaux d’exemple et les enregistre dans un fichier CSV."""

# Importation des bibliothèques utiles
import numpy as np
import pandas as pd

# Paramètres du signal
DURATION = 60  # 1 minute
SAMPLING_RATE = 32  # 32 Hz
time = np.arange(0, DURATION, 1 / SAMPLING_RATE)

# Créer les signaux
x = np.sin(0.25 * np.pi * time)  # Sinusoïde d'amplitude 1
y = np.zeros(len(time))  # Signal constant nul
z = np.convolve(np.random.randn(len(time)), np.ones(10) / 10, mode="same")  # Bruit Lissé
dataframe = pd.DataFrame({"Temps": time, "x": x, "y": y, "z": z})
dataframe.to_csv("Datas.csv", index=False)
