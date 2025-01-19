# ########## imports des autres classes ##########
from actions import Actions
from command import Command
from item import Item
from player import Player
from room import Room
from ssroom import SSRoom

########### Création de la classe Game et setup pour le lancement du jeu ##########
class Game:
    def __init__(self):
        self.isdead = False
        self.player = None 
        self.floors = [] 
        self.Rooms = []
        self.commands = {}

########## Instanciation des pièces/ss-pièces/objets (création "spécifique") ##########
    def setup(self):

# Etages du manoir

        self.floors.append(self.Rooms)

# Salles du rez-de-chausée

        couloir_rdc= Room("Couloir", "Evelyn Westwood, ivre, vient d’avoir un accident de voiture. Il pleut, elle aperçoit une lumière dans la nuit. Elle s’en approche et tombe sur l’entrée d’un manoir. La grille est entre-ouverte, Evelyn se glisse dans l’ouverture et court en titubant jusqu’à la porte principale. Elle toque ; personne ne répond. Elle attrape la poignée, ouvre la porte qui n’était donc pas verrouillée et se précipite à l’intérieur pour se mettre à l’abri. Elle se trouve devant un cadre chaleureux, une large et belle entrée éclairée de centaines de bougies rayonnent et illuminent son passage. Evelyn crie pour signaler sa présence aux propriétaires des lieux, évoquant son accident et s’excusant pour l’intrusion, tout en à appelant l’aide. Aucune réponse…")
        piece_centrale = Room("Pièce_centrale","Evelyn s’approche du milieu de la pièce et se retrouve d’un coup sous un magnifique lustre, décoré de petites boules de Noël et enlacé de guirlandes qui resplendissent en contraste à la sombre nuit qui s’abat dehors sous la pluie.")
        salle_monstres_rdc = Room("Pièce_dont_la_porte_est_légèrement_ouverte","‘Chambre de Sophie’, est-il écrit sur la porte. Evelyn pénètre dans la mystérieuse chambre. Celle-ci est plutôt sombre et totalement en désordre. Des traces de moisissures tapissent les murs, une armoire à moitié détruite est renversée sur le côté, et surtout, un trou béant gît au milieu du lit posé au centre de la pièce.")
        cuisine = Room("Cuisine", "Evelyn entre dans une spacieuse cuisine à l’américaine, dont elle semble avoir toujours souhaité qu’elle fut la sienne. Un brin de mélancolie s’empare d’elle… ")
        escaliers_caches = Room("Escaliers_derrière_la_cuisine","Il y avait bien quelque chose derrière la cuisine : des escaliers. Evelyn se dit qu’ils mènent peut-être au sous-sol. Il doit bien y avoir un générateur de secours en-bas.")
        salon = Room("Salon","Evelyn arrive dans le salon. Ce n’est pas l’espace qui manque dans cette pièce – les décorations non plus d’ailleurs. Le centre de la pièce est occupé par trois éléments qu’Evelyn a toujours voulu avoir chez elle : un canapé en ‘U’ faisant le tour du salon, un écran plat gigantesque et une belle  et grande table basse que n’aurait pas reniée la salle à manger.")
        toilettes_rdc = Room("Toilettes","Traversant la porte des toilettes, Evelyn vomit. Elle se précipite vers le lavabo et commence à se mettre de l’eau sur le visage, se demandant si les effets des verres de trop ne commenceraient pas à se faire sentir.")
        salle_a_manger = Room("Salle_à_manger","Evelyn s’avance vers la salle à manger. Cinq chaises bien décorées sont disposées autour d’une fastueuse table garnie d’un repas qui a l’air d’avoir bien trop longtemps attendu les invités. Des mouches volent au-dessus des fruits tandis que des insectes dévorent copieusement le plat de Beef Wellington placé au milieu de la table. Quel gâchis...") 
        chambre_camille = Room("Chambre_de_Camille","La chambre est verrouillée. Sur la porte, il est écrit ‘Camille’ de manière stylisée, le prénom formant de jolies arabesques.")
        chambre_victor = Room("Chambre_de_Victor","La chambre est verrouillée. Sur la porte, le prénom ‘Victor’, écrit à la verticale et anthropomorphisé, se promène en tenant un chien en laisse.")

        # self.Rooms.append(couloir_rdc) on ne souhaite pas afficher Couloir avec l'action start
        self.Rooms.append(piece_centrale)
        self.Rooms.append(salle_monstres_rdc)
        self.Rooms.append(cuisine)
        # self.Rooms.append(escaliers_caches)
        self.Rooms.append(salon)
        self.Rooms.append(toilettes_rdc)
        self.Rooms.append(salle_a_manger)
        self.Rooms.append(chambre_camille)
        self.Rooms.append(chambre_victor)

