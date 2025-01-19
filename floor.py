# Définir la classe Étage

class Floor:
    """
    Cette classe représente un étage d'un bâtiment avec des informations sur
    son nom, sa description et les sorties disponibles.

    Attributs :
        name (str) : Le nom de l'étage.
        description (str) : La description de l'étage.
        exits (dict) : Un dictionnaire des sorties, où chaque clé est une direction et la valeur est l'étage suivant.

    Méthodes :
        __init__(self, name, description) : Le constructeur de l'étage.
        get_exit(self, direction) : Renvoie l'étage dans la direction donnée si elle existe.
        get_exit_string(self) : Renvoie une chaîne décrivant les sorties de l'étage.
        get_long_description(self) : Renvoie une description complète de l'étage incluant les sorties.
    """

    def __init__(self, name, description):
        """
        Le constructeur de la classe Étage.

        Args:
            name (str) : Le nom de l'étage.
            description (str) : La description de l'étage.
        """
        self.name = name
        self.description = description
        self.exits = {}

    def get_exit(self, direction):
        """
        Renvoie l'étage dans la direction donnée si elle existe.

        Args:
            direction (str) : La direction dans laquelle chercher une sortie.

        Retourne :
            Étage ou None : L'étage suivant dans la direction donnée ou None si la direction n'existe pas.
        """
        if direction in self.exits:
            return self.exits[direction]
        return None

    def get_exit_string(self):
        """
        Renvoie une chaîne décrivant les sorties disponibles.

        Retourne :
            str : Une chaîne décrivant les sorties de l'étage.
        """
        exit_string = "Sorties : "
        for exit in self.exits:
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    def get_long_description(self):
        """
        Renvoie une description longue de l'étage incluant les sorties.

        Retourne :
            str : Une chaîne décrivant l'étage avec sa description et les sorties.
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
