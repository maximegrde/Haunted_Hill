from floor import Floor
from room import Room
from player import Player
from command import Command
from actions import Actions


class Game:
    """Classe principale du jeu qui gère l'initialisation et le déroulement."""

    def __init__(self):
        """Constructeur de la classe Game."""
        self.finished = False
        self.floors = {}
        self.commands = {}
        self.player = None

    def setup(self):
        """Initialise les éléments du jeu."""

        # Initialisation des commandes
        self.commands = {
            "help": Command("help", " : afficher cette aide", Actions.help, 0),
            "quit": Command("quit", " : quitter le jeu", Actions.quit, 0),
            "go": Command("go", " <direction> : se déplacer dans une direction", Actions.go, 1),
        }

        # Création des étages
        sous_sol = Floor("Sous-sol", "Vous arrivez dans le sous-sol du manoir.")
        rez_de_chaussee = Floor("Rez-de-chaussée", "Vous arrivez au rez-de-chaussée.")
        premier_etage = Floor("Premier étage", "Vous arrivez au premier étage.")
        toit = Floor("Toit", "Vous arrivez sur le toit.")

        self.floors = {
            "sous_sol": sous_sol,
            "rez_de_chaussee": rez_de_chaussee,
            "premier_etage": premier_etage,
            "toit": toit,
        }

        # Exemple de création de salles et configuration des sorties
        forest = Room("Forêt", "Une forêt enchantée avec une brise légère.")
        tower = Room("Tour", "Une tour immense qui s'élève au-dessus des nuages.")

        forest.exits = {"N": tower, "E": None, "S": None, "O": None}
        tower.exits = {"N": None, "E": None, "S": forest, "O": None}

        sous_sol.rooms = {
            "forest": forest,
            "tower": tower,
        }

        # Initialisation du joueur
        self.player = Player(input("\nEntrez votre nom : "))
        self.player.current_room = forest

    def play(self):
        """Lance le jeu."""
        self.setup()
        self.print_welcome()
        while not self.finished:
            self.process_command(input("> "))

    def process_command(self, command_string):
        """Traite la commande saisie par le joueur."""
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]

        if command_word not in self.commands:
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir les commandes disponibles.\n")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    def print_welcome(self):
        """Affiche le message de bienvenue."""
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())


def main():
    """Point d'entrée principal du jeu."""
    Game().play()


if __name__ == "__main__":
    main()
