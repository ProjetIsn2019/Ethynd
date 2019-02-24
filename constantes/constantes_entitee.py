vitesse = 3

entitees_liste = [
		"dragon_rouge"
	]

sprite = "images/sprites_ennemie/dragon_rouge/sprite_dragon_rouge"

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
    	}
    }
}
action = {
    "haut":    [0, vitesse, "haut", "marche", True],
    "gauche":  [vitesse, 0, "gauche", "marche", True],
    "bas":  [0, -vitesse, "bas", "marche", True],
    "droite": [-vitesse, 0, "droite", "marche", True],
    "attaque":     [0, 0, None, "attaque", False]
}
deplacement = {
    "base" : [
        "droite", "bas", "gauche", "haut"
    ],
    "aleatoire" : [
    		0,1,2,3
        
    ],
    "focus" : [
    ]

}
animation = {
	
	"monstre" : {

		"dragon_rouge" : {

			"bas" : {
					"base": [
						sprite + "00.png"
					],
					"marche": [ 
						sprite + "00.png",
						sprite + "01.png",
						sprite + "02.png",
						sprite + "03.png"
					],
				},

			"gauche" : {
					"marche": [
				sprite + "04.png",
				sprite + "05.png",
				sprite + "06.png",
				sprite + "07.png"
				],
			},	
			"droite" : {
					"marche": [
				sprite + "08.png",
				sprite + "09.png",
				sprite + "10.png",
				sprite + "11.png"
				],
			},	
			"haut" : {
					"marche": [
				sprite + "12.png",
				sprite + "13.png",
				sprite + "14.png",
				sprite + "15.png"
				]
			}

		}
	}
}