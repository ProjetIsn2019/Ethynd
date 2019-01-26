# -*- coding: utf-8 -*-
"""Programme final
Auteurs: Sofiane Dorian Anthony
"""
from fonctions import joueur
from fonctions import mapping
from fonctions import jeu
import pygame as pg

pg.init()  # Mettre en route pg
pg.display.set_caption("Ethynd")  # Titre de la fenêtre
icone = pg.image.load("images/icone.png")  # Je charge l'icone
pg.display.set_icon(icone)  # Je met en place l'icone

ecran = pg.display.set_mode((0, 0),             # (0, 0) = taille de écran
                            pg.HWSURFACE)      # Plein écran
# On affiche la fenêtre lors de la définition de "ecran".

fullscreen = True  # Notre variable plein écran pour pouvoir le changer
ecran_x = ecran.get_width()
ecran_y = ecran.get_height()
jouer = True  # On ne veux pas quitter le jeu dès le départ :')

map = mapping.Map("maps/test")  # Chargement de la map
perso = joueur.Joueur(ecran_x/2, ecran_y/2)  # On met le joueur au centre

while jouer:  # Tant que le joueur joue
    """ Boucle de jeu
    Boucle de jeu: Gestion events, executée en boucle.
    1 éxécution = 1 tick.
    """
    map = jeu.boucle_de_jeu(ecran, perso, map)

    for event in pg.event.get():  # pg.event.get() = liste des events
        jouer, fullscreen = jeu.event_pg(event,  # Event pygame
                                         ecran_x, ecran_y,
                                         fullscreen, jouer)

    pg.display.update()  # On change de tick. On actualise l'écran.
pg.quit()  # Quitter pg.
