class SSRoom:
    def __init__(self, name, description=''):
        self.name = name
        self.description = description
        self.objects = {} # ou set() = inventaire du lieu

    def get_long_description_ssroom(self):
        return f"\n{self.description}\n"
