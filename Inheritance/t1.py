from abc import ABC, abstractclassmethod
class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    @abstractclassmethod
    def say(self):
        pass
class Cat(Animal):
    def meow(say):
        print(f"cat says: meow!")
class Dog(Animal):
    def woof(say):
        print(f"dog says: woof!")

cat = Cat("neko", "tricolor", "4")
dog = Dog("inu", "ginger", "5")

print(f"{cat.name}, {cat.color}, {cat.age} года")
cat.meow()
print(f"{dog.name}, {dog.color}, {dog.age} лет")
dog.woof()   