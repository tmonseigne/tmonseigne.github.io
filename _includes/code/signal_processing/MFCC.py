import numpy as np
import matplotlib.pyplot as plt
import librosa

# Ouvrir un signal audio (parmi les exemples librosa)
signal, sr = librosa.load(librosa.ex('fishin'), duration=120)

S = librosa.feature.melspectrogram(y=signal, sr=sr, n_mels=128, fmax=8000)

# Calcul des coefficients MFCC
mfccs = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=13)

# Tracé des coefficients MFCC
fig, ax = plt.subplots(nrows=2, sharex=True)
img = librosa.display.specshow(librosa.power_to_db(S, ref=np.max), x_axis='time', y_axis='mel', fmax=8000, ax=ax[0])
fig.colorbar(img, ax=[ax[0]])
ax[0].set(title='Mel spectrogram')
ax[0].label_outer()
img = librosa.display.specshow(mfccs, x_axis='time', ax=ax[1])
fig.colorbar(img, ax=[ax[1]])
ax[1].set(title='MFCC')
plt.show()