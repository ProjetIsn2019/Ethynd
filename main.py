# -*- coding: utf-8 -*-
"""Programme final
Auteurs: Sofiane Dorian Anthony
"""
from fonctions import joueur
from fonctions import mapping
from fonctions import jeu
import pygame as pg

# FENETRE
pg.init()  # Mettre en route pg
pg.display.set_caption("Ethynd")  # Titre de la fenêtre
icone = pg.image.load("images/icone.png")  # Je charge l'icone
pg.display.set_icon(icone)  # Je met en place l'icone
ecran = pg.display.set_mode((0, 0),             # (0, 0) = taille de écran
                            pg.HWSURFACE)      # Plein écran
# On affiche la fenêtre lors de la définition de "ecran".
# FENETRE

# VARIABLES
fullscreen = True  # Notre variable plein écran pour pouvoir le changer
ecran_x = ecran.get_width()  # Taille de l'écran
ecran_y = ecran.get_height()  # Taille de l'écran
jouer = True  # On ne veux pas quitter le jeu dès le départ :')
horloge = pg.time.Clock()
# VARIABLES

# AUTRE
pg.mouse.set_visible(False)  # On cache la souris
map = mapping.Map("maps/test")  # Chargement de la map
perso = joueur.Joueur(ecran_x/2, ecran_y/2)  # On met le joueur au centre
# AUTRE

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
    horloge.tick(30)  # 30 tick par seconde seront executés
    pg.display.update()  # On change de tick. On actualise l'écran.
pg.quit()  # Quitter pg.
