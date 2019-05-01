# -*- coding: utf-8 -*-
"""Boucle et Events
Fonctions concernant le jeu et les évènements
Auteurs: Sofiane Dorian Anthony
"""
from constantes import constantes_partie as cp
from constantes import constantes_collisions as cc
from fonctions import charger
from classes import joueur
from classes import mapping
from classes import entite
import pygame as pg

def initialiser_fenetre():
    pg.display.set_caption("Ethynd")  # Définition du titre de la fenêtre
    pg.display.set_icon(pg.image.load("images/icone.png"))  # Chargement de l'icone

    pg.mouse.set_visible(False)  # On cache la souris
    cp.ecran = pg.display.set_mode((cp.ecran_x, cp.ecran_y),  # On crée une fenêtre de la taille définie dans les constantes de partie
                                   pg.NOFRAME)
    cp.jouer = True  # On défini un booléen qui nous indique le statut de la partie
    cp.horloge = pg.time.Clock()  # L'horloge pour contrôler les tick par sec


def initialiser_jeu():
    chargement()  # J'affiche l'écran de chargement
    charger.charger_tileset()  # Charger les images de tuiles
    charger.charger_sprites()  # Charger les images de sprites
    cp.map = mapping.Map("maison", (14, 93), "maison.ogg")  # Chargement de la map
    cp.map.charger_monstres()
    cp.perso = joueur.Joueur()  # Chargement du joueur
    boucle_de_jeu()  # Lancer la partie

def initialiser_musique():
    pg.mixer.pre_init(44100, -16, 2, 1024)  # Réglages du mixeur pygame (fréquence (Hz), nombre de bits, channel, taille du buffer)
    pg.mixer.init()  # Initialisation du mixeur audio pygame
    pg.mixer.set_num_channels(8)
    pg.mixer.Channel(1)
    cp.musique = pg.mixer.Sound("son/menu.ogg")  # Récuperer la musique sous forme de variable
    cp.musique.play(loops=-1)   # Jouer la musique (loops=-1 permet de la jouer en boucle indéfiniment)


def menu():
    son = pg.mixer.Sound("son/selection_menu.ogg")  # Récuperer l'effet musical de séléction
    son.play()  # Le jouer
    image = pg.image.load("images/menu/menu.png").convert()  # Charger l'image du menu
    cp.ecran.blit(image, (0, 0))  # Affiher l'image du menu
    while True:  # Boucle infinie
        #  ################### EVENEMENTS
        for evenement in pg.event.get():  # Je parcours les evenements
            if evenement.type == pg.KEYDOWN:  # Event : Touche enclenchée
                if evenement.key == pg.K_ESCAPE:  # Si touche = Echappe
                    return  # On quitte la fonction menu
                elif evenement.unicode == "q":  # Si touche = q
                    return  # On quitte la fonction menu
                elif evenement.unicode == "a":  # Si touche = a
                    return aide()  # Quitter la fonction menu et appeller la fonction aide
                elif evenement.unicode == "j":  # Si touche = j
                    return initialiser_jeu()  # Quitter la fonction menu et appeller la fonction init_jeu
            elif evenement.type == pg.QUIT:  # Event : Quitter la fenetre
                return  # On quitte
        #  ################### EVENEMENTS
        cp.horloge.tick(cp.tps)  # 30 tick par seconde seront executés
        pg.display.update()  # On change de tick. On actualise l'écran.


def aide():
    son = pg.mixer.Sound("son/selection_menu.ogg")  # Récuperer l'effet musical de séléction
    son.play()
    image = pg.image.load("images/menu/aide.png").convert()  # Charger l'image de l'aide
    cp.ecran.blit(image, (0, 0))  # Affiher l'image de l'aide
    while True:  # Boucle infinie
        for evenement in pg.event.get():  # Je parcours les evenements
            if evenement.type == pg.KEYDOWN:  # Event : Touche enclenchée
                if evenement.key == pg.K_ESCAPE:  # Si touche = Echappe
                    return menu()  # Quitter la fonction aide pour aller dans la fonction menu
            elif evenement.type == pg.QUIT:  # Event : Quitter la fenetre
                return  # Quitter aide

        cp.horloge.tick(cp.tps)  # 30 tick par seconde seront executés
        pg.display.update()  # On change de tick. On actualise l'écran.

def chargement():
    son = pg.mixer.Sound("son/selection_menu.ogg")  # Récuperer l'effet musical de séléction
    son.play()  # Le jouer
    image = pg.image.load("images/menu/chargement.png").convert()  # Charger l'image de l'aide
    cp.ecran.blit(image, (0, 0))  # Affiher l'image de l'aide
    pg.display.update()

