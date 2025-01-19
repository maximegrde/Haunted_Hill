# Description : Classe Jeu

# Importer les modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item

class Jeu:
    """
    Cette classe représente le jeu d'aventure.

    Attributs :
        finished (bool) : Indique si le jeu est terminé.
        rooms (list) : Liste des pièces du jeu.
        commands (dict) : Dictionnaire des commandes disponibles.
        player (Player) : L'objet représentant le joueur.

    Méthodes :
        setup(self) : Configure le jeu, les commandes et les pièces.
        play(self) : Lance et gère le jeu.
        process_command(self, command_string) : Traite la commande entrée par le joueur.
        print_welcome(self) : Affiche le message de bienvenue.
    """

    def __init__(self):
        """
        Constructeur de la classe Jeu.

        Initialise les attributs du jeu.
        """
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None

    def setup(self):
        """
        Configure le jeu, les commandes et les pièces.
        """
        # Configurer les commandes
        aide = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = aide
        quitter = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quitter
        aller = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, ouest, OUEST, Ouest)", Actions.go, 1)
        self.commands["go"] = aller
        historique = Command("history", " : consulter l'historique des pièces visitées", Actions.history, 0)
        self.commands["history"] = historique
        inventaire = Command("inventory", " : consulter l'inventaire du joueur", Actions.inventory, 0)
        self.commands["inventory"] = inventaire
        regarder = Command("inventory_room", " : consulter l'inventaire de la pièce visitée", Actions.look, 0)
        self.commands["inventory_room"] = regarder

        # Configurer les pièces
        foret = Room("Forêt", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(foret)
        epee = Item("Epée", "Une épée banale", 50)
        bouclier = Item("Bouclier", "Une bouclière de fer", 90)
        foret.room_inventory.add(epee)  # ajout d'un objet dans l'inventaire de la forêt
        foret.room_inventory.add(bouclier)  # ajout d'un objet dans l'inventaire de la forêt
        tour = Room("Tour", "dans une immense tour en pierre qui s'élève au-dessus des nuages.")
        self.rooms.append(tour)
        grotte = Room("Grotte", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        self.rooms.append(grotte)
        chalet = 