# Endroits à fouiller dans chaque pièce du rez-de-chausée

        # Couloir (endroits accessibles = les autres pièces)
        # Pièce centrale
        table_nappee = SSRoom("Table_nappée","Une belle table nappée")
        armoire_a_vaiselle = SSRoom("Armoire_à_vaisselle","Une armoire remplie de vaisselle")
        radiateur = SSRoom("Radiateur","Un radiateur allumé")
        # Chambre porte ouverte
        armoire_sophie = SSRoom("Armoire","Une armoire renversée et à moitié détruite")
        coin_sophie = SSRoom("Coin_de_la_chambre","Un coin sombre de la chambre")
        trou_sophie = SSRoom("Trou_dans_le_lit","Un trou béant au milieu du lit sale")
        # Cuisine
        frigo_rdc = SSRoom("Réfrigérateur","Un frigo banal de bonne taille")
        four_rdc = SSRoom("Four","Un four éteint")
        etagere_droite = SSRoom("Etagères_côté_droit","Une étagère dans la partie droite de la cuisine")
        etagere_gauche = SSRoom("Etagères_côté_gauche","Une étagère dans la partie gauche de la cuisine")
        mur_cuisine = SSRoom("Fissures_dans_le_mur","De grandes fissures dans le mur derrière le frigo")
        # Escaliers cachés derrière la cuisine
        escaliers_vers_cave = SSRoom("Escaliers_cachés_derrière_la_cuisine","Une entrée cachée derrière le frigo")
        # Salon
        canape_salon = SSRoom("Canapé","Un canapé occupant tout le salon")
        tele_salon = SSRoom("Télévision","Une écran plat géant placé devant le canapé")
        table_salon = SSRoom("Table_basse","Une table basse assez grande")
        # Toilettes 
        miroir_toilettes_rdc = SSRoom("Miroir","Un miroir avec une tâche rouge au milieu")
        cuvette_rdc = SSRoom("Cuvette_des_toilettes","Cuvette ordinaire")
        # Salle à manger
        table_manger = SSRoom("Table_garnie_de_mets_pourris","Une grande table avec un festin pourri")
        chaise_manger = SSRoom("Chaise_avec_une_radio_posée_dessus","Une radio émettant des bruits sourds, posée sur une chaise")
        # Chambre de Camille (seulement description pièce)
        # Chambre de Victor (seulement description pièce)

# Objets de chaque sous-pièce de la pièce centrale
        # table nappée
        carte_rdc = Item("Carte_du_rez-de-chaussée","Il s'agit de la carte du rez-de-chaussée.")
        # armoire à vaiselle
        vitre_a_casser = Item("Vitre_cassable","Une vitre qui semble fragile")
        trousse_soins = Item("Trousse_de_soins","Une trousse de soins en cas de besoin")
        # radiateur
        se_chauffer = Item("Se_chauffer","Il est allumé et encore chaud.")
# Objets de chaque sous-pièce de la salle_monstres
        # armoire_sophie
        rien_sophie = Item("Rien","Rien mis à part des babioles fracassées et des vêtements déchirés")
        # coin_sophie
        cafard = Item("Trou_dans_le_coin","Un cafard sort subitement du trou.")
        # trou_sophie
        grillage = Item("Grillage","Un grillage au milieu du lit donne sur un petit pavé de ruelle sombre par le haut. Un petit enfant passe dans la ruelle, s’arrête, tourne lentement sa tête défigurée vers le haut et plonge son regard pâle et inexpressif dans celui du joueur. Il sourit en montrant ses dents pointues, puis s’en va...")
# Objets de chaque sous-pièce de la cuisine
        # frigo
        photo_cuisine = Item("Photo","Une photo de trois enfants un garçon et deux filles sur la porte")
        pommes_cuisine = Item("Pommes","Des pommes pourries")
        revolver_cuisine = Item("Revolver","Un revolver congelé et inutilisable")
        # four
        rien_cuisine = Item("Rien","Rien qu’une indescriptible odeur de nostalgie")
        # étagères droit
        piege_souris = Item("Piège_à_souris","Un piège à souris classique")
        # étagères gauche
        rien = Item("Rien","Il n'y a absolument rien ici.")
        # mur_cuisine
        entree_escaliers = Item("Entrée_menant_à_des_escaliers","entrée vers le sous-sol")
