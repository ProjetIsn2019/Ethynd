# -*- coding: utf-8 -*-
"""Les listes utiles, constantes
Sprites, animations
Tuiles avec interaction
Tuiles avec collision
Tuiles d'eau
(A IMPORTER)
"""
import pygame as pg

touches = {  # Les touches pour les déplacements
    # [0, 0, "direction", "mouvement", "libre"]
    # Nombre de pixels en x, nombre de pixels en y, direction, mouvement.
    pg.K_UP:    [0, 3, "haut", "marche", True],
    pg.K_LEFT:  [3, 0, "gauche", "marche", True],
    pg.K_DOWN:  [0, -3, "bas", "marche", True],
    pg.K_RIGHT: [-3, 0, "droite", "marche", True],
    pg.K_z:     [0, 3, "haut", "marche", True],
    pg.K_q:     [3, 0, "gauche", "marche", True],
    pg.K_s:     [0, -3, "bas", "marche", True],
    pg.K_d:     [-3, 0, "droite", "marche", True],
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

collision = (  # Liste des blocs sur lesquels on ne peux pas aller
    "16",
    "17",
    "38",
    "39",
    "162",
    "165",
    "183",
    "184",
    "185",
    "186",
    "187",
    "205",
    "206",
    "207",
    "208",
    "209",
    "226",
    "227",
    "228",
    "229",
    "230"
)

eau = (
    "167",
    "168",
    "169",
    "170",
    "171",
    "172",
    "173",
    "174",
    "189",
    "190",
    "191",
    "192",
    "193",
    "194",
    "195",
    "196",
    "210",
    "211",
    "212",
    "213",
    "214",
    "215",
    "216",
    "217",
    "231",
    "232",
    "233",
    "234",
    "235",
    "236",
    "237",
    "238",
    "251",
    "252",
    "253",
    "254",
    "255",
    "256",
    "257",
    "258",
    "271",
    "272",
    "273",
    "274",
    "275",
    "276",
    "277",
    "278"
)
