# -*-coding:utf-8 -*
"""Classe du Joueur Python
Cette classe sera dédiée au joueur, uniquement et pas les PNJs.
Auteur: Dorian Voland
"""
import pygame as pg


class Joueur:
    def __init__(self, x, y):
        """Initialise le personnage
        """
        self.x = x  # Coordonnées
        self.y = y  # Coordonnées
        self.width = 64  # Taille
        self.heigth = 64  # Taille
        self.vitesse = 1  # Vitesse
        self.sprite = "images/sprites/sprite_1_00.png"  # Image

    def lecture_touche(self, ecran):
        """Lis ce que le joueur fait
            On agit en conséquence, ex: si le joueur appuie en haut le
            sprite va en haut, etc.
        """

        fenetre_x = ecran.get_width()  # La largeur de l'écran
        fenetre_y = ecran.get_height()  # La hauteur de l'écran

        touche = pg.key.get_pressed()  # On vérifie les touches
        if touche[pg.K_LEFT] and self.x > 0:  # Si touche est enfoncée
            self.x -= self.vitesse  # Déplacer le personnage
            #                       # Pareil pour le reste..
        if touche[pg.K_RIGHT] and self.x < fenetre_x - self.width:
            self.x += self.vitesse
        if touche[pg.K_UP] and self.y > 0:
            self.y -= self.vitesse
        if touche[pg.K_DOWN] and self.y < fenetre_y - self.heigth:
            self.y += self.vitesse

    def afficher(self, ecran):
        """Affiche le personnage
        """
        # Chargement de l'image avec transparence
        image_perso = pg.image.load(self.sprite).convert_alpha()
        ecran.blit(image_perso, (self.x, self.y))  # Affichage