# Objets de chaque sous-pièce des escaliers_rdc
        # pas d'objets, juste l'endroit à fouiller escaliers_vers_cave
# Objets de chaque sous-pièce du salon
        # canape_salon
        # rien si on ne regarde pas le reflet
        telecommande_salon = Item("Télécommande","La télécommande contient une clé.")
        # tele_salon
        reflet_salon = Item("Reflet","Quelque chose dépasse des assises du canapé.")
        # table_salon
        note_salon = Item("Note_sur_papier","Recto : 'Où est la clé du sous-sol, Victor ? Verso : 'Lève-toi du canapé pour une fois !'")
# Objets de chaque sous-pièce des toilettes_rdc
        # miroir_toilettes_rdc
        tache_rouge = Item("Tâche_rouge","Des lignes de sang se forment sur le miroir, comme si elles provenaient de la cuvette des toilettes derrière Evelyn. Il n’y a pas de sang dans la réalité.")
        # cuvette_rdc
        # rien (déjà instancié) si pris avant le miroir ou si refus de prendre pendant le choix
        lampe_torche = Item("Lampe-torche","Il s'agit d'une lampe-torche ensanglantée.")
# Objets de chaque sous-pièce de la salle_manger
        # table_manger
        photo_manger = Item("Photo","Une photo d’une famille heureuse, en vêtements d’été, sur le port, accrochée au plat principal avec une puce")
        # chaise_manger
        radio_manger = Item("Radio","On entend une dispute enflammée entre un homme et une femme sur des questions financières ; les enfants pleurent à l'arrière.")
# Objets de chaque sous-pièce de la chambre_camille
        # pas d'objet ou d'endroits, juste description pièce
# Objets de chaque sous-pièce de la chambre_victor
        # pas d'objet ou d'endroits, juste description pièce


