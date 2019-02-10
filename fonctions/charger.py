# -*-coding:utf-8 -*
"""Fontions de Chargement
Fonctions dédiées à charger notre base de données de chemin d'images
Sous forme d'images Pygame
Auteur: Sofiane Djerbi
"""
import pygame as pg
from constantes import constantes_joueur as cj
from constantes import constantes_tuiles as ct


def charger_tileset():
    """Charger un tileset
    Associe a chaque tuiles d'un tileset un ID, divise un tileset
    en plusieurs lignes
    Permets de bosser avec Tiled
    """
    # Charger l'image du tileset
    img = pg.image.load("images/tuiles/tileset.png").convert_alpha()
    img_largeur, img_hauteur = img.get_size()  # Prendre les dimensions
    id = 0  # J'initialise les IDs
    for y in range(int(img_hauteur/32)):  # Je parcours les lignes
        for x in range(int(img_largeur/32)):  # Je parcours les colonnes
            rectangle = (x*32, y*32, 32, 32)  # Je divise les tuiles de l'image
            # J'ajoute au dictionnaire des tuiles
            ct.tuiles[str(id)] = img.subsurface(rectangle)
            id += 1  # J'incrémente les IDs


def charger_sprite():
    """Charge les sprites
    Permets de charger les sprites du dictionnaire "info"
    """
    # Parcourir les animations PUIS les collisions
    for type in (cj.animation, cj.collision):
        for direction in type:  # Parcours des directions
            for mouvement in type[direction]:  # Parcours des move
                numero = 0  # Compteur utilisé dans le parcours des sprites
                for sprite in type[direction][mouvement]:  # sprites
                    if isinstance(sprite, str):  # Si le sprite est un txt
                        img = pg.image.load(sprite).convert_alpha()  # Charger
                        type[direction][mouvement][numero] = img  # Var
                    numero += 1  # Numéro du sprite actuel + 1
