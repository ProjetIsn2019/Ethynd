# -*- coding: utf-8 -*-
"""Les listes de constantes concernant les entités
Variables etc.
(A IMPORTER)
Auteur : Le Groupe
"""

vitesse = 2

sprite_dragon = "images/sprites/dragon_rouge_"
sprite_chauve_souris = "images/sprites/chauve_souris_"
sprite_chat = "images/sprites/chat_"
sprite_oiseau = "images/sprites/oiseau_"
sprite_poussin = "images/sprites/poussin_"

timings = { # Timings des animations
    # [tick, images, libre, reset]
    # tick = le nombre de tick pour changer une frame (Tick entre chaque frame)
    # images = le nombre d'images de l'animation - 1 (0 compte comme une frame)
    # libre = Libérer le personnage après l'animation ? True = oui False = non
    # reset = revenir sur base après la fin de l'animation ? (Sinon on répète)
    "monstre" : {
        "dragon_rouge" : {

            "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
            "marche": [4, 3, True, False]
        },
        "chauve_souris" : {

            "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
            "marche": [4, 2, True, False]
        },
        "oiseau" : {

            "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
            "marche": [10, 2, True, False]
        },
        "chat" : {

            "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
            "marche": [10, 2, True, False]
        },
        "poussin":  {

            "base": [None],  # Si tick = None, alors il y a aucun attribut d'animation
            "marche": [8, 2, True, False]
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
        "chat" : {

            "bas" : {
                    "base": [
                        sprite_chat + "00.png"
                    ],
                    "marche": [
                        sprite_chat + "01.png",
                        sprite_chat + "00.png",
                        sprite_chat + "02.png",
                    ],
                },

            "droite" : {
                    "base": [
                        sprite_chat + "06.png",
                    ],
                    "marche": [
                        sprite_chat + "07.png",
                        sprite_chat + "06.png",
                        sprite_chat + "08.png",
                ],
            },
            "haut" : {
                    "base": [
                        sprite_chat + "09.png",
                    ],
                    "marche": [

                        sprite_chat + "10.png",
                        sprite_chat + "09.png",
                        sprite_chat + "11.png",
                ]
            },
            "gauche" : {

                    "base": [
                        sprite_chat + "03.png",
                    ],
                    "marche": [

                        sprite_chat + "04.png",
                        sprite_chat + "03.png",
                        sprite_chat + "05.png",
                ]
            }

        },
        "oiseau" : {

            "bas" : {
                    "base": [
                        sprite_oiseau + "00.png"
                    ],
                    "marche": [
                        sprite_oiseau + "01.png",
                        sprite_oiseau + "00.png",
                        sprite_oiseau + "02.png",

                    ],
                },

            "droite" : {
                    "base": [
                        sprite_oiseau + "06.png",
                    ],
                    "marche": [
                        sprite_oiseau + "07.png",
                        sprite_oiseau + "06.png",
                        sprite_oiseau + "08.png",
                ],
            },
            "haut" : {
                    "base": [
                        sprite_oiseau + "09.png",
                    ],
                    "marche": [

                        sprite_oiseau + "10.png",
                        sprite_oiseau + "09.png",
                        sprite_oiseau + "11.png",

                ]
            },
            "gauche" : {
                    "base": [
                        sprite_oiseau + "03.png",
                    ],
                    "marche": [

                        sprite_oiseau + "04.png",
                        sprite_oiseau + "03.png",
                        sprite_oiseau + "05.png",

                ],
            }

        },
        "poussin" : {

            "bas" : {
                    "base": [
                        sprite_poussin + "09.png",
                    ],
                    "marche": [
                        sprite_poussin + "10.png",
                        sprite_poussin + "09.png",
                        sprite_poussin + "11.png",
                ]
            },

            "droite" : {

                    "base": [
                        sprite_poussin + "06.png",
                    ],
                    "marche": [
                        sprite_poussin + "07.png",
                        sprite_poussin + "06.png",
                        sprite_poussin + "08.png",
                    ],
            },

            "haut" : {
                    "base": [
                        sprite_poussin + "00.png"
                    ],
                    "marche": [
                        sprite_poussin + "01.png",
                        sprite_poussin + "00.png",
                        sprite_poussin + "02.png",
                    ],
            },

            "gauche" : {
                    "base": [
                        sprite_poussin + "03.png",
                    ],
                    "marche": [

                        sprite_poussin + "04.png",
                        sprite_poussin + "03.png",
                        sprite_poussin + "05.png",
                ],
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
        "dragon_rouge" : {
            "coup" : "son/monstre/dragon_rouge.ogg"
        },
        "chauve_souris" : {
            "coup" : "son/monstre/chauve_souris.ogg"
        },
        "chat" : {
            "coup" : "son/monstre/chauve_souris.ogg"
        },
        "oiseau" : {
            "coup" : "son/monstre/chauve_souris.ogg"
        },
        "poussin" : {
            "coup" : "son/monstre/chauve_souris.ogg"
        }
    }
}