########## Ajout d'un objet d'une classe dans une autre (du plus haut vers le bas) ##########

        # Ajout des sous-salles dans la pièce centrale
        piece_centrale.ssrooms[table_nappee.name] = table_nappee
        piece_centrale.ssrooms[armoire_a_vaiselle.name] = table_nappee
        piece_centrale.ssrooms[radiateur.name] = radiateur
        # Ajout des sous-salles dans la salle avec porte ouvertes
        salle_monstres_rdc.ssrooms[armoire_sophie.name] = armoire_sophie
        salle_monstres_rdc.ssrooms[coin_sophie.name] = coin_sophie
        salle_monstres_rdc.ssrooms[trou_sophie.name] = trou_sophie
        # Ajout des sous-salles dans la cuisine
        cuisine.ssrooms[frigo_rdc.name] = frigo_rdc
        cuisine.ssrooms[four_rdc.name] = four_rdc
        cuisine.ssrooms[etagere_droite.name] = etagere_droite
        cuisine.ssrooms[etagere_gauche.name] = etagere_gauche
        cuisine.ssrooms[mur_cuisine.name] = mur_cuisine
        # Ajout des sous-salles dans les escaliers cachés
        escaliers_caches.ssrooms[escaliers_vers_cave.name] = escaliers_vers_cave 
        # Ajout des sous-salles dans le salon
        salon.ssrooms[canape_salon.name] = canape_salon 
        salon.ssrooms[tele_salon.name] = tele_salon
        salon.ssrooms[table_salon.name] = table_salon
        # Ajout des sous-salles dans les toilettes du rdc
        toilettes_rdc.ssrooms[miroir_toilettes_rdc.name] = miroir_toilettes_rdc 
        toilettes_rdc.ssrooms[cuvette_rdc.name] = cuvette_rdc
        # Ajout des sous-salles dans la salle à manger
        salle_a_manger.ssrooms[table_manger.name] = table_manger
        salle_a_manger.ssrooms[chaise_manger.name] = chaise_manger
        # Ajout des sous-salles dans la chambre de Camille
            # pas d'endroits/objets, seulement la description
        # Ajout des sous-salles dans la chambre de Victor
            # pas d'endroits/objets, seulement la description

        # Ajout des objets dans les sous-salles de la pièce centrale
            # Ajout des objets dans la table nappée
        table_nappee.objects[carte_rdc.name] = carte_rdc
            # Ajout des objets dans l'armoire
        armoire_a_vaiselle.objects[vitre_a_casser.name] = vitre_a_casser
        armoire_a_vaiselle.objects[trousse_soins.name] = trousse_soins 
            # Ajout des objets dans le radiateur
        radiateur.objects[se_chauffer.name] = se_chauffer
        # Ajout des objets dans la chambre ouverte
            # Ajout des objets dans l'armoire
        armoire_sophie.objects[rien_sophie.name] = rien_sophie
            # Ajout des objets dans le coin
        coin_sophie.objects[cafard.name] = cafard
            # Ajout des objets dans le trou
        trou_sophie.objects[grillage.name] = grillage
        # Ajout des objets dans la cuisine
            # Ajout des objets dans le frigo
        frigo_rdc.objects[photo_cuisine.name] = photo_cuisine
        frigo_rdc.objects[pommes_cuisine.name] = pommes_cuisine
        frigo_rdc.objects[revolver_cuisine.name] = revolver_cuisine 
            # Ajout des objets dans le four
        four_rdc.objects[rien_cuisine.name] = rien_cuisine
            # Ajout des objets dans les étagères droit
        etagere_droite.objects[piege_souris.name] = piege_souris
            # Ajout des objets dans les étagères gauche
        etagere_gauche.objects[rien.name] = rien
            # Ajout des objets dans le mur fissuré 
        mur_cuisine.objects[escaliers_caches.name] = escaliers_caches
                # accessible seulement si clé trouvée dans salon
        # Ajout des objets dans le salon
            # Ajout des objets dans le canapé
        canape_salon.objects[telecommande_salon.name] = telecommande_salon
                # apparait si on a vu le reflet
            # Ajout des objets dans la télé
        tele_salon.objects[reflet_salon.name] = reflet_salon
            # Ajout des objets dans les étagères droit
        table_salon.objects[note_salon.name] = note_salon
        # Ajout des objets dans les toilettes
            # Ajout des objets dans le miroir
        miroir_toilettes_rdc.objects[tache_rouge.name] = tache_rouge 
            # Ajout des objets dans la cuvette
        cuvette_rdc.objects[lampe_torche.name] = lampe_torche
        # Ajout des objets dans la salle à manger
            # Ajout des objets dans la table
        table_manger.objects[photo_manger.name] = photo_manger 
            # Ajout des objets dans la chaise
        chaise_manger.objects[radio_manger.name] = radio_manger
        # Pas d'objets dans les chambres de Camille et Victor
