# -*- coding: utf-8 -*-
"""Les maps
Objet "Map" qui correspond a une carte de tuiles.
Auteur: Sofiane
"""
import pygame as pg
import os


class Map:
    """Créer une map
    Pour créer des maps directement et facilement (Un outil)
    Permets de:
    - Charger une map (Avec 4 couches de tuiles)
    - Afficher une map (Avec les 4 couches de tuiles)
    ++ Support transparence.
    """

    def __init__(self, nom, couleur_fond=(40, 38, 51)):
        self.couleur_fond = couleur_fond
        self.matrices = {
            0: [],  # Matrice qui stockera le fond
            1: [],  # Matrice qui stockera le milieu
            2: [],  # Matrice qui stockera le 1er plan
            3: []   # Matrice qui stockera le plan spécial
        }
        for i in range(4):  # On a 4 calques, ici on parcours les calques
            nom_fichier = nom + "_" + str(i) + ".csv"  # Nom du fichier
            #                                          # Ex: nom_0.csv
            print("Chargement de", nom_fichier + "...")  # Les logs
            f = open(nom_fichier, "r")    # Ouvrir le fichier
            for ligne in f.readlines():   # Je regarde chaque lignes
                ligne = ligne.replace("\n", "")  # Je supprime les \n
                ligne = ligne.split(",")  # On convertis la ligne en liste
                if ligne != []:  # Si la ligne en liste n'est pas nulle
                    self.matrices[i].append(ligne)  # On ajoute la liste
            f.close()  # Fermer fichier

        # Pour le nombre de colonnes et de lignes on utilise la matrice du fond
        self.x = len(self.matrices[0][0])  # Nombre de colonnes
        self.y = len(self.matrices[0])     # Nombre de lignes
        self.init_tuiles()  # Initialisation des tuiles

    def afficher(self, ecran):
        """ Affiche la map
        Affiche la map sur l'écran par rapport a un point
        Le point est sur 0,0 par défaut.
        """

        # Je capture les dimensions de la fenêtre actuelle
        l, h = ecran.get_width(), ecran.get_height()  # l = largeur
        #                                             # h = hauteur
        # Je calcule les points centraux (moyenne)
        x_centre = l/2  # Le x central
        y_centre = h/2  # Le y central

        # Je calcule le point de départ pour le rendu de la map
        # Formule:    Point - Nb tuiles_map * 32 / 2
        # Simplifiée: Point - Nb_tuiles_map * 16
        x_rendu = x_centre - self.x * 16
        y_rendu = y_centre - self.y * 16

        for i in range(3):  # Je parcours les couches
            for x in range(self.x):  # Parcours les colonnes
                for y in range(self.y):  # Je parcours les lignes
                    # En parcourant les 3 dimensions, on parcours toutes
                    # les tuiles. Voilà ce qu'on va faire avec:
                    if self.matrices[i][y][x] in self.tuiles:  # Si elle existe
                        tuile = self.tuiles[self.matrices[i][y][x]]  # On save
                        ecran.blit(tuile, (x_rendu + 32*x,   # On affiche
                                           y_rendu + 32*y))  # Tuile par tuile

    def afficher_4eme_couche(self, ecran):
        """ Affiche la couche transparente de la map
        Destinée a être utilisée après l'affichage du personnage.
        """

        # Je capture les dimensions de la fenêtre actuelle
        l, h = ecran.get_width(), ecran.get_height()  # l = largeur
        #                                             # h = hauteur
        # Je calcule les points centraux (moyenne)
        x_centre = l/2  # Le x central
        y_centre = h/2  # Le y central

        # Je calcule le point de départ pour le rendu de la map
        # Formule:    Point - Nb tuiles_map * 32 / 2
        # Simplifiée: Point - Nb_tuiles_map * 16
        x_rendu = x_centre - self.x * 16
        y_rendu = y_centre - self.y * 16

        for x in range(self.x):  # Parcours les colonnes
            for y in range(self.y):  # Je parcours les lignes
                # En parcourant les 3 dimensions, on parcours toutes
                # les tuiles. Voilà ce qu'on va faire avec:
                if self.matrices[3][y][x] in self.tuiles:  # Si elle existe
                    tuile = self.tuiles[self.matrices[3][y][x]]  # On save
                    ecran.blit(tuile, (x_rendu + 32*x,   # On affiche
                                       y_rendu + 32*y))  # Tuile par tuile

    def init_tuiles(self):
        """ Initialiser les tuiles
        """
        print("Chargement des tuiles...")  # Logs
        self.tuiles = {}  # Dictionnaire des tuiles
        for fichier in os.listdir("images/tuiles/"):  # Je parcours les tuiles
            nom = fichier.replace("tuile_", "")   # On supprime le prefix
            nom = nom.replace(".png", "")         # On supprime l'extension

            # On supprime les 0 au début si le nom n'est pas "000"
            # Si c'est le cas alors on retourne 0. Donc "000" = "0"
            nom = nom.lstrip("0") if nom != "000" else "0"
            fichier = "images/tuiles/" + fichier  # Ajout du chemin relatif
            # J'ajoute les tuiles au dictionnaire + support transparence
            self.tuiles[nom] = pg.image.load(fichier).convert_alpha()
