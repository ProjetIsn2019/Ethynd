# -*-coding:utf-8 -*
"""Classe du Joueur Python
Cette classe sera dédiée au joueur, uniquement et pas les PNJs.
Auteur: Dorian Voland
"""
from classes import info
import pygame as pg


class Joueur:
    def __init__(self):
        """Initialise le personnage
        """
        self.largeur = 24  # Taille Largeur
        self.hauteur = 64  # Taille Hauteur
        self.direction = "bas"  # Direction du personnage (bas par défaut)
        self.mouvement = None   # Mouvement actuel du joueur (None = aucun)
        self.libre = True       # Si le personnage est pas occupé à faire qqch
        self.charger_sprite()   # On charge les sprites

    def bouger(self, ecran, map):
        """Lis ce que le joueur fait
            On agit en conséquence, ex: si le joueur appuie en haut le
            sprite va en haut, etc.
        """
        bool = True  # Boolean pour savoir si la boucle s'execute pas
        touches = pg.key.get_pressed()  # Touches enfoncées
        if not self.libre:  # Si le personnage est occupé
            return          # Quitter la fonction
        for touche in info.touches:  # Je parcours les touches enfoncées
            if touches[touche]:  # Si la touche est définie dans info
                # Pour trouver la future position du joueur:
                # Position milieu + pixels de déplacements
                # Pour trouver le millieu on divise les dimensions de l'ecran
                # Par deux.
                # x_pos = ecran.get_width()/2 + info.touches[touche][0]
                # y_pos = ecran.get_height()/2 + info.touches[touche][1]
                # if map.est_accessible(x_pos, y_pos, ecran):  # Si 0 collision
                map.x_camera += info.touches[touche][0]  # Bouger camera
                map.y_camera += info.touches[touche][1]  # Bouger camera
                if info.touches[touche][2] is not None:
                    self.direction = info.touches[touche][2]  # Modif direction
                self.mouvement = info.touches[touche][3]  # Changer mouvement
                self.libre = info.touches[touche][4]  # Changer disponibilité
                bool = False  # La boucle s'est executée
        if bool:  # Si la boucle ne s'est pas executé (bool est sur true)
            self.mouvement = None  # On dit qu'il n'y a aucun mouvement

    def charger_sprite(self):
        """Charge les sprites
        Permets de charger les sprites du dictionnaire "info"
        """
        for mouvement in info.animation:  # Parcours des mouvements
            numero = 0  # Compteur utilisé dans le parcours des sprites
            for sprite in info.animation[mouvement]:  # Parcours des sprites
                if isinstance(sprite, str):  # Si le sprite est encore un texte
                    img = pg.image.load(sprite).convert_alpha()  # Charger Img
                    info.animation[mouvement][numero] = img  # Sauvegarder
                numero += 1  # Numéro du sprite actuel + 1

    def afficher(self, ecran):
        """Affiche le personnage
        Et gère ses animations
        """
        # Je capture les dimensions de la fenêtre actuelle
        # Et je calcule les points centraux (moyenne)
        y_decalage = -self.hauteur/2  # Le décalage car l'image se génère
        x_decalage = -self.largeur/2  # A partir de son côté haut gauche
        x_centre = ecran.get_width()/2 + x_decalage   # Le x central
        y_centre = ecran.get_height()/2 + y_decalage  # Le y central

        if self.mouvement == "marche":  # Si le joueur est en mouvement
            # Gestion du compteur
            self.compteur = self.compteur + 1 if self.compteur < 20 - 1 else 0
            # Le compteur augemente si on est en dessous de 19
            # Si on atteind 19 on rénitialise le compteur à 0
            # Car le prochain nombre est 19 et compteur < 20 est rempli donc
            # On utilise compteur < 19 pour éviter d'avoir un trop gros nombre
            # Diviseur = 5 (Fréquence normale)
            nombre = self.compteur // 5  # On veut un nombre dans [0;3]

        elif self.mouvement == "attaque":
            # Gestion du compteur
            self.compteur = self.compteur + 1 if self.compteur < 12 - 1 else 0
            # Pareil que plus haut

            if self.compteur == 0:  # Si l'animation est terminée
                self.libre = True  # Libérer le bersonnage
                nombre = 0  # Choisir la tuile de base

            # Diviseur = 2 (Fréquence très rapide)
            nombre = self.compteur // 3 + 3  # On veut un nombre dans [3;7]

        else:  # On reviens en position standart si rien ne ce passe
            self.compteur = 0  # Pas de compteur de marche
            nombre = 0

        sprite = info.animation[self.direction]  # On prend la liste
        sprite = sprite[nombre]  # On prend le bon sprite
        ecran.blit(sprite, (x_centre, y_centre))  # Affiche le sprite
