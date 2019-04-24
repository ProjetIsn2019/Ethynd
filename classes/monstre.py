import pygame as pg
import random as rd

from constantes import constantes_partie as cp
from constantes import constantes_entitee as ce
from constantes import constantes_collisions as cc
from classes import entitee as ent
from classes import collision as col


class Monstre(ent.Entitee):
    """ Classe Monstre qui herite de Entitee
            redefini methode déplacement() ==> type_deplacement: - aleatoire
                                                                 - base
                                                                 - zone (en cours)
    """
    nb_monstre = 0
    def __init__(self, type_monstre, parametre):
        """
            * parametre =  [position, taille ,type_deplacement, vie, attaque] 
        """
        Monstre.nb_monstre +=1
        monstre = "monstre_"+ type_monstre
        super(Monstre, self).__init__(monstre)
        self.position = parametre[0]
        self.taille = parametre[1]
        self.type_deplacement = parametre[2]
        self.vie = parametre[3]
        self.attaque = parametre[4]
        self.son = None
        self.masque = col.Masque("Monstre")
    
    def chargement(self):
        """ Procedure qui affiche le chargement d'un monstre
        """
        print("Chargement du monstre : " + self.id + "...")