# -*-coding:utf-8 -*
"""Fontions de Chargement
Fonctions dédiées à charger notre base de données de chemin d'images
Sous forme d'images Pygame
Auteur: Sofiane Djerbi
"""
import os
import pygame as pg
from constantes import constantes_joueur as cj
from constantes import constantes_tuiles as ct


def charger_tuiles():
    """ Initialiser les tuiles
    """
    print("Chargement des tuiles...")  # Logs
    # os.listdir retourne l'intégralité des fichiers d'un dossier en liste
    for fichier in os.listdir("images/tuiles/"):  # Je parcours les tuiles
        nom = fichier.replace("tuile_", "")   # On supprime le prefix
        nom = nom.replace(".png", "")         # On supprime l'extension
        # On supprime les 0 au début si le nom n'est pas "000"
        # Si c'est le cas alors on retourne 0. Donc "000" = "0"
        nom = nom.lstrip("0") if nom != "000" else "0"
        fichier = "images/tuiles/" + fichier  # Ajout du chemin relatif
        # J'ajoute les tuiles au dictionnaire + support transparence
        ct.tuiles[nom] = pg.image.load(fichier).convert_alpha()


def charger_sprite():
    """Charge les sprites
    Permets de charger les sprites du dictionnaire "info"
    """
    for direction in cj.animation:  # Parcours des directions
        for mouvement in cj.animation[direction]:  # Parcours des move
            numero = 0  # Compteur utilisé dans le parcours des sprites
            for sprite in cj.animation[direction][mouvement]:  # sprites
                if isinstance(sprite, str):  # Si le sprite est un txt
                    img = pg.image.load(sprite).convert_alpha()  # Charger
                    cj.animation[direction][mouvement][numero] = img  # Var
                numero += 1  # Numéro du sprite actuel + 1
