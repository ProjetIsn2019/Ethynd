# -*- coding: utf-8 -*--son
"""Programme final
Auteurs: Sofiane Dorian Anthony
"""
import pygame as pg
from fonctions import jeu

pg.mixer.pre_init(44100, -16, 2, 1024)  # Réglages du mixeur pygame (fréquence (Hz), nombre de bits, channel, taille du buffer)
pg.mixer.init()  # Initialisation du mixeur audio pygame
pg.mixer.set_num_channels(8)
pg.init()  # Mettre en route pygame
jeu.initialiser_fenetre()  # Créer et initialiser la fenêtre
jeu.musique()
jeu.menu()  # Affichage du menu
pjg.quit()  # Quitter pg.
