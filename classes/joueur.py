# -*-coding:utf-8 -*
"""Classe du Joueur Python
Cette classe sera dédiée au joueur, uniquement et pas les PNJs.
Auteur: Dorian Voland
"""
from constantes import constantes_joueur as cj
from constantes import constantes_partie as cp
import pygame as pg


class Joueur:
    def __init__(self):
        """Initialise le personnage
        """
        self.largeur = 24  # Taille Largeur
        self.hauteur = 64  # Taille Hauteur
        self.compteur = 0  # Compteur animations
        self.frame = 0     # Numero de la frame du sprite
        self.direction = "bas"   # Direction du personnage (bas par défaut)
        self.mouvement = "base"  # Mouvement actuel du joueur (base = debout)
        self.libre = True        # Si le personnage est pas occupé à faire qqch

    def lire_touches(self):
        """Lis ce que le joueur faitle
            On agit en conséquence, ex: si le joueur appuie en haut le
            sprite va en haut, etc.
        """
        touches = pg.key.get_pressed()  # Touches enfoncées
        if not self.libre:  # Si le personnage est occupé
            return          # Quitter la fonction
        for touche in cj.touches:  # Je parcours les touches enfoncées
            if touches[touche]:  # Si la touche est définie dans constantes
                cp.map.x_camera += cj.touches[touche][0]  # Bouger camera
                cp.map.y_camera += cj.touches[touche][1]  # Bouger camera

                # Si l'animation a une direction
                if cj.touches[touche][2] is not None:
                    self.direction = cj.touches[touche][2]  # Modif direction
                # Si le mouvement change
                if self.mouvement != cj.touches[touche][3]:
                    self.mouvement = cj.touches[touche][3]  # Changer mouvement
                    self.compteur = 0  # Recommencer les animation
                self.libre = cj.touches[touche][4]  # Changer disponibilité
                break  # Casser la boucle: Touche trouvée. On évite les autres
        else:  # Si la boucle n'est pas cassée: Aucune touche trouvée
            self.mouvement = "base"  # On dit qu'il n'y a aucun mouvement

    def afficher(self, ecran):
        """Affiche le personnage
        Et gère ses animations
        """
        # Je capture les dimensions de la fenêtre actuelle
        # Et je calcule les points centraux (moyenne)
        y_decalage = -self.hauteur/2  # Le décalage car l'image se génère
        x_decalage = -self.largeur/2  # A partir de son côté haut gauche
        x_centre = ecran.get_width()/2 + x_decalage   # Le x central
        y_centre = ecran.get_height()/2 + y_decalage  # Le y central

        # On vérifie si il y a un nombre de tick entre frame défini
        if cj.timings[self.mouvement][0] is None:  # Si il y en a pas
            self.compteur = 0
            self.frame = 0
        else:  # Si il y en a un
            # Maintenant on incrémente le compteur des animations si besoin
            if self.compteur < cj.timings[self.mouvement][0]:
                self.compteur = self.compteur + 1
                # Sinon si il est déjà à son max
            elif self.compteur == cj.timings[self.mouvement][0]:
                self.compteur = 0  # On le reset
                # On incrémente la frame si besoin d'être incrémenté
                if self.frame < cj.timings[self.mouvement][1]:
                    self.frame = self.frame + 1
                    # Sinon si elle est déjà a son max
                elif self.frame == cj.timings[self.mouvement][1]:
                    self.frame = 0  # Reset
                    self.libre = cj.timings[self.mouvement][2]  # Liberer perso
                    if cj.timings[self.mouvement][3]:  # Si on veux revenir
                        self.mouvement = "base"        # Sur base, on le fait

        # Charger la liste de sprites relative a la direction et le mouvement
        sprite = cj.animation[self.direction][self.mouvement]
        sprite = sprite[self.frame]  # On prend le bon sprite
        ecran.blit(sprite, (x_centre, y_centre))  # Affiche le sprite
