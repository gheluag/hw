# for

def fib():
    fibon = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    i = iter(fibon)
    for x in i:
        print(x, end = " ")
    
  
fib()

print()

#next()

def fibon():
    fibon = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    i = iter(fibon)
    while i != 10:
        print(next(i), end = " ")
    
  
fibon()