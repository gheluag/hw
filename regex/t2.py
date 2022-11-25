from re import *
def check():

    try:

        class Myexeption(Exception):
            pass

        word = input("введите слово: ")
        if search("[!@#$%^&*]", word):
            raise Myexeption
        else:
            print(word)
    except Myexeption:
        print("недопустимые символы")
check()