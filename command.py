# Ce fichier contient la classe Commande.

class Command:
    """
    Cette classe représente une commande. Une commande est composée d'un mot de commande, d'une chaîne d'aide, d'une action et d'un nombre de paramètres.

    Attributs :
        command_word (str) : Le mot de commande.
        help_string (str) : La chaîne d'aide.
        action (function) : L'action à exécuter lorsque la commande est appelée.
        number_of_parameters (int) : Le nombre de paramètres attendus pour la commande.

    Méthodes :
        __init__(self, command_word, help_string, action, number_of_parameters) : Le constructeur.
        __str__(self) : La représentation sous forme de chaîne de la commande.

    Exemples :

    >>> from actions import go
    >>> command = Command("go", "Permet de se déplacer dans une direction.", go, 1)
    >>> command.command_word
    'go'
    >>> command.help_string
    'Permet de se déplacer dans une direction.'
    >>> type(command.action)
    <class 'function'>
    >>> command.number_of_parameters
    1

    """

    def __init__(self, command_word, help_string, action, number_of_parameters):
        """
        Le constructeur de la classe Command.

        Args:
            command_word (str) : Le mot de commande.
            help_string (str) : La chaîne d'aide.
            action (function) : L'action à exécuter lorsque la commande est appelée.
            number_of_parameters (int) : Le nombre de paramètres attendus pour la commande.
        """
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters

    def __str__(self):
        """
        La représentation sous forme de chaîne de la commande.

        Retourne :
            str : Une chaîne combinant le mot de commande et la chaîne d'aide.
        """
        return f"{self.command_word} {self.help_string}"
