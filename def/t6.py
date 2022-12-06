def fact():
        chisl = int(input('введите число: '))
        fac = 1
        while chisl > 1:
            fac*= chisl
            chisl -= 1
        print(f"factorial: {fac}")
fact() 
 
print()

#рекурсия


def factor(a):
    if a == 1:
        return 1
    else:
        return factor(a-1) * a
        
print("factorial: ", factor(a = int(input('введите число: '))))