# -*-coding:utf-8 -*

"""
classe du perso python
1ere etape: créer un personnage: Ethyn butal 
"""

import pygame
from pygame.locals import *


from fonctions import maps

class Perso(object):
    def __init__(self, x, y, width, heigth):
        """
        *initialise le personnage par:
            -sa taille (width, height)
            -ses coordonées(x, y)
        
        
        *posede 2 fonction : 
            -une qui gere __les deplacement: __lecture_touche()
            -une qui gere l'affichage du perso: __afficher(fenetre)
        
        ex: perso = perso(0, 0, 100, 100) genere personnage de 100*100 px
            perso.lectureTouche() deplace perso si appui sur une fleche
            perso.afficher() affiche le personnage a l'ecrant
            
            
        """
        self.x =  x
        self.y = y
        self.width = width #ici 90px
        self.heigth = heigth #ici 120 px
        self.vitesse = 5
        
        
    def lecture_touche(self):
        """
            lit les saisi clavier et reagie en consequant:
                -haut
                -bas
                -gauche
                -droite
        """
        fenetre_x = 640
        fenetre_y = 480

        touche = pygame.key.get_pressed()  #lecture touche pressée
        if touche[K_LEFT] and self.x > 0:       #si touche est -> 
            self.x -= self.vitesse       #deplacer de velociter pixel
        if touche[K_RIGHT] and self.x < fenetre_x-self.width:
           self.x += self.vitesse
        if touche[K_UP] and self.y > 0:
            self.y -= self.vitesse
        if touche[K_DOWN] and self.y <  fenetre_y - self.heigth: 
            self.y += self.vitesse
    
    def afficher(self, fenetre):
        """
            affiche le personnage
        """
        image_perso = pygame.image.load("link.png").convert_alpha()
        fenetre.blit(image_perso,(self.x, self.y))



if __name__ == "__main__":
    pygame.init()                          # on initialise pygame
    horloge = pygame.time.Clock()          # on initialise l'horloge

    
    run = True
    fenetre =  pygame.display.set_mode((fenetre_x,fenetre_y))
    pygame.display.set_caption("test personnage")              # on initialise la fenetre et la map
    map = maps.Map("maps/test.map") 
    
    perso = Perso(0, 0, 90, 120)         # on initialise le personnage
	
    while run : 
        horloge.tick(30)
        perso.lecture_touche()
        
        for event in pygame.event.get(): #event de fin
            if event.type == QUIT:
                run = False		
	
		# Chargement de la map
        #affichage des element a l'ecrant
        map.afficher(fenetre)
        perso.afficher(fenetre)
        pygame.display.update()
    pygame.quit()

			