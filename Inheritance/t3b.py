from abc import ABC, abstractclassmethod
class Stationery:
    def __init__(self, title):
        self.title = title
    def set_color(self):
        self.color = "yellow"
        return self.color
    @abstractclassmethod
    def draw():
        print("запуск отрисовки")
    
class Pen(Stationery):
    def draw(self):
     print(f"{self.title} не пишет")
    
class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} рисует")
    
class Handle(Stationery):
    def draw(self):
        print(f"{self.title} высох..")
        
pen = Pen("ручка")
pencil = Pencil("карандаш")
handle = Handle("маркер")


print(pen.title, pen.set_color())
print(pencil.title, pencil.set_color())
print(handle.title, handle.set_color())

# наблюдаем, что все желтое