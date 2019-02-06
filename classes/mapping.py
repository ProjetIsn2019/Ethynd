# -*- coding: utf-8 -*-
"""Les maps
Objet "Map" qui correspond a une carte de tuiles.
Auteur: Sofiane
"""
from constantes import constantes_tuiles as ct
from constantes import constantes_partie as cp
import pygame as pg


class Map:
    """Créer une map
    Pour créer des maps directement et facilement (Un outil)
    Permets de:
    - Charger une map (Avec 4 couches de tuiles)
    - Afficher une map (Avec les 4 couches de tuiles)
    ++ Support transparence.
    """

    def __init__(self, nom, couleur_fond=(40, 38, 51)):
        self.nom = nom  # Définition du nom de la map
        self.x_camera = 0  # Camera X (position)
        self.y_camera = 0  # Camera Y (position)
        self.couleur_fond = couleur_fond  # Couleur de fond
        self.matrices = {  # Dictionnaire des matrices
            0: [],  # Matrice qui stockera le fond
            1: [],  # Matrice qui stockera le milieu
            2: [],  # Matrice qui stockera le 1er plan
            3: []   # Matrice qui stockera le plan spécial
        }

        self.charger_matrice()  # Chargement de la matrice, du fichier carte
        # Pour le nombre de colonnes et de lignes on utilise la matrice du fond
        self.x = len(self.matrices[0][0])  # Nombre de colonnes
        self.y = len(self.matrices[0])     # Nombre de lignes
        self.charger_collisions()  # Charger les collisions de la map

    def charger_matrice(self):
        """Charger les matrices
        Lire le fichier de la carte et stocker les tuiles dans une matrice
        Permets de convertir un .csv en tableau/matrice.
        Permets de convertir plusieurs .csv en tableaux 3D
        """
        for i in range(4):  # On a 4 calques, ici on parcours les calques
            nom_fichier = self.nom + "_" + str(i) + ".csv"  # Nom du fichier
            #                                          # Ex: nom_0.csv
            print("Chargement de", nom_fichier + "...")  # Les logs
            f = open(nom_fichier, "r")    # Ouvrir le fichier
            for ligne in f.readlines():   # Je regarde chaque lignes
                ligne = ligne.replace("\n", "")  # Je supprime les \n
                ligne = ligne.split(",")  # On convertis la ligne en liste
                if ligne != []:  # Si la ligne en liste n'est pas nulle
                    self.matrices[i].append(ligne)  # On ajoute la liste
            f.close()  # Fermer fichier

    def charger_collisions(self):
        """ Crée les rectangles de collisions de la map
        Permets de charger les rectangles de collision de la map
        (Peut génèrer des latences !)
        """
        # Je capture les dimensions de la fenêtre actuelle
        l, h = cp.ecran.get_width(), cp.ecran.get_height()  # l = largeur
        #                                                   # h = hauteur
        # Je calcule les points centraux (moyenne)
        x_centre = l/2  # Le x central a partir des dimensions de l'écran
        y_centre = h/2  # Le y central a partir des dimensions de l'écran

        # Je calcule le point de départ pour le rendu de la map
        # Formule:    Point - Nb tuiles_map * 32 / 2
        # Simplifiée: Point - Nb_tuiles_map * 16
        x_rendu = x_centre - self.x * 16 + self.x_camera
        y_rendu = y_centre - self.y * 16 + self.y_camera

        for i in range(3):  # Je parcours les 3 premières couches de la map
            for x in range(self.x):  # Parcours les colonnes
                for y in range(self.y):  # Je parcours les lignes
                    # En parcourant les 3 dimensions, on parcours toutes
                    # les tuiles. Voilà ce qu'on va faire avec:
                    if self.matrices[i][y][x] in ct.tuiles:  # Si elle existe
                        x_tuile = x_rendu + x*32  # Position de la tuile
                        y_tuile = y_rendu + y*32  # Position de la tuile$
                        if self.matrices[i][y][x] in ct.collision:
                            # On extrait l'image
                            tuile = ct.tuiles[self.matrices[i][y][x]]
                            # Charger la hitbox de la tuile
                            ct.hitbox_tuiles.append(pg.Rect(x_tuile,
                                                            y_tuile,
                                                            32, 32))

    def bouger_hitbox(self, x, y):
        """Déplace les rectangles de collision
        Permets de déplacer les rectangles de collisions, utilisé lors du
        Déplacement du personnage ou de la camera
        """
        nouvelle_hitbox = []  # Nouvelle liste des hitboxs
        for hitbox in ct.hitbox_tuiles:
            hitbox = hitbox.move(x, y)
            nouvelle_hitbox.append(hitbox)
            pg.draw.rect(cp.ecran, (255, 0, 0), hitbox)
        ct.hitbox_tuiles = nouvelle_hitbox

    def afficher(self):
        """ Affiche la map
        Affiche la map sur l'écran par rapport a un point
        Le point est sur 0,0 par défaut.
        """
        # Je capture les dimensions de la fenêtre actuelle
        l, h = cp.ecran.get_width(), cp.ecran.get_height()  # l = largeur
        #                                                   # h = hauteur
        # Je calcule les points centraux (moyenne)
        x_centre = l/2  # Le x central a partir des dimensions de l'écran
        y_centre = h/2  # Le y central a partir des dimensions de l'écran

        # Je calcule le point de départ pour le rendu de la map
        # Formule:    Point - Nb tuiles_map * 32 / 2
        # Simplifiée: Point - Nb_tuiles_map * 16
        x_rendu = x_centre - self.x * 16 + self.x_camera
        y_rendu = y_centre - self.y * 16 + self.y_camera

        for i in range(3):  # Je parcours les couches
            for x in range(self.x):  # Parcours les colonnes
                for y in range(self.y):  # Je parcours les lignes
                    # En parcourant les 3 dimensions, on parcours toutes
                    # les tuiles. Voilà ce qu'on va faire avec:
                    x_tuile = x_rendu + 32*x  # Pour faire le décalage
                    y_tuile = y_rendu + 32*y  # Entre chaque tuile
                    if self.matrices[i][y][x] in ct.tuiles:  # Si elle existe
                        tuile = ct.tuiles[self.matrices[i][y][x]]  # On extrait
                        x_tuile = x_rendu + x*32
                        y_tuile = y_rendu + y*32
                        cp.ecran.blit(tuile, (x_tuile,   # On affiche
                                              y_tuile))  # Tuile par tuile
                        # Si la tuile a des collisions

    def afficher_4eme_couche(self):
        """ Affiche la couche transparente de la map
        Destinée a être utilisée après l'affichage du personnage.
        """
        # Je capture les dimensions de la fenêtre actuelle
        l, h = cp.ecran.get_width(), cp.ecran.get_height()  # l = largeur
        #                                                   # h = hauteur
        # Je calcule les points centraux (moyenne)
        x_centre = l/2  # Le x central a partir des dimensions de l'écran
        y_centre = h/2  # Le y central a partir des dimensions de l'écran

        # Je calcule le point de départ pour le rendu de la map
        # Formule:    Point - Nb tuiles_map * 32 / 2
        # Simplifiée: Point - Nb_tuiles_map * 16
        x_rendu = x_centre - self.x * 16 + self.x_camera
        y_rendu = y_centre - self.y * 16 + self.y_camera

        for x in range(self.x):  # Parcours les colonnes
            for y in range(self.y):  # Je parcours les lignes
                # En parcourant les 3 dimensions, on parcours toutes
                # les tuiles. Voilà ce qu'on va faire avec:
                if self.matrices[3][y][x] in ct.tuiles:  # Si elle existe
                    tuile = ct.tuiles[self.matrices[3][y][x]]  # On extrait
                    x_tuile = x_rendu + x*32  # Position de la tuile
                    y_tuile = y_rendu + y*32  # Position de la tuile
                    cp.ecran.blit(tuile, (x_tuile,   # On affiche
                                          y_tuile))  # Tuile par tuile*
        for hitbox in ct.hitbox_tuiles:
            pg.draw.rect(cp.ecran, (255, 0, 0), hitbox)

    def tuile_coord(self, x, y):
        """Retourne les tuiles aux coordonnées x, y (Coordonnées en tuiles)
        Sers aux collisions et aux events.
        """
        return (self.matrices[0][y][x],  # On retourne les 3 tuiles des
                self.matrices[1][y][x],  # 3 premières couches
                self.matrices[2][y][x])

    def est_accessible(self, x, y):
        """Détermine si un bloc est accessible ou si il ne l'est pas
        (Collisions)
        Retourne un boolean
        """
        x = int(x)  # Mettre sous forme d'entier
        y = int(y)  # Convertir en entier
        tuiles = self.tuile_coord(x, y)  # Trouver tuiles en (x;y)
        if tuiles == ("-1", "-1", "-1"):  # Si c'est vide
            return False  # Retourner non car le perso ne peux pas y aller
        else:  # Si c'est pas vide
            for tuile in tuiles:  # Je parcours les couches de tuiles
                if tuile in ct.collision:  # Si une tuile a une collision
                    return False  # Retourner non
                elif tuile in ct.eau:  # Si une tuile est de l'eau
                    return False  # Retourner non
            else:  # Sinon, aucune tuile de collision détectée
                return True  # Retourner oui, pas de collisions/vide.

    def vider_hitbox(self):
        """ Vide la hitbox
        """
        ct.hitbox_tuiles.clear()  # Vider la liste des hitboxs
        return
