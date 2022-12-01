class Cat:
    def __init__(self,name, color, age ):
       self.name = name
       self.color = color
       self.age = age
    def meow(self):
        print(self.name + ": meow!")
    def mrr(self):
        print(f"{self.name}: mrr!")
    def ship(self):
        print(f"{self.name}: shhh!")
kit = Cat("kitik", "grey", "5" )
print(kit.name)
print(kit.color)
print(kit.age, " years")
kit.meow()
kit.mrr()
kit.ship()