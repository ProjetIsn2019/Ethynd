# -*- coding: utf-8 -*-
"""Les listes de sprites
Sprites, animations
Etc.
(A IMPORTER)
Auteur : Le Groupe
"""
import pygame as pg

vitesse = 3
largeur_sprite = 64
hauteur_sprite = 64
sprite = "images/sprites/personnage_"  # Le nom de base d'un sprite du joueur sans le numéro

###############################################################################
touches = {  # Les touches pour les déplacements
    # [x, y, "direction", "mouvement", libre?]
    # Nombre de pixels en x, nombre de pixels en y, direction, mouvement.
    # libre = Est-ce que le personnage est libre ? True/False
    pg.K_UP:    [0, vitesse, "haut", "marche", True],
    pg.K_LEFT:  [vitesse, 0, "gauche", "marche", True],
    pg.K_DOWN:  [0, -vitesse, "bas", "marche", True],
    pg.K_RIGHT: [-vitesse, 0, "droite", "marche", True],
    pg.K_x:     [0, 0, None, "attaque", False],
}
###############################################################################
timings = {  # Timings des animations
    # [tick, images, libre, reset]
    # tick = le nombre de tick pour changer une frame (Tick entre chaque frame)
    # images = le nombre d'images de l'animation - 1 (0 compte comme une frame)
    # libre = Libérer le personnage après l'animation ? True = oui False = non
    # reset = revenir sur base après la fin de l'animation ? (Sinon on répète)
    "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
    "marche": [4, 3, True, False],
    "attaque": [2, 3, True, True],
}
###############################################################################
animation = {  # Repertorier les sprites
    # Animation marche : 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3 [...]
    "bas": {
        "base": [
            sprite + "00.png"   # Base
        ],
        "marche": [
            sprite + "01.png",  # Marche 1
            sprite + "02.png",  # Marche 2
            sprite + "03.png",  # Marche 3
            sprite + "00.png"   # Marche 4
        ],
        "attaque": [
            sprite + "44.png",  # Attaque 1
            sprite + "45.png",  # Attaque 2
            sprite + "46.png",  # Attaque 3
            sprite + "47.png"   # Attaque 4
        ],
    },
    "droite": {
        "base": [
            sprite + "11.png"   # Base
        ],
        "marche": [
            sprite + "12.png",  # Marche 1
            sprite + "13.png",  # Marche 2
            sprite + "14.png",  # Marche 3
            sprite + "11.png"   # Marche 4
        ],
        "attaque": [
            sprite + "52.png",  # Attaque 1
            sprite + "53.png",  # Attaque 2
            sprite + "54.png",  # Attaque 3
            sprite + "55.png"   # Attaque 4
        ],
    },

    "haut": {
        "base": [
            sprite + "22.png"   # Base
        ],
        "marche": [
            sprite + "23.png",  # Marche 1
            sprite + "24.png",  # Marche 2
            sprite + "25.png",  # Marche 3
            sprite + "22.png"   # Marche 4
        ],
        "attaque": [
            sprite + "48.png",  # Attaque 1
            sprite + "49.png",  # Attaque 2
            sprite + "50.png",  # Attaque 3
            sprite + "51.png"   # Attaque 4
        ],
    },

    "gauche": {
        "base": [
            sprite + "33.png"   # Base
        ],
        "marche": [
            sprite + "34.png",  # Marche 1
            sprite + "35.png",  # Marche 2
            sprite + "36.png",  # Marche 3
            sprite + "33.png"   # Marche 4
        ],
        "attaque": [
            sprite + "56.png",  # Attaque 1
            sprite + "57.png",  # Attaque 2
            sprite + "58.png",  # Attaque 3
            sprite + "59.png"   # Attaque 4
        ],
    }
}
son = {
    "marche" : "son/joueur/marche.ogg",
    "attaque": "son/joueur/attaque.ogg",
    "blessure": "son/joueur/blessure.ogg"
}
