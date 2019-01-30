# -*- coding: utf-8 -*-
"""Les listes de sprites
Sprites, animations
Etc.
(A IMPORTER)
"""
import pygame as pg

vitesse = 3
sprite = "images/sprites/sprite_"  # Le nom d'un sprite sans son numéro

touches = {  # Les touches pour les déplacements
    # [0, 0, "direction", "mouvement", libre]
    # Nombre de pixels en x, nombre de pixels en y, direction, mouvement.
    # libre = Est-ce que le personnage est libre ? True/False
    pg.K_UP:    [0, vitesse, "haut", "marche", True],
    pg.K_LEFT:  [vitesse, 0, "gauche", "marche", True],
    pg.K_DOWN:  [0, -vitesse, "bas", "marche", True],
    pg.K_RIGHT: [-vitesse, 0, "droite", "marche", True],
    pg.K_SPACE: [0, 0, None, "saut", True],
    pg.K_w:     [0, 0, None, "attaque", False]
}

timings = {  # Timings des animations
    # [tick, images, libre, reset, couper]
    # tick = le nombre de tick pour changer une frame (Tick entre chaque frame)
    # images = le nombre d'images de l'animation - 1 (0 compte comme une frame)
    # libre = Libérer le personnage après l'animation ? True = oui False = non
    # reset = revenir sur base après la fin de l'animation ? (Sinon on répète)
    # couper = couper l'animation précedente ? True/False
    "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
    "marche": [5, 3, True, False, True],
    "attaque": [1, 3, True, True, True]
}

animation = {  # Repertorier les sprites
    # Animation marche : 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3 [...]
    "bas": {
        "base": [
            sprite + "1_00.png"   # Base
        ],
        "marche": [
            sprite + "1_01.png",  # Marche 1
            sprite + "1_02.png",  # Marche 2
            sprite + "1_03.png",  # Marche 3
            sprite + "1_00.png"   # Marche 4
        ],
        "attaque": [
            sprite + "1_44.png",  # Attaque 1
            sprite + "1_45.png",  # Attaque 2
            sprite + "1_46.png",  # Attaque 3
            sprite + "1_47.png"   # Attaque 4
        ]
    },
    "droite": {
        "base": [
            sprite + "1_11.png"   # Base
        ],
        "marche": [
            sprite + "1_12.png",  # Marche 1
            sprite + "1_13.png",  # Marche 2
            sprite + "1_14.png",  # Marche 3
            sprite + "1_11.png"   # Marche 4
        ],
        "attaque": [
            sprite + "1_52.png",  # Attaque 1
            sprite + "1_53.png",  # Attaque 2
            sprite + "1_54.png",  # Attaque 3
            sprite + "1_55.png"   # Attaque 4
        ]
    },

    "haut": {
        "base": [
            sprite + "1_22.png"   # Base
        ],
        "marche": [
            sprite + "1_23.png",  # Marche 1
            sprite + "1_24.png",  # Marche 2
            sprite + "1_25.png",  # Marche 3
            sprite + "1_22.png"   # Marche 4
        ],
        "attaque": [
            sprite + "1_48.png",  # Attaque 1
            sprite + "1_49.png",  # Attaque 2
            sprite + "1_50.png",  # Attaque 3
            sprite + "1_51.png"   # Attaque 4
        ]
    },

    "gauche": {
        "base": [
            sprite + "1_33.png"   # Base
        ],
        "marche": [
            sprite + "1_34.png",  # Marche 1
            sprite + "1_35.png",  # Marche 2
            sprite + "1_36.png",  # Marche 3
            sprite + "1_33.png"   # Marche 4
        ],
        "attaque": [
            sprite + "1_56.png",  # Attaque 1
            sprite + "1_57.png",  # Attaque 2
            sprite + "1_58.png",  # Attaque 3
            sprite + "1_59.png"   # Attaque 4
        ]
    }
}
