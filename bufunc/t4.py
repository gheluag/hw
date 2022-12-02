def cesar():
    perem = input("введите слово: ")
    for char in perem:
        ispr = ord(char) + 3
        print(chr(ispr), end = " ")
           

cesar()