""" Petit exemple python de lecture et affichage d'un signal sur 3 axes """

# Importation des bibliothèques utiles
import matplotlib.pyplot as plt	 # Bibliothèque pour l'affichage de graphique
import numpy as np				 # Bibliothèque pour le calcul
import pandas as pd				 # Bibliothèque pour la manipulation de tableaux avec en-tête et la gestion de fichiers type tableurs

#################### Traitement des données ####################
# Charger le fichier CSV dans un DataFrame
mon_fichier = "Datas.csv"			# On définit le chemin vers le fichier
data = pd.read_csv(mon_fichier)		# On ouvre le fichier avec pandas
print(data)							# On affiche le résultat

# Récupération du temps minimum et maximum
t_min = data["Temps"].iloc[0]		# On prend la première valeur de la colonne temps
t_max = data["Temps"].iloc[-1]		# On prend la dernière valeur de la colonne temps

# Calculer la magnitude racine de la somme des axes au carré
magnitude = np.sqrt(data["x"] ** 2 + data["y"] ** 2 + data["z"] ** 2)

#################### Affichage ####################
# Créer une figure pour afficher les graphiques
fig, axes = plt.subplots(4, 1, figsize=(16, 9), dpi=200)	# Création de notre canevas de figures de 4 lignes et 1 colonnes
axes = axes.ravel()											# Au lieu d'avoir un tableau de figures 2D, on prend un tableau 1D.

# Afficher les données des trois axes
axes[0].plot(data["Temps"], data["x"])						# Sur la première figure, on affiche l'axe X par rapport au temps
axes[0].set_title("Accélération sur l'axe X")				# On affiche le titre de cette figure
axes[0].set_xlabel("Temps (s)")								# On indique le titre de l'abscisse
axes[0].set_ylabel("Accélération (m/s²)")					# On indique le titre de l'ordonnée
axes[0].set_xlim(t_min, t_max)								# On définit le min et max de l'abscisse (pour éviter un petit blanc avant et après la courbe)

axes[1].plot(data["Temps"], data["y"])						# Sur la seconde figure, on affiche l'axe Y par rapport au temps
axes[1].set_title("Accélération sur l'axe Y")				# On affiche le titre de cette figure
axes[1].set_xlabel("Temps (s)")								# On indique le titre de l'abscisse
axes[1].set_ylabel("Accélération (m/s²)")					# On indique le titre de l'ordonnée
axes[1].set_xlim(t_min, t_max)								# On définit le min et max de l'abscisse (pour éviter un petit blanc avant et après la courbe)

axes[2].plot(data["Temps"], data["z"])						# Sur la troisième figure, on affiche l'axe Z par rapport au temps
axes[2].set_title("Accélération sur l'axe Z")				# On affiche le titre de cette figure
axes[2].set_xlabel("Temps (s)")								# On indique le titre de l'abscisse
axes[2].set_ylabel("Accélération (m/s²)")					# On indique le titre de l'ordonnée
axes[2].set_xlim(t_min, t_max)								# On définit le min et max de l'abscisse (pour éviter un petit blanc avant et après la courbe)

axes[3].plot(data["Temps"], magnitude, color='r')			# Sur la quatrième figure, on affiche la magnitude par rapport au temps
axes[3].set_title("Magnitude de l'accélération")			# On affiche le titre de cette figure
axes[3].set_xlabel("Temps (s)")								# On indique le titre de l'abscisse
axes[3].set_ylabel("Magnitude (m/s²)")						# On indique le titre de l'ordonnée
axes[3].set_xlim(t_min, t_max)								# On définit le min et max de l'abscisse (pour éviter un petit blanc avant et après la courbe)

# Afficher tous les graphiques
plt.tight_layout()											# On réduit les marges, c'est moche
plt.show()													# On affiche notre figure