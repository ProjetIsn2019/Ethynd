# -*-coding:utf-8 -*-
"""Classe du Joueur Python
Cette classe sera dédiée au joueur, uniquement et pas les PNJs.
Auteur: Dorian Voland
"""
from constantes import constantes_joueur as cj
from constantes import constantes_partie as cp
from constantes import constantes_collisions as cc
from classes import collision as col
import random as rd
import pygame as pg


class Joueur():  # L'objet joueur
    def __init__(self):
        """Initialise le personnage
        """
        self.sprite = None  # Sprite du personnage
        self.compteur = 0  # Compteur animations
        self.frame = 0     # Numero de la frame du sprite
        self.direction = "bas"   # Direction du personnage (bas par défaut)
        self.mouvement = "base"  # Mouvement actuel du joueur (base = debout)
        self.libre = True        # Si le personnage est pas occupé à faire qqch
        self.hitbox = col.Hitbox("joueur")  # Hitbox du joueur
        self.hitbox_objet = col.Hitbox("objet")  # Hitbox du joueur
        self.vie = 10  # Points de vie du personnage
        self.blesser = False  # Si le personnage est blessé ou non
        # Créer un rectangle centré sur les jambes du personnage pour les collisions
        self.hitbox.rect = pg.Rect((0, 0), (25, 20))
        self.hitbox.rect.center = (cp.centre_x, cp.centre_y+13)
        # Créer et assigner le hitbox
        self.hitbox.mask = pg.Mask((25, 20))
        self.hitbox.mask.fill()  # Remplir le hitbox pour créer un bloc

        self.channel_joueur = pg.mixer.Channel(2)

        # Créer un rectangle centré sur les jambes du personnage pour les collisions
        self.hitbox_objet.rect = pg.Rect((cp.centre_x-20, cp.centre_y+10), (32, 22))
        self.hitbox_objet.rect.center = (cp.centre_x-4, cp.centre_y-11)
        # Créer et assigner le hitbox
        self.hitbox_objet.mask = pg.Mask((32, 22))
        self.hitbox_objet.mask.fill()  # Remplir le hitbox pour créer un bloc



    def lire_touches(self):
        """Lis ce que le joueur fait
            On agit en conséquence, ex: si le joueur appuie en haut le
            sprite va en haut, etc.
        """
        touches = pg.key.get_pressed()  # Touches enfoncées
        if not self.libre:  # Si le personnage est occupé
            return          # Quitter la fonction
        if self.hitbox.mask is None:  # Si le hitbox est pas défini
            return  # Quitter la fonction pour éviter un déplacement précoce
        for touche in cj.touches:  # Je parcours les touches enfoncées
            if touches[touche]:  # Si la touche est définie dans constantes
                touche = cj.touches[touche]  # touche = sa liste correspondante

                if touche[2] is not None:  # Si l'animation change la direction
                    self.direction = touche[2]  # Modif direction
                if self.mouvement != touche[3]:  # Si le mouvement change
                    self.mouvement = touche[3]  # Changer le mouvement du perso
                    self.compteur = 0  # Recommencer les animations
                    self.frame = 0     # Réinitialiser les frames
                self.libre = touche[4]  # Changer disponibilité du perso

                # Capturer les déplacements
                x = touche[0]  # Nombre de pixels en x
                y = touche[1]  # Nombre de pixels en x
                # Déplacer le hitbox pour tester la position
                cp.map.bouger_hitbox(x, y)
                if self.hitbox.collision("tuile"):  # Si il y a collision:
                    # Annuler le déplacement de la hitbox de la map
                    cp.map.bouger_hitbox(-x, -y)
                else:  # Sinon, si il y a pas collision
                    cp.map.bouger(x, y)

                break  # Casser la boucle: Touche trouvée. On évite les autres

        else:  # Si la boucle n'est pas cassée: Aucune touche trouvée
            self.mouvement = "base"  # On dit qu'il n'y a aucun mouvement
            self.libre = True  # Perso libre car pas de mouvement

    def enlever_vie(self):
        """ Enleve de la vie au joueur si il prend des dégats
        """
        if self.hitbox.collision("Monstre") and not self.blesser:
            if not self.hitbox_objet.collision("Monstre"):
                self.son = pg.mixer.Sound(cj.son["blessure"])
                self.channel_joueur.play(self.son)
                self.blesser = True
                self.vie -= 1

        elif not self.hitbox.collision("Monstre") and self.blesser:
            self.blesser = False

    def attaquer(self):
        """ Déplace la hitbox de l'épée en fonction de la direction lors d'une attaque
        """
        if self.mouvement == "attaque":
            if self.direction == "bas":
                x = cp.centre_x + 10
                y = cp.centre_y + 30
                longueur =  32
                hauteur = 22
            elif self.direction == "gauche":
                x = cp.centre_x - 10
                y = cp.centre_y + 20
                longueur =  25
                hauteur = 32
            elif self.direction == "droite":
                x = cp.centre_x + 28
                y = cp.centre_y + 20
                longueur =  22
                hauteur = 32
            elif self.direction == "haut":
                x = cp.centre_x + 20
                y = cp.centre_y
                longueur =  32
                hauteur = 22

            hitbox = pg.Rect((x, y), (longueur, hauteur))

            self.hitbox_objet.rect = hitbox
            self.hitbox_objet.rect.center = (x- longueur/2, y - hauteur/2)
            # Créer et assigner le hitbox
            self.hitbox_objet.mask = pg.Mask((longueur, hauteur))
            self.hitbox_objet.mask.fill()  # Remplir le hitbox pour créer un bloc
            cc.groupes["objet"] = [self.hitbox_objet]
        else:
            cc.groupes["objet"] = []

    def actualiser_son(self):

        if self.mouvement == "attaque":
            if self.compteur == 0 and self.frame == 1:
                self.son = pg.mixer.Sound(cj.son["attaque"])
                self.channel_joueur.play(self.son)

        elif not self.channel_joueur.get_busy():
            if self.mouvement == "marche":
                self.son = pg.mixer.Sound(cj.son["marche"])
                self.channel_joueur.play(self.son)


    def actualiser_frame(self):
        # MISE A JOUR DES FRAMES EN FONCTION DES TICKS
        # On vérifie si il y a un nombre de tick entre frame défini
        if cj.timings[self.mouvement][0] is None:  # Si il y en a pas
            self.compteur = 0
            self.frame = 0
        else:  # Si il y en a un
            # Maintenant on incrémente le compteur des animations si besoin
            if self.compteur < cj.timings[self.mouvement][0]:
                self.compteur = self.compteur + 1
                # Sinon si il est déjà à son max
            else:
                self.compteur = 0  # On le reset
                # On incrémente la frame si besoin d'être incrémenté
                if self.frame < cj.timings[self.mouvement][1]:
                    self.frame = self.frame + 1
                    # Sinon si elle est déjà a son max
                else:
                    self.frame = 0  # Reset
                    self.libre = cj.timings[self.mouvement][2]  # Liberer perso
                    if cj.timings[self.mouvement][3]:  # Si on veux revenir
                        self.mouvement = "base"        # Sur base, on le fait

    def actualiser_sprite(self):
        """ Met à jour le sprite
        Mise à jour du sprite en fonction de:
            - La direction
            - Le mouvement
            - La frame
        """
        # CHARGEMENT DE L'IMAGE DU SPRITE
        # Charger la liste de sprites relative a la direction et le mouvement
        sprite = cj.animation[self.direction][self.mouvement]
        self.sprite = sprite[self.frame]  # Prendre le sprite correspondant
        cc.groupes["joueur"] = [self.hitbox]

    def interface(self):
        """ Affiche les information (uniquement vie pour l'instant)
        """
        pg.draw.rect(cp.ecran, (105, 0, 0), pg.Rect(0, 0, self.vie*20, 10))
        police = pg.font.SysFont("arial", 10)
        texte = police.render("Vie", True, (255, 255, 255))
        cp.ecran.blit(texte, (0,-2))

    def actualiser(self):
        """Actualise les stats du personnage"""
        self.enlever_vie()
        self.actualiser_frame()  # Actualiser les frames
        self.actualiser_sprite()  # Actualiser le sprite
        self.attaquer()
        self.actualiser_son()


        # Je calcule la position de rendu du sprite afin qu'il soit bien centré
        x_rendu = cp.centre_x - cj.hauteur_sprite/2  # Le x de rendu
        y_rendu = cp.centre_y - cj.largeur_sprite/2  # Le y de rendu

        cp.ecran.blit(self.sprite, (x_rendu, y_rendu))  # Affiche le sprite
