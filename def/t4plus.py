def count():
    a = 0
    countchet = 0
    countnechet = 0
    while a < 10:
        a+=1
        if a % 2 == 0:
            countchet +=1
        elif a % 2 != 0:
            countnechet+=1
           
    print(f"количество четных: {countchet}, количество нечетных {countnechet}")
count()

# print()


#рекурсия


def count1(a,even = 0,odd = 0):
    
    
    if a == 0 :
        print(f"кол-во четных: {even}, нечетных: {odd}")
        return
    else:
        if a % 2 == 0:
            even +=1
            # print(a)
        else:
            odd += 1
            # print(a)
        
        count1(a-1, even, odd)
    
count1(10)
