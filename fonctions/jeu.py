# -*- coding: utf-8 -*-
"""Boucle et Events
Auteurs: Sofiane Dorian Anthony
"""
from constantes import constantes_partie as cp
from classes import joueur
from classes import mapping
import pygame as pg


def initialiser_jeu():
    pg.init()  # Mettre en route pg
    pg.display.set_caption("Ethynd")  # Titre de la fenêtre
    pg.display.set_icon(pg.image.load("images/icone.png"))  # Je mettre l'icone
    pg.mouse.set_visible(False)  # On cache la sourise
    cp.ecran = pg.display.set_mode((0, 0),         # (0, 0) = taille de écran
                                   pg.HWSURFACE)   # Plein écran
    # On affiche la fenêtre lors de la définition de "ecran".
    # VARIABLES
    cp.plein_ecran = True  # Notre variable plein écran pour pouvoir le changer
    cp.ecran_x = cp.ecran.get_width()  # Taille de l'écran
    cp.ecran_y = cp.ecran.get_height()  # Taille de l'écran
    cp.jouer = True  # On ne veux pas quitter le jeu dès le départ :')
    cp.horloge = pg.time.Clock()
    cp.map = mapping.Map("maps/test")  # Chargement de la map
    cp.perso = joueur.Joueur()  # On met le joueur au centre


def boucle_de_jeu():
    """ Boucle de jeu
    Boucle de jeu: Gestion events, executée en boucle.
    1 éxécution = 1 tick.
    """
    cp.ecran.fill(cp.map.couleur_fond)  # On met la couleur de fond de la map
    cp.map.afficher(cp.ecran)  # On affiche la map chaque tick pour actaliser
    cp.perso.afficher(cp.ecran)  # On actualise la position du personnage
    cp.map.afficher_4eme_couche(cp.ecran)  # On affiche la 4 eme couche opaque
    cp.perso.bouger(cp.ecran, cp.map)  # Faire les déplacements, clavier


def event_pg(event):  # Events pygame
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
