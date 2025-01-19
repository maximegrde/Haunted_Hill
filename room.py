"""institue les rooms"""

class Room: #création des objets/classes pièce, ss-pièce et objet
    def __init__(self, name, description=''):
        self.name = name
        self.description = description
        self.exits_room = {} # pour les pièces dans le couloir
        self.exits_ssroom = {} # pour les sous-pièces dans les autres pièces
        self.ssrooms = {}

    def get_long_description_room(self):
        return f"\n{self.description}\n"
    
