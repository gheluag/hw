from random import randint
import time as t
chisl = (randint(0, 100))

print("поучаствуйте в игре! вам нужно угадать загаданное число от 0 до 100 за 10 попыток")
t.sleep(2)
print("3..", end = " ")
t.sleep(1)
print("2..", end = " ")
t.sleep(1)
print("1..", end = " ")
t.sleep(0.5)
print()
def random(ot):
    # popit = 10
    print(f"число попыток: {ot}")
    ugad = int(input("введите число: "))
    
    if ugad > chisl:
        # popit-=1
        print(f"число меньше, чем {ugad} \n")
    elif ugad < chisl:
        # popit-=1
        print(f"число больше, чем {ugad}\n ")
    elif ugad == chisl:
        print(f"ура! вы отгадали! это число: {chisl}\n вы угадали за {ot} попыток ")
        return
    if ot == 1:
        print(f"вы не угадали.. это число: {chisl} ")
        return
    
    random (ot - 1)

random(10)
