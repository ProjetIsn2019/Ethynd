# -*-coding:utf-8 -*
"""Classe du Joueur Python
Cette classe sera dédiée au joueur, uniquement et pas les PNJs.
Auteur: Dorian Voland
"""
import pygame as pg
from fonctions import info


class Joueur:
    def __init__(self, x, y):
        """Initialise le personnage
        """
        self.x = x  # Coordonnées
        self.y = y  # Coordonnées
        self.largeur = 24  # Taille Largeur
        self.hauteur = 64  # Taille Hauteur
        self.direction = "bas"  # Direction du personnage (bas par défaut)
        self.mouvement = None  # Mouvement actuel du joueur (None = aucun)
        self.charger_sprite()  # On charge les sprites

    def bouger(self, ecran, x_camera, y_camera):
        """Lis ce que le joueur fait
            On agit en conséquence, ex: si le joueur appuie en haut le
            sprite va en haut, etc.
        """
        bool = True  # Boolean pour savoir si la boucle s'execute pas
        touches = pg.key.get_pressed()  # Touches enfoncées
        for touche in info.touches:  # Je parcours les touches enfoncées
            if touches[touche]:  #
                x_camera += info.touches[touche][0]  # On actualise les var
                y_camera += info.touches[touche][1]  # Etc..
                self.direction = info.touches[touche][2]
                self.mouvement = info.touches[touche][3]
                bool = False  # La boucle s'est executée
        if bool:  # Si la boucle ne s'est pas executé (bool est sur true)
            self.mouvement = None  # On dit qu'il n'y a aucun mouvement
        return x_camera, y_camera  # Renvoi des coordonnées de la camera

    def charger_sprite(self):
        """Charge les sprites
        Permets de charger les sprites du dictionnaire "info"
        """
        for mouvement in info.animation:  # Parcours des mouvements
            numero = 0  # Compteur utilisé dans le parcours des sprites
            for sprite in info.animation[mouvement]:  # Parcours des sprites
                if isinstance(sprite, str):  # Si le sprite est encore un texte
                    img = pg.image.load(sprite).convert_alpha()  # Charger Img
                    info.animation[mouvement][numero] = img  # Sauvegarder
                numero += 1  # Numéro du sprite actuel + 1

    def afficher(self, ecran):
        """Affiche le personnage
        Et gère ses animations
        """

        if self.mouvement is not None:  # Si le joueur est en mouvement
            # Gestion du compteur
            compteur = self.compteur  # Pour plus de visibilité
            self.compteur = compteur + 1 if compteur < 20 - 1 else 0
            # Le compteur augemente si on est en dessous de 19
            # Si on atteind 19 on rénitialise le compteur à 0
            # Car le prochain nombre est 19 et compteur < 20 est rempli donc
            # On utilise compteur < 19 pour éviter d'avoir un trop gros nombre
            nombre = self.compteur // 5  # On veut un nombre dans [0;3]
            sprite = info.animation[self.direction]  # On prend la liste
            sprite = sprite[nombre]  # On prend le bon sprite
            ecran.blit(sprite, (self.x, self.y))  # On affiche

        else:  # On reviens en position standart si rien ne ce passe
            self.compteur = 0  # Pas de compteur de marche

            sprite = info.animation[self.direction]  # On prend la liste
            sprite = sprite[0]  # On prend le bon sprite? 0 = sprite de base
            ecran.blit(sprite, (self.x, self.y))  # Affiche
