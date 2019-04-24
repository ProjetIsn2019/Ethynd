# -*-coding:utf-8 -*
"""Fontions de Chargement
Fonctions dédiées à charger notre base de données de chemin d'images
Sous forme d'images Pygame
Auteur: Sofiane Djerbi
"""
import pygame as pg
from constantes import constantes_joueur as cj
from constantes import constantes_tuiles as ct
from constantes import constantes_partie as cp
from constantes import constantes_collisions as cc
from classes.monstre import Monstre

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
    for direction in cj.animation:  # Parcours des directions
        for mouvement in cj.animation[direction]:  # Parcours des mouvements
            numero = 0  # Compteur utilisé dans le parcours des sprites
            for sprite in cj.animation[direction][mouvement]:  # Parcourir imgs
                if isinstance(sprite, str):  # Si le sprite est un txt
                    img = pg.image.load(sprite).convert_alpha()  # Charger
                    cj.animation[direction][mouvement][numero] = img  # Sauver
                numero += 1  # Numéro du sprite actuel + 1 (Le compteur)


def charger_monstre(id_niveau = "niveau_1"):
    """ Céer des monstres d'une liste 
    """
    liste_monstre = []
    masqueMonstre = []

    for type_monstre in cp.niveau[id_niveau]:
        liste_monstre.append(type_monstre)

    for type_monstre in liste_monstre:
        for liste_parametre in cp.niveau[id_niveau][type_monstre]:
            
            monstre = Monstre(type_monstre, liste_parametre)
            cp.entites_liste.append(monstre)

    for entite in cp.entites_liste:
        entite.deplacement()
        entite.afficher()
        masqueMonstre.append(entite.masque)
    masqueMonstre = masqueMonstre
    
def gerer_monstres():
    """
    * Gere les montres:
    *  - ajoute leurs masques
    *  - les deplaces
    *  - les affiches
    *
    """
    masqueMonstre = []

    for entite in cp.entites_liste:
        if entite.vie > 0:
            if entite.masque.collision("objet"):
                entite.vie -= 1
                entite.jouer_son("hit")
            entite.deplacement()
            entite.afficher()
            masqueMonstre.append(entite.masque)
    cc.groupes["Monstre"] = masqueMonstre

