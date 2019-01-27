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
    # [0, 0, "direction", "mouvement"]
    # Nombre de pixels en x, nombre de pixels en y, direction, mouvement.
    pg.K_UP:    [0, 3, "haut", "marche"],
    pg.K_LEFT:  [3, 0, "gauche", "marche"],
    pg.K_DOWN:  [0, -3, "bas", "marche"],
    pg.K_RIGHT: [-3, 0, "droite", "marche"],
    pg.K_z:     [0, 3, "haut", "marche"],
    pg.K_q:     [3, 0, "gauche", "marche"],
    pg.K_s:     [0, -3, "bas", "marche"],
    pg.K_d:     [-3, 0, "droite", "marche"]
}

animation = {
    # Animation marche : 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3 [...]
    "bas": [
        "images/sprites/sprite_1_00.png",  # Base
        "images/sprites/sprite_1_01.png",  # Marche1
        "images/sprites/sprite_1_02.png",  # Marche2
        "images/sprites/sprite_1_03.png",  # Marche3
    ],
    "droite": [
        "images/sprites/sprite_1_11.png",  # Base
        "images/sprites/sprite_1_12.png",  # Marche1
        "images/sprites/sprite_1_13.png",  # Marche2
        "images/sprites/sprite_1_14.png",  # Marche3
    ],
    "haut": [
        "images/sprites/sprite_1_22.png",  # Base
        "images/sprites/sprite_1_23.png",  # Marche1
        "images/sprites/sprite_1_24.png",  # Marche2
        "images/sprites/sprite_1_25.png",  # Marche3
    ],
    "gauche": [
        "images/sprites/sprite_1_33.png",  # Base
        "images/sprites/sprite_1_34.png",  # Marche1
        "images/sprites/sprite_1_35.png",  # Marche2
        "images/sprites/sprite_1_36.png",  # Marche3
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
