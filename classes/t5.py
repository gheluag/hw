from time import sleep

class Trafficlight:
    def __init__(self, light):
        self.light = light
        
    def red(self):
        sleep(1)
        print("red light")
    def yellow(self):
        sleep(0.5)
        print("yellow light")
    def green(self):
        sleep(2)
        print("green light")
traffic_red = Trafficlight("red_light")
traffic_yellow = Trafficlight("yellow_light")
traffic_green = Trafficlight("green_light")

traffic_red.red()
traffic_yellow.yellow()
traffic_green.green()