# -*- coding: utf-8 -*-
"""Boucle et Events
Auteurs: Sofiane Dorian Anthony
"""
import pygame as pg


def boucle_de_jeu(ecran, perso, map):
    """ Boucle de jeu
    Boucle de jeu: Gestion events, executée en boucle.
    1 éxécution = 1 tick.
    """
    ecran.fill(map.couleur_fond)  # On change la couleur de fond (de la map)
    map.afficher(ecran)  # On affiche la map chaque tick pour actaliser
    perso.afficher(ecran)  # On actualise la position du personnage
    perso.lecture_touche(ecran)  # On vérifie les touches
    #                    # les déplacements
    return map


def event_pg(event, ecran_x, ecran_y, fullscreen, jouer):  # Events pygame
        if event.type == pg.KEYDOWN:  # Event : Touche enclenchée

            if event.key == pg.K_ESCAPE:  # Touche = Echappe
                jouer = False  # On quitte

            if event.key == pg.K_f:  # Si touche = f
                # On veut pouvoir changer le mode plein écran en jeu
                # C'est possible avec ces instructions
                if fullscreen:  # Si on est déjà en plein écran
                    pg.display.set_mode((680, 480), pg.NOFRAME)
                    # Mettre en fenêtre
                    fullscreen = False  # Enregistrer le choix dans notre var.
                else:  # Si on est déjà en fenêtre
                    pg.display.set_mode((ecran_x, ecran_y),
                                        pg.HWSURFACE)
                    fullscreen = True   # Enregistrer le choix dans notre var.
                    # Mettre en plein écran

        if event.type == pg.QUIT:  # Event : Touche enclenchée
            jouer = False  # On quitte

        return jouer, fullscreen
