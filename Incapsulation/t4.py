from t3 import *


class Truck:
    def __init__(self, mark, transmission, capacity):
        self.mark = mark
        self.transmission = transmission 
        self.capacity = capacity
    def __add__(self, box):
        self.capacity.append(box)
    def __sub__(self, other):
        self.capacity.pop()
    def __str__(self):
        return f'грузовик: {self.mark}, коробка передач: {self.transmission} \nсодержимое: {self.capacity}'

truck = Truck('volvo', 'automatic', [str(box1), str(box2)])
truck - box1        # он почему-то игнорирует минус и просто добавляет в список, при этом не включает в него box2
truck + box3
print(str(truck))   # вывод: ['посылка hikaru едет с Москва в Казань postcode: 539088', посылка stershine едет с Челябинск в Набережные Челны postcode: 985736]