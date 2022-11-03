from time import sleep
from random import sample
def countdown():
    rnd = (sample(range(0, 11), 11))
    rnd.sort(reverse = True)
    rnd = map(str, rnd)
    ot = ' '.join(rnd)
    for i in ot:
      sleep(0.2)
      print(i, end= "")
    sleep(0.4)
    print(" пуск!")
    sleep(0.5)
    
countdown()