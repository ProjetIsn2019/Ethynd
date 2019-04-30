# -*- coding: utf-8 -*-
"""Les listes de constantes concernant les collisions.
Groupes de collision etc.
(A IMPORTER)
Auteur : Le Groupe (Principalement Sofiane)
"""
import pygame as pg

groupes = {
    "tuile": pg.sprite.Group(),     # Liste des masques pour les tuiles
    "entite": pg.sprite.Group(),   # Liste des masques pour les entiees
    "joueur": pg.sprite.Group(),    # Liste des masques pour les joueurs
    "Monstre": pg.sprite.Group(),   # Liste des masques pour les ennemis
    "objet": pg.sprite.Group(),     # Liste des masques pour les objets
    "pnj": pg.sprite.Group(),       # Liste des masques pour les personnages non joueurs
    "tout": pg.sprite.Group()       # Liste des masques pour tout
}
