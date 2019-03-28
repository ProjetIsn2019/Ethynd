# -*- coding: utf-8 -*-
"""Les maps
Objet "Tuile" qui correspond a une tuile.
Objet "Map" qui correspond a une carte de tuiles.
Auteur: Sofiane
"""
from constantes import constantes_tuiles as ct
from constantes import constantes_partie as cp
from constantes import constantes_collisions as cc
from classes import collision as col
import pygame as pg


class Map:
    """Créer une map
    Pour créer des maps directement et facilement (Un outil)
    Permets de:
    - Charger une map (Avec 4 couches de tuiles)
    - Afficher une map (Avec les 4 couches de tuiles)
    ++ Support transparence.
    """

    def __init__(self, nom, musique=None, camera=(0, 0), couleur_fond=(40, 38, 51)):
        """Initialise la map
        Avec un nom, la position de la camera, la couleur de fond
        Ajoute une hitbox pour les collisions et convertis le fichier de la map
        Sous forme de matrice en 3 dimensions
        1 map est composée de 4 couches, nommées respectivement 0, 1, 2, 3
        Seul la couche "3" (la 4 ème) passe DEVANT le personnage.
        Les couches 0 1 et 2 sont pour les collisions et les graphismes
        """
        x, y = camera  # On extrait les coordonnées de la tuple
        self.nom = nom  # Définition du nom de la map
        self.x_camera = x  # Camera X (position)
        self.y_camera = y  # Camera Y (position)
        self.couleur_fond = couleur_fond  # Couleur de fond
        self.matrices = {  # Dictionnaire des matrices
            0: [],  # Matrice qui stockera le fond
            1: [],  # Matrice qui stockera le milieu
            2: [],  # Matrice qui stockera le 1er plan
            3: []   # Matrice qui stockera le plan spécial
        }
        self.charger_matrice()  # Chargement de la matrice, du fichier carte
        # Pour le nombre de colonnes et de lignes on utilise la matrice du fond
        self.x = len(self.matrices[0][0])  # Variable contenant le nombre de colonnes
        self.y = len(self.matrices[0])     # Variable contenant le nombre de colonnes
        # Variable contenant l'arrière plan de la map (pg.SCRALPHA permet de rendre la surface transparente)
        self.arriere_plan = pg.Surface((self.x*32, self.y*32), pg.SRCALPHA)  # On crée une surface de la taille de la map
        # Variable contenant le premier plan de la map 
        self.premier_plan = pg.Surface((self.x*32, self.y*32), pg.SRCALPHA)  # On crée une surface de la taille de la map
        self.charger_masques()  # Charger les collisions de la map (Masques)
        self.charger_arriere_plan()  # Charger l'arrière plan
        self.charger_premier_plan()  # Charger le premier plan
        
        if cp.musique is not None:  # Si une musique est jouée
            cp.musique.stop()   # Alors arrêter cette musique
        if musique is not None: # Si une musique est donnée dans les paramètres 
            cp.musique = pg.mixer.Sound("son/" + musique)  # Récuperer la musique sous forme de variable
            cp.musique.play()   # Jouer la musique 

    def afficher_arriere_plan(self):
        """ Affiche les 3 premières couches de la map
        3 premières couches (0,1,2) = Arrière plan
        """
        cp.ecran.blit(self.arriere_plan, (self.x_camera, 
                                          self.y_camera)) #Affiche le premier plan
        
    def afficher_premier_plan(self):
        """ Affiche la 4 eme couche de la map
        Quatrième couche (3) = Premier plan devant le personnage
        """
        cp.ecran.blit(self.premier_plan, (self.x_camera, 
                                          self.y_camera)) #Affiche le premier plan
        
    def bouger_masque(self, x, y):
        """Déplace les masques de collision
        Permets de déplacer les masques de collisions, utilisé lors du
        Déplacement du personnage ou de la camera
        """
        nouvelle_liste = [] # Liste contenant les masques actualisés
        # nouvelle_liste doit écraser la liste des constantes de collision pour les tuiles
        for masque in cc.groupes["tuile"]:  # Je parcours le contenu du groupe
            masque.rect.move_ip(x, y)  # Déplacer le rect.
            nouvelle_liste.append(masque)  # L'ajouter à la nouvelle liste
        cc.groupes["tuile"] = nouvelle_liste  # Ecraser l'ancienne liste
        
    def bouger(self, x, y):
        """Déplacer la map
        Déplace:
        - Les 3 couches esthétiques de tuiles
        - La 4 ème couche qui passe par-dessus le personnage
        - La couche de collision, invisible
        """
        cp.map.bouger_masque(x, y)  # Bouger le masque de collision
        cp.map.x_camera += x  # Bouger la camera
        cp.map.y_camera += y  # Bouger la camera

    def point_rendu(self):
        """Avoir le point de départ du rendu
        Retourne les points de rendu
        """
        # Je calcule le point de départ pour le rendu de la hitbox
        # Formule:    Point - Nb tuiles_map * 32 / 2
        # Simplifiée: Point - Nb_tuiles_map * 16
        x_rendu = cp.centre_x - self.x * 16 + self.x_camera
        y_rendu = cp.centre_y - self.y * 16 + self.y_camera
        return x_rendu, y_rendu

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

    def charger_masques(self):
        """ Crée les rectangles de collisions de la map
        Permets de charger les rectangles de collision de la map
        (Peut génèrer des latences !)
        """
        for groupe in cc.groupes:  # Je parcours les groupes de collision
            cc.groupes[groupe] = pg.sprite.Group()  # Je les réinitialise

        x_rendu, y_rendu = self.point_rendu()  # Sauvegarder le point du rendu
        for i in range(3):  # Je parcours les 3 premières couches de la map
            for x in range(self.x):  # Parcours les colonnes
                for y in range(self.y):  # Je parcours les lignes
                    if self.matrices[i][y][x] in ct.tuiles:  # Si elle existe
                        x_tuile = x_rendu + x*32  # Position de la tuile
                        y_tuile = y_rendu + y*32  # Position de la tuile$
                        if self.matrices[i][y][x] in ct.tuiles_collisions:
                            # On extrait l'image
                            tuile = ct.tuiles[self.matrices[i][y][x]]
                            # On fait le mask a partir de cette image
                            mask = pg.mask.from_surface(tuile)
                            # On créé le rectangle associé a l'image
                            rect = pg.Rect(x_tuile, y_tuile, 32, 32)
                            # Sauvegarder la liste (rect + mask)
                            col.Masque("tuile", rect, mask)

    def charger_arriere_plan(self):
        """ Charge dans la variable self.arriere_plan l'image
        Superposée des 3 premieres couches
        """
        x_rendu, y_rendu = self.point_rendu()  # Avoir le point du rendu

        for i in range(3):  # Je parcours les couches
            for x in range(self.x):  # Parcours les colonnes
                for y in range(self.y):  # Je parcours les lignes
                    x_tuile = x_rendu + 32*x  # Pour faire le décalage
                    y_tuile = y_rendu + 32*y  # Entre chaque tuile
                    if self.matrices[i][y][x] in ct.tuiles:  # Si elle existe
                        tuile = ct.tuiles[self.matrices[i][y][x]]  # On extrait
                        x_tuile = x_rendu + x*32
                        y_tuile = y_rendu + y*32
                        self.arriere_plan.blit(tuile, (x_tuile,   # On affiche
                                                       y_tuile))  # Tuile par tuile

    def charger_premier_plan(self):
        """ Charge dans la variable self.premier_plan l'image
        De la 4 eme couche
        """
        x_rendu, y_rendu = self.point_rendu()  # Avoir le point du rendu

        for x in range(self.x):  # Parcours les colonnes
            for y in range(self.y):  # Je parcours les lignes
                if self.matrices[3][y][x] in ct.tuiles:  # Si elle existe
                    tuile = ct.tuiles[self.matrices[3][y][x]]  # On extrait
                    x_tuile = x_rendu + x*32  # Position de la tuile
                    y_tuile = y_rendu + y*32  # Position de la tuile
                    self.premier_plan.blit(tuile, (x_tuile,   # On affiche
                                                   y_tuile))  # Tuile par tuile
