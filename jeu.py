# -*- coding: utf-8 -*-
"""Programme final
+ Boucle de jeu
"""
from fonctions import maps
import pygame

pygame.init()  # Mettre en route pygame
pygame.display.set_caption("Ethynd")  # Titre de la fenêtre
# pygame.display.set_icon("images/icone.png")  # Icone
ecran = pygame.display.set_mode((640, 480))  # Affichage de la fenêtre
# 600 et 400: c'est la taille de la fenêtre (20 et 15 tuiles)
quitter = False
map = maps.Map("maps/test.map")
map.init_tuiles() # Initialisation des tuiles
map.afficher(ecran) # On affiche la map

while quitter != True:  # Tant que le joueur ne veux pas jouer
    """ Boucle de jeu
    Boucle de jeu: Gestion events, executée en boucle.
    """

    for event in pygame.event.get():  # pygame.event.get() = liste des events
        if event.type == pygame.KEYDOWN:  # Event : Touche enclenchée
            if event.key == pygame.K_ESCAPE:  # Touche = Echappe
                quitter = True  # On quitte

    pygame.display.flip()  # On change de frame. On actualise l'écran.
pygame.quit()  # Quitter pygame.
