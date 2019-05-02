# -*- coding: utf-8 -*-
"""Les maps
Objet "Entité" qui correspond a un "être vivant" à l'échelle du jeu
Auteur: Dorian Voland
"""
import pygame as pg
import random as rd

from constantes import constantes_partie as cp
from constantes import constantes_entite as ce
from constantes import constantes_collisions as cc
from classes import collision as col

class Entite():
    """Classe mere des entités du jeu
    Une entité est un personnage animé par le jeu directement
    C'est souvent décoratif ou pour mettre en place des combats
    """

    def __init__(self, id=None):
        """Initialise la classes entite
        """
        self.pos_ancienne_cam = [cp.map.x_camera, cp.map.y_camera]
        self.position = [cp.map.x_camera, cp.map.y_camera]
        self.id = id
        self.taille = [1, 1]
        self.compteur = 0  # Compteur animations
        self.compteur_action = 0
        self.frame = 0     # Numero de la frame du sprite
        self.sprite = None
        self.direction = "bas"   # Direction du personnage (bas par défaut)
        self.mouvement = "base"  # Mouvement actuel du joueur (base = debout)
        self.libre = True        # Si le personnage est pas occupé à faire qqch
        self.type_deplacement = "base"

        self.channel_entite = pg.mixer.Channel(3)
        self.charger_sprite()

    def jouer_son(self, le_son):
        if not self.channel_entite.get_busy():
            self.son = pg.mixer.Sound(ce.son[self.type][self.id][le_son])
            self.channel_entite.play(self.son)

    def charger_sprite(self):
        """Charge les sprites
        Permets de charger les sprites du personnage
        """
        #charger sprite
        identifiant = self.id.split("_", 1)
        self.type = identifiant[0]
        self.id = identifiant[1]

        animation = ce.animation[self.type][self.id]

        for direction in animation:  # Parcours des directions
            for mouvement in animation[direction]:  # Parcours des move
                numero = 0  # Compteur utilisé dans le parcours des sprites
                for sprite in animation[direction][mouvement]:  # sprites
                    if isinstance(sprite, str):  # Si le sprite est un txt
                        img = pg.image.load(sprite).convert_alpha()  # Charger
                        animation[direction][mouvement][numero] = img  # Var
                    numero += 1  # Numéro du sprite actuel + 1

    def bouger_hitbox(self, coord):
        """ Gere le mouvement de la hitbox
        """
        self.hitbox.rect = self.sprite.get_rect(center=(self.position[0] + coord[0] + self.taille[0]/2,
                                                        self.position[1] + coord[1] + self.taille[1]/2))
        self.hitbox.mask = pg.Mask((self.taille[0], self.taille[1]))
        self.hitbox.mask.fill()  # Remplir le hitbox pour créer un bloc

        # pg.draw.rect(cp.ecran, (255,0,0), self.hitbox.rect)
    def deplacement(self):
        """ Défini le mouvement de base
        pour une entitée la fait tourner sur elle meme
        """
        if self.hitbox.mask is None:  # Si le hitbox est pas défini
            return  # Quitter la fonction pour éviter un déplacement précoce

        if self.compteur_action >= len(ce.deplacement[self.type_deplacement]): # On reinitialise le compteur d'action
            self.compteur_action = 0

        # Charge le type deplacement
        action = ce.deplacement["base"][self.compteur_action]
        self.mouvement = "marche"
        self.direction = action

        #Calcul du delta de la camera entre deux frame
        delta_x = cp.map.x_camera - self.pos_ancienne_cam[0] # Delta camera x
        delta_y = cp.map.y_camera - self.pos_ancienne_cam[1] # Delta camera y

        #Donne la valeur des deplacement ex: + 4 px
        deplacement_x = ce.action[action][0]  # en x
        deplacement_y = ce.action[action][1]  # en y

        # Donne la position du prochain déplacement
        x = self.position[0] + delta_x + deplacement_x
        y = self.position[1] + delta_y + deplacement_y

        # On bouge le hitbox a cette emplacement
        self.bouger_hitbox((deplacement_x, deplacement_y))
        if not self.hitbox.collision("tuile"):  # S'il n'y a pas:
            # On actualise les positon
            self.position[0] = x   #en x
            self.position[1] = y  #en y
        else:
            self.position[0] = x - deplacement_x   #en x
            self.position[1] = y - deplacement_y #en y
        self.bouger_hitbox((-deplacement_x, -deplacement_y))

        # On actualise la camera
        self.pos_ancienne_cam = [cp.map.x_camera, cp.map.y_camera]


    def actualiser_frame(self):
        # charge attribut mouvement en cours

        mouvement = ce.timings[self.type][self.id][self.mouvement]

        # Si le monstre est immobile, retour des conteurs à 0
        if mouvement[0] is None :
            self.compteur = 0
            self.frame = 0
        else:
            # Maintenant on incrémente le compteur des animations si besoin
            if self.compteur < mouvement[0]:
                self.compteur = self.compteur + 1
            else :
                # On incremente le compteur de frame si besoins
                self.compteur = 0
                if self.frame < mouvement[1]:
                    self.frame = self.frame + 1
                else:
                    # verifi si on libere l'entitée apres l'animation et reset frame
                    self.frame = 0
                    self.libre = mouvement[2]
                    # une fois l'animation terminer, on efectue l'action suivante
                    if self.type_deplacement == "aleatoire":
                        self.compteur_action = rd.randint(0,3)
                    else :
                        self.compteur_action +=1

                    if mouvement[3]:  # Si on veux revenir
                        self.mouvement = "base"        # Sur base, on le fait

    def actualiser_sprite(self):
        #charge les animations du mouvement
        animation = ce.animation[self.type][self.id][self.direction][self.mouvement]
        # On prend le bon sprite
        self.sprite = animation[self.frame]
        # On actualise le hitbox
        self.bouger_hitbox((0, 0))


    def afficher(self):
        """ Procedure qui gere l'affichage de mon personnage
        Gère l'affichage des animations
        """
        self.actualiser_frame()
        self.actualiser_sprite()
        x = self.position[0]
        y = self.position[1]

        # Affiche le sprite
        cp.ecran.blit(self.sprite, (x, y))