def mort():
    cp.musique.stop()
    image = pg.image.load("images/menu/mort.png").convert()  # Charger l'image de mort
    cp.ecran.blit(image, (0, 0))  # Affiher l'image en question
    while True:  # Boucle infinie
        for evenement in pg.event.get():  # Je parcours les evenements
            if evenement.type == pg.KEYDOWN:  # Event : Touche enclenchée
                if evenement.key == pg.K_ESCAPE:  # Si touche = Echappe
                    return  # Quitter la fonction
            elif evenement.type == pg.QUIT:  # Event : Quitter la fenetre
                return  # Quitter
        cp.horloge.tick(cp.tps)  # 30 tick par seconde seront executés
        pg.display.update()  # On change de tick. On actualise l'écran.

def gerer_monstres():
    """  DORIAN
    * Gere les montres:
    *  - les deplaces
    *  - les affiches
    *  - enlève de la vie
    """
    for entite in cp.entites_liste:
        if entite.vie > 0:
            if entite.hitbox.collision("objet"):
                entite.vie -= 1
                entite.jouer_son("coup")
            entite.deplacement()
            entite.afficher()

def boucle_de_jeu():
    while True:  # Tant que le joueur joue
        """ SOFIANE Boucle de jeu
        Boucle de jeu: Gestion events, executée en boucle.
        1 éxécution = 1 tick.
        """

        cp.ecran.fill((32, 23, 41))  # On met une couleur de fond noir
        cp.perso.lire_touches()  # Faire les déplacements/Animations du personnage
        cp.map.actualiser()  # On actualise les tuiles animés de la maps
        cp.map.afficher_arriere_plan()  # Afficher l'arrière plan de la map
        gerer_monstres()  # Déplacer, afficher les monstres
        cp.perso.actualiser()  # Actualiser la position du personnage
        cp.map.afficher_premier_plan()  # Afficher le premier plan de la map
        cp.perso.interface()
#  ################## EVENEMENTS
        for evenement in pg.event.get():  # Je parcours les evenements
            if evenement.type == pg.KEYDOWN:  # Event : Touche enclenchée
                if evenement.key == pg.K_ESCAPE:  # Si touche = Echappe
                    return  # On quitte
            elif evenement.type == pg.QUIT:  # Event : Quitter la fenetre
                    return  # On quitte
        # EVENEMENT NON PYGAME (SI LE PERSONNAGE MEURT ETC):
        teleportation()  # Faire les téléportations
        if cp.perso.vie < 1:  # Si le personnage n'as plus de vie
            return mort()
#  ################### EVENEMENTS
        cp.horloge.tick(cp.tps)  # 30 tick par seconde seront executés
        pg.display.update()  # On change de tick. On actualise l'écran.

def teleportation():
    """ ANTHONY / SOFIANE
    Téléporte le joueur et éxecute des choses a certain endroit de la map
    """
    if cp.map.nom is "maison":  # Si le joueur est dans la maison
        if 110 <= cp.map.x_camera <= 146 and -249 <= cp.map.y_camera <= -235:
            chargement()
            cp.map = mapping.Map("aventure", (-464, -261), "aventure.ogg")  # Chargement de la map aventure
            cp.map.charger_monstres()
        elif -19 <= cp.map.x_camera <= 26 and -180 <= cp.map.y_camera <= -168:
            chargement()
            cp.map = mapping.Map("grotte", (-416, -180), "grotte.ogg")  # Chargement de la map grotte
            cp.map.charger_monstres()

    elif cp.map.nom is "grotte":  # Si le joueur est dans la grotte
        if 133 <= cp.map.x_camera <= 220 and -610 <= cp.map.y_camera <= -600:  # SI LE JOUEUR SORS DE LA GROTTE
            chargement()
            cp.map = mapping.Map("aventure", (-1103, -460), "aventure.ogg")  # Chargement de la map aventure
            cp.map.charger_monstres()
        elif -434 <= cp.map.x_camera <= -398 and -138 <= cp.map.y_camera <= -111:  # Si le joueur rentre dans la maison
            chargement()
            cp.map = mapping.Map("maison", (0, -125), "maison.ogg")  # Chargement de la map maison
            cp.map.charger_monstres()

    elif cp.map.nom is "aventure":  # Si le nom de la map est "aventure" (elif au cas ou on veut ajouter encore des maps)
        if -467 <= cp.map.x_camera <= -461 and -255 <= cp.map.y_camera <= -237:  # SI LE JOUEUR RENTRE DANS LA MAISON
            chargement()
            cp.map = mapping.Map("maison", (128, -234), "maison.ogg")  # Chargement de la map maison
            cp.map.charger_monstres()
        elif -1106 <= cp.map.x_camera <= -1100 and -451 <= cp.map.y_camera <= -430:  # SI LE JOUEUR RENTRE DANS LA GROTTE
            chargement()
            cp.map = mapping.Map("grotte", (175, -591), "grotte.ogg")  # Chargement de la map maison
            cp.map.charger_monstres()
