# -*- coding: utf-8 -*-
"""Boucle et Events
Fonctions concernant le jeu et les évènements
Auteurs: Sofiane Dorian Anthony
"""
from constantes import constantes_partie as cp
from fonctions import charger
from classes import joueur
from classes import mapping
from classes import entitee
import pygame as pg
import time

def musique():
    cp.musique = pg.mixer.Sound("son/menu.ogg")  # Récuperer la musique sous forme de variable
    cp.musique.play(loops=-1)   # Jouer la musique (loops=-1 permet de la jouer en boucle indéfiniment)


def menu():
    image = pg.image.load("images/menu.png").convert()  # Charger l'image du menu
    cp.ecran.blit(image, (0, 0))  # Affiher l'image du menu
    menu = True  # Booléen indiquant si l'on est dans le menu
    while menu:  # Tant que le joueur est sur le menu
        #  ################### EVENEMENTS
        for evenement in pg.event.get():  # Je parcours les evenements
            if evenement.type == pg.KEYDOWN:  # Event : Touche enclenchée
                if evenement.key == pg.K_ESCAPE:  # Si touche = Echappe
                    menu = False  # On quitte
                elif evenement.key == pg.K_q:  # Si touche = q
                    menu = False  # On quitte
                elif evenement.key == pg.K_a:  # Si touche = a
                    menu = False  # On quitte
                    aide()
                elif evenement.key == pg.K_j:  # Si touche = j
                    menu = False
                    initialiser_jeu()
                    boucle_de_jeu()
            elif evenement.type == pg.QUIT:  # Event : Quitter la fenetre
                menu = False  # On quitte
        #  ################### EVENEMENTS
        cp.horloge.tick(cp.tps)  # 30 tick par seconde seront executés
        pg.display.update()  # On change de tick. On actualise l'écran.


def aide():
    image = pg.image.load("images/aide.png").convert()  # Charger l'image de l'aide
    cp.ecran.blit(image, (0, 0))  # Affiher l'image de l'aide
    aide = True  # Booléen indiquant si l'on est dans le menu
    while aide:  # Tant que le joueur est sur le menu
        #  ################### EVENEMENTS
        for evenement in pg.event.get():  # Je parcours les evenements
            if evenement.type == pg.KEYDOWN:  # Event : Touche enclenchée
                if evenement.key == pg.K_ESCAPE:  # Si touche = Echappe
                    aide = False
                    menu()
            elif evenement.type == pg.QUIT:  # Event : Quitter la fenetre
                aide = False  # On quitte
        #  ################### EVENEMENTS
        cp.horloge.tick(cp.tps)  # 30 tick par seconde seront executés
        pg.display.update()  # On change de tick. On actualise l'écran.


def initialiser_fenetre():
    pg.display.set_caption("Ethynd")  # Définition du titre de la fenêtre
    pg.display.set_icon(pg.image.load("images/icone.png"))  # Chargement de l'icone

    pg.mouse.set_visible(False)  # On cache la souris
    cp.ecran = pg.display.set_mode((cp.ecran_x, cp.ecran_y),  # On crée une fenêtre de la taille définie dans les constantes de partie
                                   pg.NOFRAME)
    cp.jouer = True  # On défini un booléen qui nous indique le statut de la partie
    cp.horloge = pg.time.Clock()  # L'horloge pour contrôler les tick par sec


def initialiser_jeu():
    charger.charger_tileset()  # Charger les images de tuiles
    charger.charger_sprite()  # Charger les images de sprites
    cp.map = mapping.Map("aventure", (-800, -1000), "aventure.ogg")  # Chargement de la map
    cp.perso = joueur.Joueur()  # Chargement du joueur
    #cp.monstre = entitee.Monstre("dragon_rouge", [50, 200], [57, 57], "aleatoire", 10, 1)


def boucle_de_jeu():
    while cp.jouer:  # Tant que le joueur joue
        """ Boucle de jeu
        Boucle de jeu: Gestion events, executée en boucle.
        1 éxécution = 1 tick.
        """
        cp.ecran.fill(cp.map.couleur_fond)  # Mettre la couleur de fond correspondant à la map
        cp.map.actualiser()
        cp.perso.lire_touches()  # Faire les déplacements/Animations du personnage
        #cp.monstre.deplacement()  # Effectuer le déplacement de tout les monstres
        cp.map.afficher_arriere_plan()  # Afficher l'arrière plan de la map
        cp.perso.afficher()  # Actualiser la position du personnage
        #cp.monstre.afficher()  # Afficher les monstres
        cp.map.afficher_premier_plan()  # Afficher le premier plan de la map
#  ################## EVENEMENTS
        for evenement in pg.event.get():  # Je parcours les evenements
            if evenement.type == pg.KEYDOWN:  # Event : Touche enclenchée
                if evenement.key == pg.K_ESCAPE:  # Si touche = Echappe
                    cp.jouer = False  # On quitte
            elif evenement.type == pg.QUIT:  # Event : Quitter la fenetre
                cp.jouer = False  # On quitte
#  ################### EVENEMENTS

        cp.horloge.tick(cp.tps)  # 30 tick par seconde seront executés
        pg.display.update()  # On change de tick. On actualise l'écran.
