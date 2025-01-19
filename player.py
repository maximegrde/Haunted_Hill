from item import Item

# Définir la classe Joueur
class Joueur:
    """
    Cette classe représente un joueur dans le jeu.

    Attributs :
        name (str) : Le nom du joueur.
        current_room (Room) : La pièce dans laquelle se trouve le joueur.
        history (list) : L'historique des pièces visitées par le joueur.
        player_inventory (dict) : L'inventaire du joueur (objet, quantité).

    Méthodes :
        __init__(self, name, history=[], player_inventory={}) : Constructeur de la classe.
        move(self, direction) : Permet au joueur de se déplacer dans une direction donnée.
        get_history(self, game, list_of_words, number_of_parameters) : Affiche l'historique des pièces visitées par le joueur.
    """

    def __init__(self, name, history=None, player_inventory=None):
        """
        Constructeur de la classe Joueur.

        Args :
            name (str) : Le nom du joueur.
            history (list, optionnel) : L'historique des pièces visitées par le joueur. Par défaut une liste vide.
            player_inventory (dict, optionnel) : L'inventaire du joueur. Par défaut un dictionnaire vide.
        """
        if history is None:
            history = []
        if player_inventory is None:
            player_inventory = {}

        self.name = name
        self.current_room = None
        self.history = history
        self.player_inventory = player_inventory

    def move(self, direction):
        """
        Permet au joueur de se déplacer dans une direction donnée.

        Args :
            direction (str) : La direction dans laquelle le joueur souhaite se déplacer.

        Retourne :
            bool : Retourne True si le mouvement a réussi, sinon False.
        """
        # Obtenir la prochaine pièce à partir du dictionnaire des sorties de la pièce actuelle.
        next_room = self.current_room.exits.get(direction)

        # Si la prochaine pièce est None, afficher un message d'erreur et retourner False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Définir la pièce actuelle sur la prochaine pièce et ajouter la pièce initiale à l'historique
        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        
        # Historique des pièces découvertes
        if self.current_room not in self.history:
            self.history.append(self.current_room)
            print("\nVous avez déjà visité les pièces suivantes :\n")
        for elt in self.history:
            print("- " + str(elt.name) + "\n")
        return True

    def get_history(self, game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des pièces visitées par le joueur.

        Args :
            game (Jeu) : L'objet représentant le jeu.
            list_of_words (list) : La liste des mots de la commande.
            number_of_parameters (int) : Le nombre de paramètres attendus pour la commande.
        
        Retourne :
            bool : Toujours True.
        """
        if game.player.current_room not in self.history:
            game.player.history.append(game.player.current_room)
        
        print("\nVous avez déjà visité les pièces suivantes :\n")
        for elt in game.player.history:
            print("- " + str(elt.name) + "\n")
        return True
