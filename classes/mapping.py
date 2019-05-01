# -*- coding: utf-8 -*-
"""Les maps
Objet "Tuile" qui correspond a une tuile.
Objet "Map" qui correspond a une carte de tuiles.
Auteur: Sofiane Djerbi pour correspondre au modèle de carte imaginé par Anthony
"""
from constantes import constantes_tuiles as ct
from constantes import constantes_partie as cp
from constantes import constantes_collisions as cc
from classes import monstre as mstr
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

    def __init__(self, nom, camera=(0, 0), musique=None):
        """Initialise la map
        Avec un nom, la position de la camera, la couleur de fond
        Ajoute une hitbox pour les collisions et convertis le fichier de la map
        Sous forme de matrice en 3 dimensions
        1 map est composée de 4 couches, nommées respectivement 0, 1, 2, 3
        Seul la couche "3" (la 4 ème) passe DEVANT le personnage.
        Les couches 0 1 et 2 sont pour les collisions et les graphismes
        Système de musique créé par Anthony.
        """
        self.compteur = 0  # Variable du compteur d'animation initialisé à 0
        x, y = camera      # On extrait les coordonnées de la tuple
        self.nom = nom     # Définition du nom de la map
        # On met -x et -y afin d'utiliser des coordonnées positives.
        # En effet la map utilise un repère orthonormé standard partageant son 0 avec le repère pygame.
        # Elle est donc très souvent négative.
        self.x_camera = x  # Camera X (position de la camera en fonction de l'axe des abcysses)
        self.y_camera = y  # Camera Y (position de la camera en fonction de l'ordonnée)
        self.matrices = {  # Dictionnaire des matrices
            0: [],  # Matrice qui stockera le fond
            1: [],  # Matrice qui stockera le milieu
            2: [],  # Matrice qui stockera le 1er plan
            3: []   # Matrice qui stockera le plan spécial
        }
        self.charger_matrice()  # Chargement de la matrice, du fichier carte
        # Pour le nombre de colonnes et de lignes on utilise la matrice du fond
        self.x = len(self.matrices[0][0])  # Variable contenant le nombre de colonnes
        self.y = len(self.matrices[0])     # Variable contenant le nombre de lignes
        # Variable contenant l'arrière plan de la map (pg.SCRALPHA permet de rendre la surface transparente)
        self.arriere_plan = pg.Surface((self.x*32, self.y*32), pg.SRCALPHA)  # On crée une surface de la taille de la map
        # Variable contenant le premier plan de la map
        self.premier_plan = pg.Surface((self.x*32, self.y*32), pg.SRCALPHA)  # On crée une surface de la taille de la map
        self.charger_hitboxs()  # Charger les collisions de la map (Hitboxs)
        self.charger_images()  # Charger l'arrière plan et le premier plan
        self.vider_monstres()  # Supprimer les monstres de l'ancienne map (si il y en a)

        if musique is not None:  # Si une musique est donnée dans les paramètres
            if cp.musique is not None:  # Si une musique est jouée
                cp.musique.stop()   # Alors arrêter cette musique
            cp.musique = pg.mixer.Sound("son/" + musique)  # Récuperer la musique sous forme d'objet
            cp.musique.play(loops=-1)   # Jouer la musique (loops=-1 permet de la jouer en boucle indéfiniment)

    def afficher_arriere_plan(self):
        """ Affiche les 3 premières couches de la map
        3 premières couches (0,1,2) = Arrière plan
        """
        cp.ecran.blit(self.arriere_plan, (self.x_camera,
                                          self.y_camera))  # Affiche l'arrière plan

    def afficher_premier_plan(self):
        """ Affiche la 4 eme couche de la map
        Quatrième couche (3) = Premier plan devant le personnage
        """
        cp.ecran.blit(self.premier_plan, (self.x_camera,
                                          self.y_camera))  # Affiche le premier plan

    def bouger_hitbox(self, x, y):
        """Déplace les hitboxs de collision
        Permets de déplacer les hitboxs de collisions, utilisé lors du
        Déplacement du personnage ou de la camera
        """
        # nouvelle_liste va écraser la liste des constantes de collision pour les tuiles
        for hitbox in cc.groupes["tuile"]:  # Je parcours le contenu du groupe
            hitbox.rect.move_ip(x, y)  # Déplacer le rect.

    def bouger(self, x, y):
        """Déplacer la map
        Déplace:
        - Les 3 couches esthétiques de tuiles
        - La 4 ème couche qui passe par-dessus le personnage
        """
        cp.map.x_camera += x  # Bouger la camera
        cp.map.y_camera += y  # Bouger la camera

    def actualiser(self):
        """Actualise la map
        Fait les animations de tuiles.
        Censé être lancé chaque tick
        """
        if self.compteur < 5:  # Si le compteur est inférieur à 5
            self.compteur += 1  # Incrémenter le compteur
            return  # Quitter la fonction
        for i in range(4):  # Parcourir les couches de la map
            for y in range(self.y):  # Parcourir les tuiles en abscisse
                for x in range(self.x):  # Parcourir les tuiles en ordonnée
                    if self.matrices[i][y][x] in ct.animations:  # Si la tuile a une animation correspondante
                        self.matrices[i][y][x] = ct.animations[self.matrices[i][y][x]]  # Lui assigner l'animation correspondante
                        tuile = ct.tuiles[self.matrices[i][y][x]]  # On extrait la tuile
                        if i == 3:  # Si on parcours le premier plan
                            self.premier_plan.blit(tuile, (x*32, y*32))  # On colle les images sur l'arrière plan tuile par tuile
                        else:  # Sinon (implicitement, on parcours l'arrière plan)
                            self.arriere_plan.blit(tuile, (x*32, y*32))  # On colle les images sur le premier plan tuile par tuile
        self.compteur = 0

    def charger_matrice(self):
        """Charger les matrices
        Lire le fichier de la carte et stocker les tuiles dans une matrice
        Permets de convertir un .csv en tableau/matrice.
        Permets de convertir plusieurs .csv en tableaux 3D
        """
        for i in range(4):  # On a 4 calques, ici on parcours les calques
            nom_fichier = "maps/" + self.nom + "_" + str(i) + ".csv"  # Nom du fichier
            #                                          # Ex: nom_0.csv
            f = open(nom_fichier, "r")    # Ouvrir le fichier
            for ligne in f.readlines():   # Je regarde chaque lignes
                ligne = ligne.replace("\n", "")  # Je supprime les \n
                ligne = ligne.split(",")  # On convertis la ligne en liste
                if ligne != []:  # Si la ligne en liste n'est pas nulle
                    self.matrices[i].append(ligne)  # On ajoute la liste
            f.close()  # Fermer fichier

    def charger_hitboxs(self):
        """ Crée les rectangles de collisions de la map
        Permets de charger les rectangles de collision de la map
        (Peut génèrer des latences !)
        """
        for groupe in cc.groupes:  # Je parcours les groupes de collision
            cc.groupes[groupe] = pg.sprite.Group()  # Je les réinitialise

        for i in range(3):  # Je parcours les 3 premières couches de la map
            for y in range(self.y):  # Parcours les colonnes
                for x in range(self.x):  # Je parcours les lignes
                    if self.matrices[i][y][x] in ct.tuiles:  # Si la tuile existe
                        if self.matrices[i][y][x] in ct.collisions:  # Si on lui a assigné des collisions
                            x_tuile = self.x_camera + x*32  # Position de la tuile (abscisses)
                            y_tuile = self.y_camera + y*32  # Position de la tuile (ordonnée)
                            tuile = ct.tuiles[self.matrices[i][y][x]]  # On extrait l'image
                            mask = pg.mask.from_surface(tuile)  # On fait le mask a partir de cette image
                            rect = pg.Rect(x_tuile, y_tuile, 32, 32)  # On créé le rectangle associé a l'image
                            col.Hitbox("tuile", rect, mask)  # Sauvegarder la liste (rect + mask)

    def vider_monstres(self):
        """ Supprime tout les monstres
        Utilisé lors d'un changement de map
        """
        cp.entites_liste = []

    def charger_monstres(self):
        """ Crée les monstres associés a une map
        Créer des monstres d'une liste
        """
        liste_monstre = []

        for type_monstre in cp.niveau[self.nom]:
            liste_monstre.append(type_monstre)

        for type_monstre in liste_monstre:
            for liste_parametre in cp.niveau[self.nom][type_monstre]:
                monstre = mstr.Monstre(type_monstre, liste_parametre)
                cp.entites_liste.append(monstre)

        for entite in cp.entites_liste:
            entite.deplacement()
            entite.afficher()


    def charger_images(self):
        """ Charge dans la variable self.arriere_plan l'image superposée des 3 premieres couches (0, 1, 2)
            Charge dans la variable self.premier_plan l'image de la dernière couche (3)
        """

        for i in range(4):  # Je parcours les couches
            for y in range(self.y):  # Parcours les colonnes
                for x in range(self.x):  # Je parcours les lignes
                    if self.matrices[i][y][x] in ct.tuiles:  # Si elle existe
                        tuile = ct.tuiles[self.matrices[i][y][x]]  # On extrait
                        if i < 3:  # Si on parcours les couches 2, 1 et 0
                            self.arriere_plan.blit(tuile, (x*32, y*32))  # On colle les images sur l'arrière plan tuile par tuile
                        else:
                            self.premier_plan.blit(tuile, (x*32, y*32))  # On colle les images sur le premier plan tuile par tuile
