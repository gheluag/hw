danet = "y"
while(danet!= 'n'):

    def calcul():

        a = float(input('введите первое число:'))
        b = float(input('введите второе число:'))
        znak = input('введите операцию: ')
        
        if znak == "+":
            print(a+b)
        elif znak == "-":
            print (a-b)
        elif znak == "*":
            print(a*b)
        elif znak == "/" and b == 0:
            print("err")
        elif znak == "/":
            print(a/b)
            
        
    calcul()
    danet = input('совершить еще одно действие? y/n:')