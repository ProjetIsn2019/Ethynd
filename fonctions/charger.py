# -*-coding:utf-8 -*
"""Fontions de Chargement
Fonctions dédiées à charger notre base de données de chemin d'images
Sous forme d'images Pygame
Auteur: Sofiane Djerbi + Dorian Voland
"""
import pygame as pg
from constantes import constantes_joueur as cj
from constantes import constantes_tuiles as ct
from constantes import constantes_partie as cp
from constantes import constantes_collisions as cc

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


def charger_sprites():
    """Charge les sprites
    Permets de charger les sprites des différents dictionnaires
    """
    for direction in cj.animation:  # Parcours des directions
        for mouvement in cj.animation[direction]:  # Parcours des mouvements
            numero = 0  # Compteur utilisé dans le parcours des sprites
            for sprite in cj.animation[direction][mouvement]:  # Parcourir images
                if isinstance(sprite, str):  # Si le sprite est un txt
                    img = pg.image.load(sprite).convert_alpha()  # Charger
                    cj.animation[direction][mouvement][numero] = img  # Sauver
                numero += 1  # Numéro du sprite actuel + 1 (Le compteur)
