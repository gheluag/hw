from re import *
def checker():
    try:
     login = input("введите логин: ")
     if search("[!@#$%^&*()_+]", login):
        raise ValueError
     else:
        print("никаких проблем!")
    except ValueError:
        print("недопустимые символы!")
checker()