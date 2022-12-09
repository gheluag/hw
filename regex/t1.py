def validator():
    

    try:
        
        chislo = int(input("введите число: "))
        c = chislo ** 2
        return c

      
    except ValueError:
        c = "введено не число"

    finally:
        print(c)
    
    
validator()