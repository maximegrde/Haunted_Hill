# Description : Le module des actions.

# Le module des actions contient les fonctions qui sont appelées lorsqu'une commande est exécutée.
# Chaque fonction prend 3 paramètres :
# - game : l'objet du jeu
# - list_of_words : la liste des mots dans la commande
# - number_of_parameters : le nombre de paramètres attendus pour la commande
# Les fonctions renvoient True si la commande a été exécutée avec succès, False sinon.
# Elles affichent un message d'erreur si le nombre de paramètres est incorrect.
# Le message d'erreur est différent selon le nombre de paramètres attendus par la commande.

# Le message d'erreur est stocké dans les variables MSG0 et MSG1, formatées avec le nom de la commande.
# MSG0 est utilisé lorsque la commande ne prend pas de paramètre.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# MSG1 est utilisé lorsque la commande prend 1 seul paramètre.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

from player import Player
from room import Room
from item import Item


class Actions:
    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Déplacer le joueur dans la direction spécifiée par le paramètre.
        Le paramètre doit être une direction cardinale (N, E, S, O).

        Args:
            game (Game) : L'objet du jeu.
            list_of_words (list) : La liste des mots dans la commande.
            number_of_parameters (int) : Le nombre de paramètres attendus par la commande.

        Returns:
            bool : True si la commande a été exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            print(MSG1.format(command_word=list_of_words[0]))
            return False

        direction = list_of_words[1]
        player = game.player
        player.move(direction)
        return True

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quitter le jeu.

        Args:
            game (Game) : L'objet du jeu.
            list_of_words (list) : La liste des mots dans la commande.
            number_of_parameters (int) : Le nombre de paramètres attendus par la commande.

        Returns:
            bool : True si la commande a été exécutée avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False

        player = game.player
        print(f"\nMerci {player.name} d'avoir joué. Au revoir.\n")
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Afficher la liste des commandes disponibles.

        Args:
            game (Game) : L'objet du jeu.
            list_of_words (list) : La liste des mots dans la commande.
            number_of_parameters (int) : Le nombre de paramètres attendus par la commande.

        Returns:
            bool : True si la commande a été exécutée avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False

        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        """
        Afficher l'historique des pièces visitées par le joueur.

        Args:
            game (Game) : L'objet du jeu.
            list_of_words (list) : La liste des mots dans la commande.
            number_of_parameters (int) : Le nombre de paramètres attendus par la commande.

        Returns:
            bool : True si la commande a été exécutée avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False

        print("\nVous avez déjà visité les pièces suivantes :\n")
        for room in game.player.history:
            print("- " + room.name)
        return True

    @staticmethod
    def inventory(game, list_of_words, number_of_parameters):
        """
        Afficher l'inventaire du joueur.

        Args:
            game (Game) : L'objet du jeu.
            list_of_words (list) : La liste des mots dans la commande.
            number_of_parameters (int) : Le nombre de paramètres attendus par la commande.

        Returns:
            bool : True si la commande a été exécutée avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False

        print("\nVotre inventaire contient :\n")
        for item in game.player.inventory:
            print(f"- {item.name} : {item.description}, {item.weight} kg")
        return True

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """
        Regarder autour de soi pour voir les objets présents dans la salle actuelle.

        Args:
            game (Game) : L'objet du jeu.
            list_of_words (list) : La liste des mots dans la commande.
            number_of_parameters (int) : Le nombre de paramètres attendus par la commande.

        Returns:
            bool : True si la commande a été exécutée avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG0.format(command_word=list_of_words[0]))
            return False

        room = game.player.current_room
        if not room.room_inventory:
            print("\nCette pièce est vide...\n")
        else:
            print("\nCette pièce contient :\n")
            for item in room.room_inventory:
                print(f"- {item.name} : {item.description}, {item.weight} kg")
        return True

    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """
        Prendre un objet dans la pièce actuelle et l'ajouter à l'inventaire du joueur.

        Args:
            game (Game) : L'objet du jeu.
            list_of_words (list) : La liste des mots dans la commande.
            number_of_parameters (int) : Le nombre de paramètres attendus par la commande.

        Returns:
            bool : True si la commande a été exécutée avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            print(MSG1.format(command_word=list_of_words[0]))
            return False

        item_name = list_of_words[1]
        room = game.player.current_room

        item = next((item for item in room.room_inventory if item.name == item_name), None)
        if item:
            game.player.inventory.append(item)
            room.room_inventory.remove(item)
            print(f"\nVous avez pris {item_name}.")
            return True
        else:
            print("\nCet objet n'est pas dans la pièce.")
            return False
