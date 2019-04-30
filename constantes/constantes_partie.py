# -*- coding: utf-8 -*-
"""Les listes de constantes concernant les parties
Variables etc.
(A IMPORTER)
Auteur : Le Groupe
"""
# Rappel, None = "vide". (Toujours avec une majuscule)
tps = 30                # Nombre de tick par seconde
ecran = None            # L'écran principal
perso = None            # Le personnage
map = None              # La map
ecran_x = 640           # Largeur de l'écran
ecran_y = 480           # Hauteur de l'écran
centre_x = ecran_x/2    # Coordonnées du milieu de l'écran (Largeur)
centre_y = ecran_y/2    # Coordonnées du milieu de l'écran (Hauteur)
horloge = None          # Destiné à contenir l'objet horloge (pygame)
musique = None          # Variable qui stocke la musique
entites_liste = []      # Liste des entités chargé dans un niveau

# Syntaxe : [coordonnées], [taille_sprite], "type mouvement", vie, attaque
niveau = {
	"niveau_1" : {
		"dragon_rouge" : [
				[[0, 0], [57, 57],"aleatoire", 10, 1],

			],
		"chauve_souris" :[
				[[0, 0], [32, 32],"aleatoire", 10, 1],
			]

		}
}
