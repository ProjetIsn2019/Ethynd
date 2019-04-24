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
from classes import entitee
import pygame as pg


def musique():
    pg.mixer.Channel(1)
    cp.musique = pg.mixer.Sound("son/menu2.ogg")  # Récuperer la musique sous forme de variable
    cp.musique.play(loops=-1)   # Jouer la musique (loops=-1 permet de la jouer en boucle indéfiniment)


def menu():
    musique = pg.mixer.Channel(1)
    son = pg.mixer.Sound("son/selection_menu.ogg")  # Récuperer l'effet musical de séléction
    musique.play(son)  # Le jouer
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
    musique = pg.mixer.Channel(1)
    son = pg.mixer.Sound("son/selection_menu.ogg")  # Récuperer l'effet musical de séléction
    musique.play(son)  # Le jouer
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


def initialiser_fenetre():
    pg.display.set_caption("Ethynd")  # Définition du titre de la fenêtre
    pg.display.set_icon(pg.image.load("images/icone.png"))  # Chargement de l'icone

    pg.mouse.set_visible(False)  # On cache la souris
    cp.ecran = pg.display.set_mode((cp.ecran_x, cp.ecran_y),  # On crée une fenêtre de la taille définie dans les constantes de partie
                                   pg.NOFRAME)
    cp.jouer = True  # On défini un booléen qui nous indique le statut de la partie
    cp.horloge = pg.time.Clock()  # L'horloge pour contrôler les tick par sec


def initialiser_jeu():
    son = pg.mixer.Sound("son/selection_menu.ogg")  # Récuperer l'effet musical de séléction
    son.play()  # Le jouer
    charger.charger_tileset()  # Charger les images de tuiles
    charger.charger_sprite()  # Charger les images de sprites
    cp.map = mapping.Map("aventure", (-800, -1000), "aventure.ogg")  # Chargement de la map
    cp.perso = joueur.Joueur()  # Chargement du joueur
    charger.charger_monstre()
    #cp.monstre = entitee.Monstre("dragon_rouge", [50, 200], [57, 57], "aleatoire", 10, 1)
    boucle_de_jeu()  # Lancer la partie

def boucle_fin():
    cp.musique.stop()
    musique()

    i = 0
    if cp.perso.vie < 1:
        image = pg.image.load("images/menu/menu_mort.jpg").convert()  # Charger l'image du menu
    else:
        image = pg.image.load("images/menu/menu_fin.png").convert()  # Charger l'image du menu
        
    cp.ecran.blit(image, (0, 0))  # Affiher l'image du menu
    while True or i < 180:  # Boucle infinie
        i += 1
        #  ################### EVENEMENTS
        for evenement in pg.event.get():  # Je parcours les evenements
            if evenement.type == pg.KEYDOWN:  # Event : Touche enclenchée
                return menu()
            elif evenement.type == pg.QUIT:  # Event : Quitter la fenetre
                return  # On quitte
        #  ################### EVENEMENTS
        cp.horloge.tick(cp.tps)  # 30 tick par seconde seront executés
        pg.display.update()  # On change de tick. On actualise l'écran.


def boucle_de_jeu():
    jeux = True
    while jeux:  # Tant que le joueur joue
        """ Boucle de jeu
        Boucle de jeu: Gestion events, executée en boucle.
        1 éxécution = 1 tick.
        """
        if cp.perso.vie < 1:
            jeux = False
        if cc.groupes["Monstre"] == []:
            jeux = False
        cp.ecran.fill(cp.map.couleur_fond)  # Mettre la couleur de fond correspondant à la map
        cp.map.actualiser()
        cp.perso.lire_touches()  # Faire les déplacements/Animations du personnage
        #cp.monstre.deplacement()  # Effectuer le déplacement de tout les monstres
        cp.map.afficher_arriere_plan()  # Afficher l'arrière plan de la map
        cp.perso.actualiser()  # Actualiser la position du personnage
        #cp.monstre.afficher()  # Afficher les monstres
        charger.gerer_monstres()
        cp.map.afficher_premier_plan()  # Afficher le premier plan de la map
        cp.perso.interface()
#  ################## EVENEMENTS
        for evenement in pg.event.get():  # Je parcours les evenements
            if evenement.type == pg.KEYDOWN:  # Event : Touche enclenchée
                if evenement.key == pg.K_ESCAPE:  # Si touche = Echappe
                    return  # On quitte
            elif evenement.type == pg.QUIT:  # Event : Quitter la fenetre
                    return  # On quitte
#  ################### EVENEMENTS
        cp.horloge.tick(cp.tps)  # 30 tick par seconde seront executés
        pg.display.update()  # On change de tick. On actualise l'écran.
    
    boucle_fin()

        