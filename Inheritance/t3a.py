from abc import ABC, abstractclassmethod
class Stationery:
    def __init__(self, title):
        self.title = title
    @abstractclassmethod
    def draw():
        print("запуск отрисовки")
class Pen(Stationery):
    def __init__(self, color):
        super().__init__("ручка")
        self. color = color
    def draw(self):
     print(f"{self.title} не пишет")
    
class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} рисует")
    
class Handle(Stationery):
    def draw(self):
        print(f"{self.title} высох..")
        
pen = Pen("синяя")
pencil = Pencil("карандаш")
handle = Handle("маркер")

print(pen.color, end = " ")
pen.draw()
pencil.draw()
handle.draw()
