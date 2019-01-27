import pygame as pg


hauteur_perso = 22
longueur_perso = 64
vitesse_perso = 4

touches_perso = {
	"gauche" : pg.K_LEFT,
	"droite" : pg.K_RIGHT,
	"haut" :   pg.K_UP,
	"bas" :	   pg.K_DOWN,
    "attaque" : pg.K_x
}

animation_perso = {
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
    ],
    "attaque_bas": [
        "images/sprites/sprite_1_44.png",  # attaque 0
        "images/sprites/sprite_1_45.png",  # attaque 1
        "images/sprites/sprite_1_46.png",  # attaque 2
        "images/sprites/sprite_1_47.png",  # attaque 3
        ],
    "attaque_droite": [
        "images/sprites/sprite_1_52.png",  # attaque 0
        "images/sprites/sprite_1_53.png",  # attaque 1
        "images/sprites/sprite_1_54.png",  # attaque 2
        "images/sprites/sprite_1_55.png",  # attaque 3
        ],
    "attaque_haut": [
        "images/sprites/sprite_1_48.png",  # attaque 0
        "images/sprites/sprite_1_49.png",  # attaque 1
        "images/sprites/sprite_1_50.png",  # attaque 2
        "images/sprites/sprite_1_51.png",  # attaque 3
        ],
    "attaque_gauche": [
        "images/sprites/sprite_1_56.png",  # attaque 0
        "images/sprites/sprite_1_57.png",  # attaque 1
        "images/sprites/sprite_1_58.png",  # attaque 2
        "images/sprites/sprite_1_59.png",  # attaque 3
        ]

}