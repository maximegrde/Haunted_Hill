########## Création des actions possibles pour le joueur ##########
# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

from player import Player

class Actions:

    # historique actif
    # def inventory(game, list_of_words,number_of_parameters):
    #     print("Votre inventaire contient : \n")
    #     for item_inventory in game.Evelyn_Westwood.inventory: # inventaire dans la classe game
    #         print("- "+str(item_inventory.name)+"\n")

    # Code de M. Courivaud
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]
        # Move the player in the direction specified by the parameter.
        player.move(direction)
        return True

    def start(game, list_of_words, number_of_parameters):
        """
        Start the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> start(game, ["Start"], 0)
        True
        >>> quit(game, ["Start", "N"], 0)
        False
        >>> quit(game, ["Start", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        start_room = game.player.current_room
        print(f"\n{start_room.get_long_description_room()}\n")
        for salle in game.floors[0]: 
            print(f"- {salle.name}")
        # msg = f"\n{start_room.description}"
        # print(msg)
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci d'avoir joué. Au revoir.\n"
        print(msg)
        game.isdead = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    # check the objects in the ssroom 
    def look(game, list_of_words,number_of_parameters):
        player = game.player
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        # print the objects in the ssroom
        print("\n Vous fouillez l'endroit et remarquez les objets suivants : \n")
        direction = list_of_words[1]
        player.move(direction)
        return True
        
    # take objects in the ssroom
    def take(game, list_of_words,number_of_parameters):
        
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # retire l'objet d'un lieu pour le mettre dans l'inventaire
        item_pris = game.player.current_ssroom.objects[list_of_words[1]]
        if item_pris.name == "Entrée_menant_à_des_escaliers":
            print("Vous descendez les escaliers menant au sous-sol...\n")
            print("Merci d'avoir joué à la version d'essai ! Rendez-vous sur notre boutique pour acheter le jeu complet.")
            quit()
        if item_pris in game.player.current_ssroom.objects.values():
            if item_pris.name == "Trou_dans_le_coin" or item_pris.name == "Grillage" or item_pris.name == "Tâche_rouge" or item_pris.name == "Lampe-torche":
                game.player.state+= 1
            else:
                print("Vous avez récupéré : \n")
                print("- " + str(item_pris.name) + ": " + str(item_pris.description))
                game.player.inventory.add(item_pris) # ajout à l'inventaire du joueur
                del game.player.current_ssroom.objects[list_of_words[1]] # suppression du dictionnaire des objets de la ss-pièce
        else:
            print("Il n'y a pas cet objet ici.\n")

