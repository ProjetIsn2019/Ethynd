vitesse = 3

entitees_liste = [
        "dragon_rouge"
    ]

sprite_dragon = "images/sprites_ennemi/dragon_rouge/sprite_dragon_rouge"
sprite_chauve_souris = "images/sprites_ennemi/chauve_souris/sprite_chauve_souris"
sprite_joueur = "images/sprites/sprite_"

son_chauve_souris = "son/monstre/dragon_rouge_"
son_dragon_rouge = "son/monstre/chauve_souris_"
marche = ""
hit = "hit.ogg"

timings = { # Timings des animations
    # [tick, images, libre, reset]
    # tick = le nombre de tick pour changer une frame (Tick entre chaque frame)
    # images = le nombre d'images de l'animation - 1 (0 compte comme une frame)
    # libre = Libérer le personnage après l'animation ? True = oui False = non
    # reset = revenir sur base après la fin de l'animation ? (Sinon on répète)
    "monstre" : {
        "dragon_rouge" : {

            "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
            "marche": [4, 3, True, False],
            "attaque": [2, 3, True, True]
        },
        "chauve_souris" : {

            "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
            "marche": [4, 2, True, False],
            "attaque": [2, 2, True, True]
        }
    }
}
action = {
    "haut":    [0, -vitesse, "haut", "marche", True],
    "gauche":  [-vitesse, 0, "gauche", "marche", True],
    "bas":  [0, vitesse, "bas", "marche", True],
    "droite": [vitesse, 0, "droite", "marche", True],
    "attaque":     [0, 0, None, "attaque", False]
}
deplacement = {
    "base" : [
        "haut", "gauche", "bas", "droite"
    ],
    "trajet" : [
        "droite", "gauche", "bas", "droite"
    ],
    "aleatoire" : [
            0,1,2,3

    ],
    "focus" : [
    ]

}
animation = {
    
    "monstre" : {
        "chauve_souris" : {

            "bas" : {
                    "base": [
                        sprite_chauve_souris + "00.png"
                    ],
                    "marche": [ 
                        sprite_chauve_souris + "01.png",
                        sprite_chauve_souris + "02.png",
                        sprite_chauve_souris + "03.png",
                        sprite_chauve_souris + "04.png"
                    ],
                },

            "droite" : {
                    "base": [
                        sprite_chauve_souris + "04.png",
                    ],
                    "marche": [
                
                sprite_chauve_souris + "05.png",
                sprite_chauve_souris + "06.png",
                sprite_chauve_souris + "07.png"
                ],
            },  
            "haut" : {
                    "base": [
                        sprite_chauve_souris + "08.png",
                    ],
                    "marche": [
                sprite_chauve_souris + "09.png",
                sprite_chauve_souris + "09.png",
                sprite_chauve_souris + "11.png"
                ],
            },  
            "gauche" : {
                    "base": [
                        sprite_chauve_souris + "12.png",
                    ],
                    "marche": [
                
                sprite_chauve_souris + "13.png",
                sprite_chauve_souris + "14.png",
                sprite_chauve_souris + "15.png"
                ]
            }

        },

        "dragon_rouge" : {

            "bas" : {
                    "base": [
                        sprite_dragon + "00.png"
                    ],
                    "marche": [ 
                        sprite_dragon + "00.png",
                        sprite_dragon + "01.png",
                        sprite_dragon + "02.png",
                        sprite_dragon + "03.png"
                    ],
                },

            "gauche" : {
                    "marche": [
                sprite_dragon + "04.png",
                sprite_dragon + "05.png",
                sprite_dragon + "06.png",
                sprite_dragon + "07.png"
                ],
            },  
            "droite" : {
                    "marche": [
                sprite_dragon + "08.png",
                sprite_dragon + "09.png",
                sprite_dragon + "10.png",
                sprite_dragon + "11.png"
                ],
            },  
            "haut" : {
                    "marche": [
                sprite_dragon + "12.png",
                sprite_dragon + "13.png",
                sprite_dragon + "14.png",
                sprite_dragon + "15.png"
                ]
            }

        }
    }
}
son = {
    "monstre" : {
        "chauve_souris" : {
            "hit" : son_chauve_souris + hit,
        },
        "dragon_rouge" : {
            "hit" : son_dragon_rouge + hit,
        }
    }
}