####################### Setup des rooms, ssrooms et items #######################

    # Setup exits couloir -> toutes les pièces du 1er étage
        couloir_rdc.exits_room = {"Pièce_centrale" : piece_centrale, 
                            "Pièce_dont_la_porte_est_légèrement_entre-ouverte" : salle_monstres_rdc, 
                            "Cuisine" : cuisine, 
                            "Escaliers_derrière_la_cuisine" : escaliers_caches,
                            "Salon" : salon,
                            "Toilettes" : toilettes_rdc,
                            "Salle_à_manger" : salle_a_manger,
                            "Chambre_de_Camille" : chambre_camille,
                            "Chambre_de_Victor" : chambre_victor}
        piece_centrale.exits_room = {"Couloir": couloir_rdc}
        salle_monstres_rdc.exits_room = {"Couloir": couloir_rdc}
        cuisine.exits_room = {"Couloir": couloir_rdc, "Escaliers_derrière_la_cuisine" : escaliers_caches}
        escaliers_caches.exits_room = {"Couloir": couloir_rdc}
        salon.exits_room = {"Couloir": couloir_rdc}
        toilettes_rdc.exits_room = {"Couloir": couloir_rdc}
        salle_a_manger.exits_room = {"Couloir": couloir_rdc}
        chambre_camille.exits_room = {"Couloir": couloir_rdc}
        chambre_victor.exits_room = {"Couloir": couloir_rdc}

    # Setup exits de chaque room -> ssroom dans chaque room
        piece_centrale.exits_ssroom = {"Table_nappée" : table_nappee,
                                    "Armoire_à_vaisselle" : armoire_a_vaiselle,
                                    "Radiateur" : radiateur,}
        salle_monstres_rdc.exits_ssroom = {"Armoire" : armoire_sophie,
                                    "Coin_de_la_chambre" : coin_sophie,
                                    "Trou_dans_le_lit" : trou_sophie,}
        cuisine.exits_ssroom = {"Réfrigérateur" : frigo_rdc,
                                "Four" : four_rdc,
                                "Etagères_côté_droit" : etagere_droite,
                                "Etagères_côté_gauche" : etagere_gauche,
                                "Fissures_dans_le_mur" : mur_cuisine}
        escaliers_caches.exits_ssroom = {"Escaliers_cachés_derrière_la_cuisine" : escaliers_vers_cave}
        salon.exits_ssroom = {"Canapé" : canape_salon,
                            "Télévision" : tele_salon,
                            "Table_basse" : table_salon}
        toilettes_rdc.exits_ssroom = {"Miroir" : miroir_toilettes_rdc,
                                    "Cuvette_des_toilettes" : cuvette_rdc}
        salle_a_manger.exits_ssroom = {"Table_garnie_de_mets_pourris" : table_manger,
                                    "Chaise_avec_une_radio_posée_dessus" : chaise_manger}
        chambre_camille.exits_ssroom = {}
        chambre_victor.exits_ssroom = {}

    # Setup ssrooms objects 

        # Pièce centrale
        table_nappee.objects = {"Carte_du_rez-de-chaussée" : carte_rdc}
        armoire_a_vaiselle.objects = {"Vitre_cassable" : vitre_a_casser, "Trousse de soins" : trousse_soins}
        radiateur.objects = {"Se_chauffer" : se_chauffer}
        # Salle de monstres
        armoire_sophie.objects = {"Rien" : rien_sophie}
        coin_sophie.objects = {"Trou_dans_le_coin" : cafard}
        trou_sophie.objects = {"Grillage" : grillage }
        # Cuisine
        frigo_rdc.objects = {"Photo" : photo_cuisine , "Pommes" : pommes_cuisine,"Revolver" : revolver_cuisine}  
        four_rdc.objects = {"Rien" : rien_cuisine}
        etagere_droite.objects = {"Piège_à_souris" : piege_souris}
        etagere_gauche.objects = {"Rien" : rien}
        mur_cuisine.objects = {"Entrée_menant_à_des_escaliers" : entree_escaliers}
        # Escaliers
        escaliers_vers_cave.objects = {"Entrée_menant_à_des_escaliers" : entree_escaliers}
        # Salon 
        canape_salon.objects = {"Télécommande" : telecommande_salon}
        tele_salon.objects = {"Reflet" : reflet_salon}
        table_salon.objects = {"Note_sur_papier" : note_salon}
        # Toilettes
        miroir_toilettes_rdc.objects = {"Tâche_rouge" : tache_rouge}
        cuvette_rdc.objects = {"Lampe-torche" : lampe_torche}
        # Salle à manger
        table_manger.objects = {"Photo" : photo_manger}
        chaise_manger.objects = {"Radio" : radio_manger}
        # Chambre de Camille

        # Chambre de Victor

    

    # Setup player
        self.player = Player("Evelyn Westwood") # nom du personnage principal fixe
        self.player.current_room = couloir_rdc
        self.player.current_ssroom = None

    # Setup commands (code de M. Courivaud)

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <pièce> : entrer dans cette pièce )", Actions.go, 1)
        self.commands["go"] = go
        start = Command("start"," : démarrer le jeu",Actions.start,0)
        self.commands["start"] = start
        look = Command("look"," : fouiller un endroit de la pièce",Actions.look,1)
        self.commands["look"] = look
        take = Command("take"," : récupérer un objet",Actions.take,1)
        self.commands["take"] = take

# Play the game (Code de M. Courivaud)
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.isdead:
            if self.player.state >=2:
                print("Les hallucinations sont trop importantes. Evelyn fait une crise cardiaque...")
                quit()
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ") # split(" ") crée une liste en séparant la string à chq espace

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nVous incarnez Evelyn Westwood, une femme d’une trentaine d’années, présentatrice télé à la carrière ruinée par une dernière émission ratée le jour de Noël. Ce soir, après avoir bu plus que de raison, seule dans un bar, vous prenez la voiture pour rentrer chez vous.")
        print(f"\nEnter start to begin.")
        print("\nEntrez 'help' si vous avez besoin d'aide.")

def main():
# Create a game object and play the game
    Game().play()

#Appel protégé de la fonction main (obligatoire dans chaque programme) (permet aussi de lancer le programme)
########## Déplacements du joueur (étage à objets, dans un sans et l'autre) ##########

if __name__=="__main__":
    main()
