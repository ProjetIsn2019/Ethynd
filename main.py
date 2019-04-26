# -*- coding: utf-8 -*--son
"""Programme final
Auteurs: Sofiane Dorian Anthony
"""
import pygame as pg
from fonctions import jeu

pg.init()  # Mettre en route pygame
jeu.initialiser_fenetre()  # Créer et initialiser la fenêtre
jeu.musique()  # Initialiser la musique
jeu.menu()  # Affichage du menu
pg.quit()  # Quitter pg.
