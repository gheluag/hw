def calc():
    a = float(input('введите число: '))
    b = float(input('введите число: '))
    oper = input('введите операцию: ')
    if oper == '/' and b == 0:
        print("ошибка! деление на ноль!")
    else:
        print(eval(f"{a}{oper}{b}"))
calc()
