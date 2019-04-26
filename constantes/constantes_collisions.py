# -*- coding: utf-8 -*-
"""Les constantes de collision
Contient les groupes de collisions ainsi que les listes de collision
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
