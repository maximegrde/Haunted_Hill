# Description: Game class

# Import modules

from floor import Floor
from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.floors = {}
        self.rooms = {}
        self.srooms = {}
        # self.floors = {"Sous-sol":{"Pièce 1":{"générateur":{câble, bouton de démarrage}}}, "étage 1" : {"Pièce 1":{"générateur":{câble, bouton de démarrage}}}, etc }
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        """ 
        Les setups floors/rooms/ss-rooms décrivent les ambiances !
        """
        # Setup floors

        sous_sol = Floor("Sous-sol", "Vous arrivez dans le sous-sol du manoir.")
        salle_cachee = Room("Salle cachée", "Vous traversez le mur que vous venez de détruire et vous arrivez dans une pièce sombre.")
        tiroir = SRoom("Tiroir","Il s'agit d'un tiroir que vous pouvez ouvrir.")
        floors[self.floors(sous_sol)]=self.rooms #ajout du sous-sol dans le dict floors 
        floors[0][0]=self.salle_cachee #ajout de la salle cachée au sous-sol
        floors[0][0][0]=self.tiroir #ajout du tiroir dans la salle cachée

        floors[0][1]=self.cachee
        floors[0][2]=self.monstres
        floors[0][3]=self.generateur
        floors[0][4]=self.fissures
        floors[0][5]=self.cle
        floors[0][6]=self.souvenir
        floors[0][7]=self.essence

        rez_de_chaussee = Floor("Rez-de-chaussée", "Vous arrivez dans le rez-de-chaussée.")
        floors+=self.floors(rez_de_chaussée)
        premier_etage = Floor("Premier étage", "Vous arrivez au premier étage.")
        floors+=self.floors(premier_etage)
        deuxieme_etage = Floor("Deuxième étage", "Vous arrivez au deuxième étage.")
        floors+=self.floors(deuxieme_etage)
        toit = Floor("Toit", "Vous arrivez sur le toit.")
        floors+=self.floors(toit)
        
        # Setup rooms

        # Couloirs pour chaque étage (créer un fichier contenant les couloirs de chaque étage)
        couloirsol = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        couloirrdc = Room("Tower", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
        self.rooms.append(tower)
        couloirpremier = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        self.rooms.append(cave)
        couloirdeuxieme = Room("Cottage", "dans un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        self.rooms.append(cottage)
        couloirtoit = Room("Swamp", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        self.rooms.append(swamp)

        couloirsol.exits = {"N" : cave, "E" : tower, "S" : castle, "O" : None}
        couloirrdc.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave}
        couloirpremier.exits = {"N" : cottage, "E" : None, "S" : swamp, "O" : forest}
        couloirdeuxieme.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None}
        couloirtoit.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle}

        # Rooms du floor 0
        # Rooms du floor 1
        # Rooms du floor 2
        # Rooms du floor toit


        # Setup sous-rooms (endroits à fouiller dans chaque pièce)
        







        # Create exits for floors, rooms, srooms

        # Exits for floors

        sous_sol.exits = {"N" : cave, "E" : tower, "S" : castle, "O" : None}
        rez_de_chaussee.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave}
        premier_etage.exits = {"N" : cottage, "E" : None, "S" : swamp, "O" : forest}
        deuxieme_etage.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None}
        toit.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle}

        # Exits for rooms

        forest.exits = {"N" : cave, "E" : tower, "S" : castle, "O" : None}
        tower.exits = {"N" : cottage, "E" : None, "S" : swamp, "O" : forest}
        cave.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None}
        cottage.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave}
        swamp.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle}
        castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None}

        # Exits for srooms

        forest.exits = {"N" : cave, "E" : tower, "S" : castle, "O" : None}
        tower.exits = {"N" : cottage, "E" : None, "S" : swamp, "O" : forest}
        cave.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None}
        cottage.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave}
        swamp.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle}
        castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = swamp

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

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
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
