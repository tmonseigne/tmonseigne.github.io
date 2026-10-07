"""Affiche un spectrogramme Mel et les coefficients cepstraux d’un extrait audio."""

import librosa
import matplotlib.pyplot as plt
import numpy as np

# Ouvrir un signal audio (parmi les exemples librosa)
signal, sampling_rate = librosa.load(librosa.ex("fishin"), duration=120)

mel_spectrogram = librosa.feature.melspectrogram(y=signal, sampling_rate=sampling_rate, n_mels=128, fmax=8000)

# Calcul des coefficients MFCC
mfccs = librosa.feature.mfcc(y=signal, sampling_rate=sampling_rate, n_mfcc=13)

# Tracé des coefficients MFCC
fig, ax = plt.subplots(nrows=2, sharex=True)
img = librosa.display.specshow(librosa.power_to_db(mel_spectrogram, ref=np.max), x_axis="time", y_axis="mel", fmax=8000, ax=ax[0])
fig.colorbar(img, ax=[ax[0]])
ax[0].set(title="Spectrogramme Mel")
ax[0].label_outer()
img = librosa.display.specshow(mfccs, x_axis="time", ax=ax[1])
fig.colorbar(img, ax=[ax[1]])
ax[1].set(title="MFCC")
plt.show()
