# -*- coding: utf-8 -*-
"""Boucle et Events
Fonctions concernant le jeu et les évènements
Auteurs: Sofiane Dorian Anthony
"""
from constantes import constantes_partie as cp
from fonctions import charger
from classes import joueur
from classes import mapping
import pygame as pg


def initialiser_jeu():
    pg.display.set_caption("Ethynd")  # Titre de la fenêtre
    pg.display.set_icon(pg.image.load("images/icone.png"))  # Je mettre l'icone

    pg.mouse.set_visible(False)  # On cache la souris
    cp.ecran = pg.display.set_mode((0, 0),  # (0, 0) = taille de écran, on
                                   pg.HWSURFACE)   # affiche la fenêtre
    cp.ecran_x = cp.ecran.get_width()  # Taille de l'écran
    cp.ecran_y = cp.ecran.get_height()  # Taille de l'écran

    cp.plein_ecran = True  # Notre variable plein écran pour pouvoir le changer
    cp.jouer = True  # On ne veux pas quitter le jeu dès le départ :')
    cp.horloge = pg.time.Clock()  # L'horloge pour contrôler les tick par sec

    cp.map = mapping.Map("maps/test2")  # Chargement de la map
    cp.perso = joueur.Joueur()  # Chargement du joueur

    charger.charger_tileset()  # Charger les images de tuiles
    charger.charger_sprite()  # Charger les images de sprites


def boucle_de_jeu():
    """ Boucle de jeu
    Boucle de jeu: Gestion events, executée en boucle.
    1 éxécution = 1 tick.
    """
    cp.ecran.fill(cp.map.couleur_fond)  # On met la couleur de fond de la map
    cp.perso.lire_touches()  # Faire les déplacements/Animations
    cp.map.afficher(cp.ecran)  # On affiche la map chaque tick pour actaliser
    cp.perso.afficher(cp.ecran)  # On actualise la position du personnage
    cp.map.afficher_4eme_couche(cp.ecran)  # On affiche la 4 eme couche opaque


def event_pg(event):  # Events pygame
        """Les evénements pygame
        Evènements relatifs à Pygame en soi
        """
        if event.type == pg.KEYDOWN:  # Event : Touche enclenchée

            if event.key == pg.K_ESCAPE:  # Touche = Echappe
                cp.jouer = False  # On quitte

            if event.key == pg.K_f:  # Si touche = f
                # On veut pouvoir changer le mode plein écran en jeu
                # C'est possible avec ces instructions
                if cp.plein_ecran:  # Si on est déjà en plein écran, changer
                    pg.display.set_mode((680, 480), pg.NOFRAME)
                    cp.plein_ecran = False  # Enregistrer le statut
                else:  # Si on est déjà en fenêtre, mettre plein ecran
                    pg.display.set_mode((cp.ecran_x, cp.ecran_y),
                                        pg.HWSURFACE)
                    cp.plein_ecran = True   # Enregistrer le statut

        if event.type == pg.QUIT:  # Event : Touche enclenchée
            cp.jouer = False  # On quitte
