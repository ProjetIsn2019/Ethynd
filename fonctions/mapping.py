# -*- coding: utf-8 -*-
"""Les maps
Objet "Map" qui correspond a une carte de tuiles.
Auteur: Sofiane
"""

import pygame
import os

class Map:
    """Créer une map
    Pour créer des maps directement et facilement
    """
    def __init__(self, nom, couleur_fond = (10,10,10)):
        print("Chargement de " + nom) # Les logs

        self.couleur_fond = couleur_fond
        self.nom = nom # Stockage du nom
        self.matrice = [] # Matrice qui stockera la map
        fichier = open(nom, "r")  # Ouvrir le fichier map

        for ligne in fichier.readlines():  # Je regarde chaque lignes
            compteur = 0 # Compteur de lignes

            ligne = ligne.split() # On convertis la ligne en liste
            # Split permets de supprimer les espaces inutiles

            if ligne != []: # Si la ligne en liste n'est pas nulle
                self.matrice.append(ligne)  # On ajoute la ligne en liste

            compteur += 1 # On ajoute 1 ligne au compteur car on l'a lu

        fichier.close() # Fermer fichier

        self.x = len(self.matrice[0])  # Nombre de colonnes
        self.y = len(self.matrice)  # Nombre de lignes

        self.init_tuiles() # Initialisation des tuiles

        print(nom + " chargé!") # Logs


    def afficher(self, ecran):
        """ Affiche la map
        Affiche la map sur l'écran par rapport a un point
        Le point est sur 0,0 par défaut.
        """

        # Je capture les dimensions de la fenêtre actuelle
        l, h = ecran.get_width(), ecran.get_height()  # l = largeur
                                                      # h = hauteur
        # Je calcule les points centraux (moyenne)
        x_centre = l/2  # Le x central
        y_centre = h/2  # Le y central

        # Je calcule le point de départ pour le rendu de la map
        # Formule:    Point - Nb tuiles_map * 16 / 2
        # Simplifiée: Point - Nb_tuiles_map * 8
        x_rendu = x_centre - self.x * 8
        y_rendu = y_centre - self.y * 8

        for i in range(self.x): # Parcours les colonnes
            for j in range(self.y): # Je parcours les lignes
                if self.matrice[j][i] in self.tuiles: # Si la tuile est connue
                    tuile = self.tuiles[self.matrice[j][i]] # Stocker la tuile
                    ecran.blit(tuile, (x_rendu + 16*i,  # Tuile par tuile
                                       y_rendu + 16*j)) # Afficher la map


    def init_tuiles(self): # Initialiser les tuiles
        """ Initialiser les tuiles
        Important: Toutes les tuiles doivent être déclarés ici.
        """
        print("Chargement des tuiles...") # Logs
        self.tuiles = {} # Dictionnaire des tuiles
        for fichier in os.listdir("images/tuiles/"): # Je parcours les tuiles
            nom = fichier.replace("tuile_", "") # On supprime le prefix
            nom = nom.replace(".png", "")       # On supprime l'extension
            fichier = "images/tuiles/" + fichier # Ajout du chemin relatif
            # J'ajoute les tuiles au dictionnaire
            self.tuiles[nom] = pygame.image.load(fichier).convert_alpha()
