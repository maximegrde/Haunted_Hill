########## Création du personnage joueur ##########

class Player:
    def __init__(self, name, history=[]):
        self.history = [] # historique des pièces visitées
        self.name = name
        self.inventory = set() # ou dict()
        self.current_room = None
        self.current_ssroom = None
        self.isdead = False
        self.state = 0 # état d'Evelyn (3 possibilités selon le palier qu'atteint le compteur state)

    # Define the move_room method (moving from a room to another).
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        if direction == "Couloir": # Cas où on veut revenir dans le couloir principal
            next_room = self.current_room.exits_room[direction]
            self.current_room = next_room
            print("\nVous êtes revenue dans le couloir principal.\n")
            for ssroom in self.current_room.exits_room.keys():
                print("\n- " + str(ssroom))
        else:
        # Set the current ssroom to the next ssroom 
            if direction in self.current_room.exits_ssroom.keys(): # Cas où on va dans une sous-pièce 
                next_ssroom = self.current_room.exits_ssroom[direction]
                self.current_ssroom = next_ssroom
                print(self.current_ssroom.get_long_description_ssroom()+"\n")
                for item in self.current_ssroom.objects.keys():
                    print("- " + str(item) + "\n")

        # Set the current room to the next room and add initial room to history
            else: # Cas où on va dans une pièce 
                next_room = self.current_room.exits_room[direction]
                self.history.append(self.current_room)
                self.current_room = next_room
                print(self.current_room.get_long_description_room()+"\n")
                for ssroom in self.current_room.exits_ssroom.keys():
                    print("- " + str(ssroom) + "\n")
        return True
    
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits_room.keys():
            return self.exits_room[direction]
        if direction in self.exits_ssroom.keys():
            return self.exits_room[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string
