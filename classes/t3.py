from time import sleep
class Car:
    def __init__(self, color, mark, kuzov, transmission, speed = 0):
        self.color = color
        self.mark = mark
        self.kuzov = kuzov
        self.speed = speed
        self.transmission = transmission
    
    def start(self):
        print("\nмашина начала движение")
        print("скорость: 10 km/h")
        self.speed = 10
    def stop(self):
        print("\nмашина остановилась")
        print('скорость: 0 km/h')
        self.speed = 0
    def turn(self):
        storona = input("в какую сторону поворот? направо/налево ")
        if storona == "налево":
            print("машина повернула налево")
        else:
            print("машина повернула направо")
    def speed_up(self, i=1):
        print("\nмы нажали на газ!")
        print(f"\nскорость: {self.speed + i} km/h")
        self.speed += i
    def speed_down(self, i=1):
        if self.speed == 0:
            print("\nскорость: 0 km/h")
        else:
            print("\nмашина замедляется")
            print(f"скорость: {self.speed - i} km/h")
            self.speed -= i
    def beep(self):
        print("биип")
car = Car("black", "lada", "sedan", "mechanic")
truck = Car("white", "man", "truck", "automatic")

print(car.mark, car.color, car.kuzov, car.transmission, "\n")

print("скорость: ", car.speed, "km/h")
car.start()
car.turn()
car.speed_up(30)
car.speed_down(20)
car.stop()
print("машина сделала " , end = " ")
car.beep()

print()
sleep(1)
print("\n", truck.mark, truck.color, truck.kuzov, truck.transmission, "\n")

print("скорость: ", truck.speed, "km/h")
truck.start()
truck.speed_up(20)
truck.speed_down(10)
truck.turn()
truck.speed_up(30)
truck.speed_down(20)
truck.stop()
print("грузовик сделал " , end = " ")
truck.beep()
