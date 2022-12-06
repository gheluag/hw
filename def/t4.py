def count():
    a = 0
    while a <=10:
        print(a, end = " ")
        a+=1
count()

print()

#рекурсия

def count1(i=0):
    if i == 10:
        print(i)
    else:
        print(i, end = " ")
        return (count1(i+1))
    
    
count1()