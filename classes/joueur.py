# -*-coding:utf-8 -*
"""Classe du Joueur Python
Cette classe sera dédiée au joueur, uniquement et pas les PNJs.
Auteur: Dorian Voland
"""
from constantes import constantes_joueur as cj
from constantes import constantes_partie as cp
from classes import collision as col
import pygame as pg


class Joueur():  # L'objet joueur hérite de la classe Sprite
    def __init__(self):
        """Initialise le personnage
        """
        self.compteur = 0  # Compteur animations
        self.frame = 0     # Numero de la frame du sprite
        self.direction = "bas"   # Direction du personnage (bas par défaut)
        self.mouvement = "base"  # Mouvement actuel du joueur (base = debout)
        self.libre = True        # Si le personnage est pas occupé à faire qqch
        self.masque = col.Masque("joueur")  # Masque du joueur

    def lire_touches(self):
        """Lis ce que le joueur faitle
            On agit en conséquence, ex: si le joueur appuie en haut le
            sprite va en haut, etc.
        """
        touches = pg.key.get_pressed()  # Touches enfoncées
        if not self.libre:  # Si le personnage est occupé
            return          # Quitter la fonction
        if self.masque.mask is None:  # Si le masque est pas défini
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
                # Déplacer le masque pour tester la position
                cp.map.bouger_masque(x, y)
                if self.masque.collision("tuile"):  # Si il y a collision:
                    # Annuler le déplacement de la hitbox de la map
                    cp.map.bouger_masque(-x, -y)
                else:  # Sinon, si il y a pas collision
                    cp.map.x_camera += x  # Bouger la camera en x
                    cp.map.y_camera += y  # Bouger la camera en y

                break  # Casser la boucle: Touche trouvée. On évite les autres

        else:  # Si la boucle n'est pas cassée: Aucune touche trouvée
            self.mouvement = "base"  # On dit qu'il n'y a aucun mouvement
            self.libre = True  # Perso libre car pas de mouvement

    def sprite(self):
        """ Retourne le sprite et le met à jour """
        # Charger la liste de sprites relative a la direction et le mouvement
        sprite = cj.animation[self.direction][self.mouvement]
        sprite = sprite[self.frame]  # Prendre le sprite correspondant
        # Mettre à jour le rectangle du masque en créant un rectangle centré
        self.masque.rect = sprite.get_rect(center=(cp.centre_x,
                                                   cp.centre_y))
        # Créer et assigner le masque
        self.masque.mask = pg.mask.from_surface(sprite)
        return sprite  # Retourner le sprite

    def afficher(self):
        """Affiche le personnage
        Et gère ses animations
        """
        # Je calcule la position de rendu du sprite afin qu'il soit bien centré
        x_rendu = cp.centre_x - cj.hauteur_sprite/2  # Le x de rendu
        y_rendu = cp.centre_y - cj.largeur_sprite/2  # Le y de rendu

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

        sprite = self.sprite()  # Charger le bon sprite
        cp.ecran.blit(sprite, (x_rendu, y_rendu))  # Affiche le sprite
