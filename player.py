# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = [] #ajout de l'historique des pièces visitées

    # def get_history(self): # fonction qui regarde si tous les endroits d'une pièce ont été fouillés
    #     for eltf in self.floors:
    #         for eltr in self.rooms:
    #             for i in range len(self.srooms):
    #                 if self.rooms[i]=='':
    #                     print "Vous avez déjà exploré : " + str(eltr)

    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    