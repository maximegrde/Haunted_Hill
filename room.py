# Définir la classe Pièce

class Piece:
    """
    Cette classe représente une pièce dans le jeu.

    Attributs :
        name (str) : Le nom de la pièce.
        description (str) : La description de la pièce.
        exits (dict) : Le dictionnaire des sorties de la pièce, où chaque direction (clé) mène à une autre pièce.
        room_inventory (set) : L'inventaire de la pièce, qui contient des objets.

    Méthodes :
        __init__(self, name, description, room_inventory=set()) : Constructeur de la classe.
        get_exit(self, direction) : Permet d'obtenir la pièce située dans une direction donnée.
        get_exit_string(self) : Retourne une chaîne décrivant les sorties de la pièce.
        get_long_description(self) : Retourne une description détaillée de la pièce, y compris les sorties.
    """

    def __init__(self, name, description, room_inventory=None):
        """
        Constructeur de la classe Pièce.

        Args :
            name (str) : Le nom de la pièce.
            description (str) : La description de la pièce.
            room_inventory (set, optionnel) : L'inventaire de la pièce. Par défaut un ensemble vide.
        """
        if room_inventory is None:
            room_inventory = set()

        self.name = name
        self.description = description
        self.exits = {}
        self.room_inventory = room_inventory

    def get_exit(self, direction):
        """
        Permet d'obtenir la pièce située dans une direction donnée.

        Args :
            direction (str) : La direction dans laquelle vérifier la sortie (par exemple "N", "E", etc.).

        Retourne :
            Piece ou None : La pièce correspondante à la direction, ou None si la sortie n'existe pas.
        """
        # Retourne la pièce dans la direction donnée si elle existe.
        return self.exits.get(direction, None)
    
    def get_exit_string(self):
        """
        Retourne une chaîne décrivant les sorties de la pièce.

        Retourne :
            str : Une chaîne décrivant les sorties disponibles.
        """
        exit_string = "Sorties : " 
        for exit_direction in self.exits.keys():
            if self.exits.get(exit_direction) is not None:
                exit_string += exit_direction + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    def get_long_description(self):
        """
        Retourne une description longue de cette pièce, y compris les sorties.

        Retourne :
            str : Une description complète de la pièce.
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
