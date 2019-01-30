# -*- coding: utf-8 -*-
"""Programme final
Auteurs: Sofiane Dorian Anthony
"""
import pygame as pg
from constantes import constantes_partie as cp
from fonctions import jeu

pg.init()  # Mettre en route pygame
jeu.initialiser_jeu()  # J'initialise la partie

while cp.jouer:  # Tant que le joueur joue
    """ Boucle de jeu
    Boucle de jeu: Gestion events, executée en boucle.
    1 éxécution = 1 tick.
    """
    jeu.boucle_de_jeu()  # La boucle de jeu

    for event in pg.event.get():  # Je parcours les events
        jeu.event_pg(event)  # Fonction des events pygame

    cp.horloge.tick(30)  # 30 tick par seconde seront executés
    pg.display.update()  # On change de tick. On actualise l'écran.
pg.quit()  # Quitter pg.
