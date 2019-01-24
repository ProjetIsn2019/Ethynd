# -*- coding: utf-8 -*-
"""
Test d'une map de base
"""

import pygame
import os

class Map:
    """Créer une map
    Pour créer des maps directement et facilement
    """
    def __init__(self, nom):
        print("Chargement de " + nom) # Les logs

        self.nom = nom # Stockage du nom
        self.matrice = []
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
        Affiche la map sur l'écran
        """
        for i in range(self.x): # Parcours les colonnes
            for j in range(self.y): # Je parcours les lignes
                if self.matrice[j][i] in self.tuiles: # Si la tuile est connue
                    tuile = self.tuiles[self.matrice[j][i]] # Stocker la tuile
                    ecran.blit(tuile, (32*i, 32*j)) # Afficher la map

    def init_tuiles(self): # Initialiser les tuiles
        """ Initialiser les tuiles
        Important: Toutes les tuiles doivent être déclarés ici.
        """
        os.chdir("images/") # On va dans le répertoire des images
        self.tuiles = {
            "0" : pygame.image.load("rose_test.png").convert_alpha() # Rose test
        }
