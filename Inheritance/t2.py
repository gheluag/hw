class Father:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Child(Father):
    def __init__(self, patronim):
        super().__init__("Luffy", "Monkey D." )
        self.patronim = patronim
chil = Child("Luffy son")
print(chil.surname, chil.name, chil.patronim)