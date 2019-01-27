# -*-coding:utf-8 -*
"""Classe du Joueur Python
Cette classe sera dédiée au joueur, uniquement et pas les PNJs.
Auteur: Dorian Voland
"""
import pygame as pg
import os


class Joueur:
    def __init__(self, x_camera, y_camera, hauteur, largeur, vitesse, animation, touche):
        """Initialise le personnage
        """
        self.x = x_camera  # Coordonnées
        self.y = y_camera  # Coordonnées

        self.largeur = largeur  # Taille
        self.hauteur = hauteur  # Taille
        self.vitesse = vitesse  # Vitesse (pixel/sec)
        
        self.direction = "bas"  #direction par default
        self.mouvement = None
        self.libre = True
        self.animation = animation
        self.charger_sprite() # On initialise les animations (dictionnaire : self.animation)
        self.touches_perso = touche
       
        
        self.compteur_marche = 5 #initialise le compteur de marche (gere les animation (premier sprite du mouvement))
        self.compteur_action = 0

    def lecture_touche(self,touche, ecran, x_camera, y_camera):
        """Lis ce que le joueur fait
            On agit en conséquence, ex: si le joueur appuie en haut le
            sprite va en haut, etc.
        """
        # On vérifie les touches
        if self.libre: 
            if touche[self.touches_perso["attaque"]]:

                self.mouvement = "attaque"
                self.libre = False
                for clef, valeur in self.touches_perso.items():
                    self.direction = clef if touche[valeur] and clef != "attaque" else   self.direction
                    
            elif touche[self.touches_perso["gauche"]]: # Si la touche est gauche
                self.mouvement = "marche"                # Le personnage bouge
                x_camera += self.vitesse
                self.direction = 'gauche'            # Set la direction
            
            elif touche[self.touches_perso["droite"]]:
                x_camera -= self.vitesse
                self.direction = 'droite'
                self.mouvement = "marche"

            elif touche[self.touches_perso["haut"]]:
                y_camera += self.vitesse
                self.direction = 'haut'
                self.mouvement = "marche"

            elif touche[self.touches_perso["bas"]]:
                y_camera -= self.vitesse
                self.direction = 'bas'
                self.mouvement = "marche"

            else:
                self.direction = 'bas'
                self.mouvement = False
                
                


        return x_camera, y_camera #renvoie les coordoné de la camera

    def charger_sprite(self):
        """Charge les sprites
        Permets de charger les sprites du dictionnaire "info"
        """
        for mouvement in self.animation:  # Parcours des mouvements
            numero = 0  # Compteur utilisé dans le parcours des sprites
            for sprite in self.animation[mouvement]:  # Parcours des sprites
                if isinstance(sprite, str):  # Si le sprite est encore un texte
                    img = pg.image.load(sprite).convert_alpha()  # Charger Img
                    self.animation[mouvement][numero] = img  # Sauvegarder
                numero += 1  # Numéro du sprite actuel + 1


    def afficher(self, ecran):
        """Affiche le personnage
        Et gère ses animations
        """
         # Je capture les dimensions de la fenêtre actuelle
        y_decalage,x_decalage= -self.hauteur/2, -self.largeur/2  # Le décalage car l'image se génère

        x_centre, y_centre = ecran.get_width()/2 + x_decalage , ecran.get_height()/2 + y_decalage  
        #                    # Le x central              # Le y central
        if self.mouvement == "marche":
            compteur_marche = self.compteur_marche
            self.compteur_marche = compteur_marche + 1 if compteur_marche +1 < 20 else 0 #compteur de marche renitialise tout les 20px

            nombre = self.compteur_marche // 5  # On veut un nombre dans [0;3]

            sprite = self.animation[self.direction] # On met charge la liste de sprite 
            sprite = sprite[nombre]                 # On charge le sprite
            
            ecran.blit(sprite, (x_centre, y_centre)) # On colle l'image
        elif self.mouvement == "attaque":

            # Gestion du compteur
            self.compteur_action = self.compteur_action + 1 if self.compteur_action < 19 else 0
            # Pareil que plus haut
            
            if self.compteur_action == 0:  # Si l'animation est terminée
                self.libre = True# Libérer le bersonnage
                compteur_action = 0  # Choisir la tuile de base

            # Diviseur = 2 (Fréquence très rapide)
            nombre = self.compteur_action // 5  # On veut un nombre dans [3;7]
            animation = self.mouvement + "_" + self.direction
            sprite = self.animation[animation] # On met charge la liste de sprite 
            sprite = sprite[nombre]                 # On charge le sprite
            
            ecran.blit(sprite, (x_centre, y_centre)) # On colle l'image

        else:
            self.compteur_marche = 5 #on renitialise le compteur de marche

            sprite = self.animation[self.direction]  # On prend la liste
            sprite = sprite[0]  # On prend le bon sprite? 0 = sprite de base
            ecran.blit(sprite, (x_centre, y_centre))  # Affiche
