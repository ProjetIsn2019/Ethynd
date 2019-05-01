# -*- coding: utf-8 -*-
"""Objet monstre
Créer des monstres, ennemis.
Auteur : Dorian Voland
"""
import pygame as pg
import random as rd

from constantes import constantes_partie as cp
from constantes import constantes_entite as ce
from constantes import constantes_collisions as cc
from classes import entite as ent
from classes import collision as col


class Monstre(ent.Entite):
    """ Classe Monstre qui herite de Entite
            redefini methode déplacement() ==> type_deplacement: - aleatoire
                                                                 - base
                                                                 - zone (en cours)
    """
    nb_monstre = 0
    def __init__(self, type_monstre, parametre):
        """
            * parametre =  [position, taille, type_deplacement, vie, attaque]
        """
        Monstre.nb_monstre +=1  # On augemente le nombre de monstre
        monstre = "monstre_" + type_monstre  # Préparation du nom du monstre pour l'initialisation
        super(Monstre, self).__init__(monstre)  # Initialisation de la superclasse
        # Mise en place des différents paramètres..
        x, y = parametre[0]  # Coordonnées relatives a la map
        x += cp.map.x_camera
        y += cp.map.y_camera
        self.position = [x, y]
        self.taille = parametre[1]
        self.type_deplacement = parametre[2]
        self.vie = parametre[3]
        self.attaque = parametre[4]
        ################
        self.son = None  # Le son du monstre
        self.hitbox = col.Hitbox("Monstre")  # Les collisions du monstre
