# -*-coding:utf-8 -*
"""Classe du Joueur Python
Cette classe sera dédiée au joueur, uniquement et pas les PNJs.
Auteur: Dorian Voland
"""
import pygame as pg
import os
from fonctions import constants

class Joueur:
    def __init__(self, x, y):
        """Initialise le personnage
        """
        self.x = x  # Coordonnées
        self.y = y  # Coordonnées

        self.width = 64  # Taille
        self.heigth = 64  # Taille
        self.vitesse = 3  # Vitesse
        self.sprite_base = pg.image.load("images/sprites/hero_bas (1).png").convert_alpha()  # Image

        self.init_animation()
        self.right = False
        self.left = False
        self.up = False
        self.down = False

        self.compteur_marche = 5

    def lecture_touche(self, ecran):
        """Lis ce que le joueur fait
            On agit en conséquence, ex: si le joueur appuie en haut le
            sprite va en haut, etc.
        """

        fenetre_x = ecran.get_width()  # La largeur de l'écran
        fenetre_y = ecran.get_height()  # La hauteur de l'écran

        touche = pg.key.get_pressed()  # On vérifie les touches
        if touche[pg.K_LEFT] and self.x > 0:  # Si touche est enfoncée
            self.x -= self.vitesse  # Déplacer le personnage
            #                       # Pareil pour le reste..
            self.right = False      #variable de animation
            self.left = True
            self.up = False
            self.down = False

        elif touche[pg.K_RIGHT] and self.x < fenetre_x - self.width:
            self.x += self.vitesse
            self.right = True
            self.left = False
            self.up = False
            self.down = False

        elif touche[pg.K_UP] and self.y > 0:
            self.y -= self.vitesse
            self.right = False
            self.left = False
            self.up = True
            self.down = False

        elif touche[pg.K_DOWN] and self.y < fenetre_y - self.heigth:
            self.y += self.vitesse
            self.right = False
            self.left = False
            self.up = False
            self.down = True
        else:
            self.right = False
            self.left = False
            self.up = False
            self.down = False

    def init_animation(self):
        """
            fonction qui revoie une liste des animation avec leur sprite:
                    key = ['bas', 'bas_triste', 'bas_main', 
                    'droite', 'droite_triste', 'droite_main', 
                    'haut', 'haut_triste', 'haut_main',
                    'gauche', 'gauche_triste', 'gauche_main', 
                    'bas_attaque', 'haut_attaque', 'droite_attaque', 'gauche_attaque']
        """
        print("Chargement des animations...")
        self.animation = {}
        

        for animation in os.listdir("images/sprites/"):

            sprite = []
            
            nom = animation.replace("hero_", "")                # On supprime le prefix
            nom = nom.replace(".png", "")                       # On supprime l'extension
            nom_temp = nom.split(" ")                           # On separe le nombre et le nom

            nom_animation = nom_temp[0]                         # On recupere le nom
            fichier = "images/sprites/" + animation 
            image = pg.image.load(fichier).convert_alpha()      # Image est loader
            

            
            if not nom_animation in self.animation.keys():      # Si c'est la premiere sprite, on ajoute au dictionnaire le sprite
                sprite.append(image)
                self.animation[nom_animation] = sprite
            
            else:                                               # Sinon on ajoute l'image a la liste corespondant a la clef
                sprite += self.animation[nom_animation]
                sprite.append(image)
                self.animation[nom_animation] = sprite

        # print("key: ", self.animation.keys())

    def afficher(self, fenetre):
        """
            fonction qui gere les animation du personnage
        """
        if self.compteur_marche + 1 > 15:           #compteur de marche renitialise tout les 20px
            self.compteur_marche = 0

        if self.right :     #animation droite       #si le personnage va à droite alors jouer l'animation droite
            sprite = self.animation["droite"]       #sprite prend la liste contenu dans le dictionnaire
            self.compteur_marche +=1               

            fenetre.blit(sprite[self.compteur_marche//5], (self.x, self.y)) #toute les 5 tours de boucle, on change d'image

        elif self.left :    #animation gauche
            sprite = self.animation["gauche"]   
            self.compteur_marche +=1
            fenetre.blit(sprite[self.compteur_marche//5], (self.x, self.y))
        elif self.up:       #animation haut
            sprite = self.animation["haut"]
            
            self.compteur_marche +=1
            fenetre.blit(sprite[self.compteur_marche//5], (self.x, self.y))
        elif self.down:      #animation bas
            sprite = self.animation["bas"]
           
            self.compteur_marche +=1
            fenetre.blit(sprite[self.compteur_marche//5], (self.x, self.y))
        else:
            self.compteur_marche = 5                                           #remet le compteur a 5 (premeir splite de mouvement)

            fenetre.blit(self.sprite_base, (self.x, self.y))                   # on reviens en position standart si rien ne ce passe
    
