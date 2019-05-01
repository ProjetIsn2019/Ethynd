# -*- coding: utf-8 -*-
"""Les objets de collision
Objet "hitbox_collision" qui permets de créer une hitbox de collisions
Auteur : Sofiane Djerbi
"""
import pygame as pg
from constantes import constantes_collisions as cc


class Hitbox(pg.sprite.Sprite):  # La classe Hitbox hérite de pg.sprite.Sprite CAD qu'elle inclut les caracteristiques de pg.sprite.Sprite
    """Hitbox de collisions.
    Utilisé pour créer des collisions parfaites basées uniquement
    Sur la transparence d'une image
    """

    def __init__(self, groupe, rect=None, mask=None):
        """Création de la hitbox de collision
        Avec image, rectangle et hitbox correspondant
        Initialisé à "None" par défaut.
        Groupes possibles : "joueur", "block", "ennemi", "png"
        Tout les hitboxs créés seront sauvegardés automatiquement dans
        les listes du dictionnaire des constantes de collision
        """
        super().__init__()  # Initialisation de pg.sprite.Sprite
        # Ici "super()" fait référence a la classe mère (pg.sprite.Sprite ici)
        self.rect = rect    # Rectangle de la hitbox
        self.mask = mask    # "Mask" qui correspond au hitbox des collisions
        cc.groupes["tout"].add(self)  # Ajouter a la liste de tout les hitboxs
        cc.groupes[groupe].add(self)  # Ajouter a la liste correspondante

    def collision(self, groupe="tout"):
        """Vérifie les collisions avec un groupe (tout par défaut)
        Retourne True si il y a collision
        Retourne False si il n'y a pas de collisions
        """
        # Retourne le boolean fourni par la fonction qui Permets
        # De vérifier si il y a des collisions entre 1 hitbox et 1 groupe
        # De hitbox. pg.sprite.collide_mask signifie que l'on veut utiliser
        # les hitboxs
        return pg.sprite.spritecollideany(self, cc.groupes[groupe],
                                          pg.sprite.collide_mask)
