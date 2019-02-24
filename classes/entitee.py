import pygame as pg
from constantes import constantes_partie as cp
from constantes import constantes_tuiles as ct
from constantes import constantes_entitee as ce
from constantes import constantes_joueur as cj
from classes import collision as col
import random as rd
class Entitee(object):
    """Classe mere des entitee du jeu 
    comporte: - __init__()
              - charger_sprite()
              - mouvement()
              - afficher()
    """

    def __init__(self, id = None):
        """Initialise la classes entitee
        """ 
        self.pos_encienne_cam = [cp.map.x_camera, cp.map.y_camera]
        self.position = [cp.map.x_camera, cp.map.y_camera]
        self.id = id 
        self.taille = [0,0]

        self.compteur = 0  # Compteur animations
        self.compteur_action = 0
        self.frame = 0     # Numero de la frame du sprite
        self.sprite = None
        self.direction = "bas"   # Direction du personnage (bas par défaut)
        self.mouvement = "base"  # Mouvement actuel du joueur (base = debout)
        self.libre = True        # Si le personnage est pas occupé à faire qqch
        self.masque = col.Masque("entitee")  # Masque de l'entitee
        self.type_deplacement = "base"

        self.charger_sprite()
        self.chargement()

    def chargement():
        print("Chargement d'une entitee")

    def charger_sprite(self):
        """Charge les sprites
        Permets de charger les sprites du personnage
        """
        #charger sprite
        identifiant = self.id.split("_", 1)
        self.type = identifiant[0]
        self.id = identifiant[1]

        animation = ce.animation[self.type][self.id]

        for direction in animation:  # Parcours des directions
            for mouvement in animation[direction]:  # Parcours des move
                numero = 0  # Compteur utilisé dans le parcours des sprites
                for sprite in animation[direction][mouvement]:  # sprites
                    if isinstance(sprite, str):  # Si le sprite est un txt
                        img = pg.image.load(sprite).convert_alpha()  # Charger
                        animation[direction][mouvement][numero] = img  # Var
                    numero += 1  # Numéro du sprite actuel + 1

    def deplacement(self):
        """ Défini le mouvement de base
        pour une entitée la fait tourner sur elle meme
        """
        # On calcule le delta de la camera
        delta_x = cp.map.x_camera - self.pos_ancienne_cam[0] # calcule delta camera x
        delta_y = cp.map.y_camera - self.pos_ancienne_cam[1] # calcule delta camera y

        # On donne la nouvel position si la camera bouge
        self.position[0] = self.position[0] + delta_x           # On affecte la nouvelle position
        self.position[1] = self.position[1] + delta_y           # en x et y    

        # On actualise la camera
        self.pos_ancienne_cam = [cp.map.x_camera, cp.map.y_camera]  
                
    def actualiser_frame(self):
        # charge attribut mouvement en cours

        mouvement = ce.timings[self.type][self.id][self.mouvement] 

        # Si le monstre est immobile, retour des conteurs à 0
        if mouvement[0] is None :           
            self.compteur = 0       
            self.frame = 0
        else:
            # Maintenant on incrémente le compteur des animations si besoin
            if self.compteur < mouvement[0]:
                self.compteur = self.compteur + 1
            else :
                # On incremente le compteur de frame si besoins
                self.compteur = 0 
                if self.frame < mouvement[1]:
                    self.frame = self.frame + 1
                else:
                    # verifi si on libere l'entitée apres l'animation et reset frame
                    self.frame = 0
                    self.libre = mouvement[2] 
                    # une fois l'animation terminer, on efectue l'action suivante
                    if self.type_deplacement == "aleatoire":
                        self.compteur_action = rd.randint(0,3) 
                    else :
                        self.compteur_action +=1

                    if mouvement[3]:  # Si on veux revenir
                        self.mouvement = "base"        # Sur base, on le fait
    
    def actualiser_sprite(self):
        #charge les animations du mouvement
        animation = ce.animation[self.type][self.id][self.direction][self.mouvement]
        # On prend le bon sprite
        self.sprite = animation[self.frame]  
        # On actualise le masque
        self.masque.rect = self.sprite.get_rect(center=(self.position[0],
                                                        self.position[1]))
        # Créer et assigner le masque
        self.masque.mask = pg.mask.from_surface(self.sprite)

    def afficher(self):
        """ Procedure qui gere l'affichage de mon personnage
        Gère l'affichage des animations
        """
        self.actualiser_frame()
        self.actualiser_sprite()
        x = self.position[0]
        y = self.position[1]

        # Affiche le sprite
        cp.ecran.blit(self.sprite, (x, y))  



class Monstre(Entitee):
    """ Classe Monstre qui herite de Entitee
            redefini methode déplacement() ==> type_deplacement: - aleatoire
                                                                 - base
                                                                 - zone (en cours)
    """
    def __init__(self, id, position, type_deplacement):
        monstre = "monstre_"+ str(id)
        super(Monstre, self).__init__(monstre)
        self.position = position
        self.masque = col.Masque("Monstre")
        self.pos_ancienne_cam = [cp.map.x_camera, cp.map.y_camera]
        self.type_deplacement = type_deplacement

    def chargement(self):
        """ Procedure qui affiche le chargement d'un monstre
        """
        print("Chargement du monstre : " + self.id + "...")
        
    def deplacement(self):
        """ Gere deplacement d'un monstre
        """    
        if self.compteur_action >= len(ce.deplacement[self.type_deplacement]): # On reinitialise le compteur d'action
            self.compteur_action = 0
     
        # Charge le type deplacement
        action = ce.deplacement["base"][self.compteur_action]             
        self.mouvement = "marche"
        self.direction = action

        #Calcul du delta de la camera entre deux frame
        delta_x = cp.map.x_camera - self.pos_ancienne_cam[0] # Delta camera x
        delta_y = cp.map.y_camera - self.pos_ancienne_cam[1] # Delta camera y

        # Donne valeur du prochain deplacement
        x = self.position[0] + delta_x - ce.action[action][0] 
        y = self.position[1] + delta_y - ce.action[action][1]

        # cp.map.bouger_masque(x, y)
        # if self.masque.collision("tuile"):  # Si il y a collision:
        #     # Annuler le déplacement de la hitbox de la map
        #     cp.map.bouger_masque(-x, -y)
        # else:  # Sinon, si il y a pas collision

        # On actualise les positon
        self.position[0] = x  #en x
        self.position[1] = y  #en y

        # On actualise la camera
        self.pos_ancienne_cam = [cp.map.x_camera, cp.map.y_camera]

