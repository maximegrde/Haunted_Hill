########## Création des commandes utilisant les fonctions dans la classe Actions ##########

class Command: # Code de M.Courivaud

    # The constructor.
    def __init__(self, command_word, help_string, action, number_of_parameters):
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters
    
    # The string representation of the command.
    def __str__(self):
        return  self.command_word + self.help_string
