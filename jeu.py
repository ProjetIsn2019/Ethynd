# -*- coding: utf-8 -*-
"""Programme final
+ Boucle de jeu
Auteurs: Sofiane Dorian Anthony
"""
from fonctions import map
import pygame

pygame.init()  # Mettre en route pygame
pygame.display.set_caption("Ethynd")  # Titre de la fenêtre
icone = pygame.image.load("images/icone.png") # Je charge l'icone
pygame.display.set_icon(icone)  # Je met en place l'icone

ecran = pygame.display.set_mode((0, 0),             # (0, 0) = taille de écran
                                pygame.FULLSCREEN)  # Plein écran
# On affiche la fenêtre lors de la définition de "ecran".

quitter = False # On ne veux pas quitter le jeu dès le départ :')
map = maps.Map("maps/test.map") # Chargement de la map

while quitter != True:  # Tant que le joueur ne veux pas jouer
    """ Boucle de jeu
    Boucle de jeu: Gestion events, executée en boucle.
    1 éxécution = 1 tick.
    """
    ecran.fill(map.couleur_fond)  # On change la couleur de fond (gris)
    map.afficher(ecran) # On affiche la map chaque tick pour actaliser
                        # les déplacements
    for event in pygame.event.get():  # pygame.event.get() = liste des events
        if event.type == pygame.KEYDOWN:  # Event : Touche enclenchée
            if event.key == pygame.K_ESCAPE:  # Touche = Echappe
                quitter = True  # On quitte

    pygame.display.update()  # On change de tick. On actualise l'écran.
pygame.quit()  # Quitter pygame.
