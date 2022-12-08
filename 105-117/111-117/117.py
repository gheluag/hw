import csv
from random import randint


name = input("введите имя: ")
vopros = [
    "хорошо время проводите? ",
    "сколько времени сейчас? ", 
    "любимый музыкальный исполнитель? ",
    "чем занимаетесь? ", 
    "любимый персонаж ", 
    "сколько книг прочитано? ", 
    "счастлив? ",
    "стоит жить хотя бы ради пьяной вишни? "]

rnd1 = randint(0, len(vopros) - 1)
rnd2 = randint(0, len(vopros) - 1)
def rand_vop():
    if rnd1 == rnd2:
        rnd2 = randint(0, len(vopros) - 1)
        return rand_vop()
    return

answ = input(vopros[rnd1])
answ2 = input(vopros[rnd2])

fansw = f"{name}, {vopros[rnd1]} {answ}"
fansw2 = f"{name}, {vopros[rnd2]} {answ2}"

file = open("105-117/111-117/game.csv", "a")
file.write(f"{fansw}\n")
file.write(f"{fansw2}\n")
file.close()

file = open("105-117/111-117/game.csv", "r")
for row in file:
    print(row)