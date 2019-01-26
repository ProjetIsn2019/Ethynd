# -*- coding: utf-8 -*-
"""Programme final
+ Boucle de jeu
Auteurs: Sofiane Dorian Anthony
"""
from fonctions import mapping
import pygame

pygame.init()  # Mettre en route pygame
pygame.display.set_caption("Ethynd")  # Titre de la fenêtre
icone = pygame.image.load("images/icone.png")  # Je charge l'icone
pygame.display.set_icon(icone)  # Je met en place l'icone

ecran = pygame.display.set_mode((0, 0),             # (0, 0) = taille de écran
                                pygame.FULLSCREEN)  # Plein écran
# On affiche la fenêtre lors de la définition de "ecran".

jouer = True  # On ne veux pas quitter le jeu dès le départ :')
map = mapping.Map("maps/test.map")  # Chargement de la map

while jouer:  # Tant que le joueur joue
    """ Boucle de jeu
    Boucle de jeu: Gestion events, executée en boucle.
    1 éxécution = 1 tick.
    """
    ecran.fill(map.couleur_fond)  # On change la couleur de fond (gris)
    map.afficher(ecran)  # On affiche la map chaque tick pour actaliser
#                        # les déplacements

    print(pygame.time.Clock.get_fps)

    for event in pygame.event.get():  # pygame.event.get() = liste des events
        if event.type == pygame.KEYDOWN:  # Event : Touche enclenchée
            if event.key == pygame.K_ESCAPE:  # Touche = Echappe
                Jouer = False  # On quitte

    pygame.display.update()  # On change de tick. On actualise l'écran.
pygame.quit()  # Quitter pygame.
