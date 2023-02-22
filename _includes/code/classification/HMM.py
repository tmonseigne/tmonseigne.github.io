from hmmlearn import hmm
import numpy as np
import matplotlib.pyplot as plt

# Génération de données aléatoires
np.random.seed(42)
states = ["pluie", "nuageux", "soleil"]
n_states = len(states)
observations = ["parapluie", "lunettes de soleil"]
n_observations = len(observations)
start_probability = np.array([0.6, 0.3, 0.1])
transition_probability = np.array([
  [0.7, 0.2, 0.1],
  [0.3, 0.5, 0.2],
  [0.2, 0.3, 0.5]
])
emission_probability = np.array([
  [0.1, 0.9],
  [0.6, 0.4],
  [0.9, 0.1]
])
model = hmm.MultinomialHMM(n_components=n_states)
model.startprob_ = start_probability
model.transmat_ = transition_probability
model.emissionprob_ = emission_probability

# Prédiction d'une séquence d'observations
X = np.array([[0, 1, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 0, 0, 1, 0, 0, 0]]).T
lengths = [len(X)]  # nombre d'observations pour chaque séquence
model.fit(X, lengths=lengths)
logprob, hidden_states = model.decode(X, algorithm="viterbi")
print("Sequence d'etats caches predite :", [states[i] for i in hidden_states])

# Création de l'automate correspondant au modèle
fig, ax = plt.subplots()
plt.title("Automate de l'HMM")
plt.xlabel("Temps")
plt.ylabel("État")
plt.imshow(model.transmat_, cmap="Blues", interpolation="nearest")
plt.colorbar()

# Ajout des labels pour les états et transitions
for i in range(n_states):
    for j in range(n_states):
        ax.text(j, i, f"{model.transmat_[i, j]:.2f}", ha="center", va="center", color="white")
        if i == 0:
            ax.text(j, i-0.4, states[j], ha="center", va="top", color="black")
        if j == 0:
            ax.text(j-0.3, i, states[i], ha="right", va="center", color="black")

plt.show()