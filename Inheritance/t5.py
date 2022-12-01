from time import time, localtime
class Clock:
    @staticmethod
    def say_time():
        vremya = localtime(time())
        print(f"{vremya.tm_hour} : {vremya.tm_min} : {vremya.tm_sec}")
Clock.say_time()