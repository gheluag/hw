from time import sleep
class Car:
    def __init__(self, color, mark, kuzov, transmission, speed = 0):
        self.color = color
        self.mark = mark
        self.kuzov = kuzov
        self.speed = speed
        self.transmission = transmission
    
    def start(self):
        print(f"машина начала движение, ее скорость:  {self.speed} км/ч")
        self.speed = 10
    def stop(self):
        print("\nмашина остановилась")
        self.speed = 0
    def turn(self):
        storona = input("\nв какую сторону поворот? направо/налево ")
        if storona == "налево":
            print("машина повернула налево")
        else:
            print("машина повернула направо")
    def speed_up(self):
           self.speed += 50
           if self.kuzov == 'truck':
                 if self.speed >=60:
                    self.speed = 60
                    print('/мы нажали на газ!')
                    print(f'Скорость превышена! разрешенная скорость 60км/ч. \nскорость: {self.speed} км/ч')
                 else:
                  print('\nмы нажали на газ!')
                  print(f'скорость машины {self.speed} км/ч')
           else:
                if self.speed >= 80:
                    self.speed = 80
                    print('\nмы нажали на газ!')
                    print(f'Скорость превышена! разрешенная скорость 80 км/ч. \nскорость:  {self.speed} км/ч')
                else:
                    print('\nмы нажали на газ!')
                    print(f'скорость машины: {self.speed} км/ч')

    def speed_down(self):
        if self.speed == 0:
            print('скорость 0 км/ч')
        else:
            self.speed -= 50
        print('\nмашина замедляется')
        print(f'скорость машины {self.speed}')
    def beep(self):
        print("биип")
car = Car("black", "lada", "sedan", "mechanic")
truck = Car("white", "mersedes", "truck", "automatic")


print(f"car.mark, car.color, car.kuzov, car.transmission\n")

print("скорость: ", car.speed, " км/ч")
car.speed_up()
print()
car.speed_up()
print()
car.speed_down()
print()
car.turn()
print()
car.stop()
print()
print("машина сделала" , end = " ")
car.beep()

print()
print()

sleep(1)

print(f"truck.mark, truck.color, truck.kuzov, truck.transmission\n")

print("скорость: ", truck.speed, " км/ч")
truck.start()
print()
truck.speed_up()
print()
truck.speed_up()
print()
truck.speed_down()
print()
truck.turn()
print()
truck.stop()
print()
print("грузовик сделал" , end = " ")
truck.beep()