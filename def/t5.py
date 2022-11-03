def fib():
    a = 1
    b = 0
    print(b, end = " ")
    while a+b <=100:
        a,b = b ,a +b
        print(b, end = " ")
fib()

print()

#рекурсия

lst = [0,1]

def fib1(lst = [0,1], a = 0 , b = 1):
    i = len(lst)
    b = lst[i-1]
    a = lst[i-2]
    c = a + b
    lst.append(c)
    if b >= 50:
        print(lst)  
        return
    else: fib1(lst, a , b)
    return lst
    
fib1()