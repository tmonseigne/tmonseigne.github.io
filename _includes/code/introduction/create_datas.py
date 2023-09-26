""" Petit exemple python de créations de données et enregistremenbt dans un csv """

# Importation des bibliothèques utiles
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Paramètres du signal
duree = 60  # 1 minute
frequence = 32  # 32 Hz
temps = np.arange(0, duree, 1 / frequence)

# Créer les signaux
x = np.sin(0.25 * np.pi * temps)  # Sinusoïde d'amplitude 1
y = np.zeros(len(temps))  # Constante à 1
z = np.convolve(np.random.randn(len(temps)), np.ones(10)/10, mode='same')  # Bruit Lissé
dataframe = pd.DataFrame({'Temps': temps, 'x': x, 'y': y, 'z': z})
dataframe.to_csv("Datas.csv", index=False)