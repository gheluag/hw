from math import *
def engineering():
    perv = float(input("введите первое число: "))
    vtor = float(input("введите второе число: "))
    print("введите операцию\n 'root' или 'pow'")
    znak = input()
    if znak == 'root':
        print(f"root of {perv}: {sqrt(perv)}, {vtor}: {sqrt(vtor)}")

    elif znak == 'pow':
    
        print(f"pow: {pow(perv,vtor)}")
    else:
        print("error")
engineering()