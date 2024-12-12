# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name, history=[]):
        self.name = name
        self.current_room = None
        self.history = history

    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room and add initial room to history
        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        # history of rooms discovered
        if self.current_room not in self.history:
            self.history.append(self.current_room) 
            print("\nVous avez déjà visité les pièces suivantes :\n")
        for elt in self.history:
            print("- "+str(elt.name)+"\n")
        return True

    def get_history(self,game, list_of_words,number_of_parameters):
        if game.player.current_room not in self.history:
            game.player.history.append(game.player.current_room) #Player().current_room <=> player_history.current_room 
        print("\nVous avez déjà visité les pièces suivantes :\n")
        for elt in game.player.history:
            print("- "+str(elt.name)+"\n")
        return True



    