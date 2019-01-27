# -*- coding: utf-8 -*-
"""Les listes de sprites
Sprites, animations
Etc.
(A IMPORTER)
"""
import pygame as pg

vitesse = 3

touches = {  # Les touches pour les déplacements
    # [0, 0, "direction", "mouvement", "libre"]
    # Nombre de pixels en x, nombre de pixels en y, direction, mouvement.
    pg.K_UP:    [0, vitesse, "haut", "marche", True],
    pg.K_LEFT:  [vitesse, 0, "gauche", "marche", True],
    pg.K_DOWN:  [0, -vitesse, "bas", "marche", True],
    pg.K_RIGHT: [-vitesse, 0, "droite", "marche", True],
    pg.K_SPACE: [0, 0, None, "saut", True],
    pg.K_w:     [0, 0, None, "attaque", False]
}

animation = {
    # Animation marche : 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3 [...]
    "bas": [
        "images/sprites/sprite_1_00.png",  # Base
        "images/sprites/sprite_1_01.png",  # Marche 1
        "images/sprites/sprite_1_02.png",  # Marche 2
        "images/sprites/sprite_1_03.png",  # Marche 3
        "images/sprites/sprite_1_44.png",  # Attaque 1
        "images/sprites/sprite_1_45.png",  # Attaque 2
        "images/sprites/sprite_1_46.png",  # Attaque 3
        "images/sprites/sprite_1_47.png"   # Attaque 4
    ],
    "droite": [
        "images/sprites/sprite_1_11.png",  # Base
        "images/sprites/sprite_1_12.png",  # Marche 1
        "images/sprites/sprite_1_13.png",  # Marche 2
        "images/sprites/sprite_1_14.png",  # Marche 3
        "images/sprites/sprite_1_52.png",  # Attaque 1
        "images/sprites/sprite_1_53.png",  # Attaque 2
        "images/sprites/sprite_1_54.png",  # Attaque 3
        "images/sprites/sprite_1_55.png"   # Attaque 4
    ],
    "haut": [
        "images/sprites/sprite_1_22.png",  # Base
        "images/sprites/sprite_1_23.png",  # Marche 1
        "images/sprites/sprite_1_24.png",  # Marche 2
        "images/sprites/sprite_1_25.png",  # Marche 3
        "images/sprites/sprite_1_48.png",  # Attaque 1
        "images/sprites/sprite_1_49.png",  # Attaque 2
        "images/sprites/sprite_1_50.png",  # Attaque 3
        "images/sprites/sprite_1_51.png"   # Attaque 4
    ],
    "gauche": [
        "images/sprites/sprite_1_33.png",  # Base
        "images/sprites/sprite_1_34.png",  # Marche 1
        "images/sprites/sprite_1_35.png",  # Marche 2
        "images/sprites/sprite_1_36.png",  # Marche 3
        "images/sprites/sprite_1_56.png",  # Attaque 1
        "images/sprites/sprite_1_57.png",  # Attaque 2
        "images/sprites/sprite_1_58.png",  # Attaque 3
        "images/sprites/sprite_1_59.png"   # Attaque 4
    ]
}
