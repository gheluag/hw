#цикл for

def countdown():
    gen = (i for i in range(11)) 
    for viv in gen:
        print(viv, end = " ")
countdown()

print()

#next()

def countdownnext():
    gener = (i for i in range(11)) 
    while gener != 10:
        print(next(gener), end = " ")
countdownnext()