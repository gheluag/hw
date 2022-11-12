from register import *
from time import sleep
base_passw = {"jaba" : "kva", "ildar" : "jab", "artur" : "cat", "aizat" : "meow" }

def login():
    
    passw = input("введите пароль: ")
    
    password = base_passw.get(log)
    if password and password == passw:
        print("доступ разрешён!")
    elif not password:
        register()
        base_passw[log] = passw
        print("регистрация прошла успешно!")
    else:
        print("доступ запрещён!")
        

def del_user():
    passw = input("введите пароль: ")
    udali = input("какой логин удалить? ")
    base_passw.pop(udali)
    sleep(0.7)
    print("подождите", end = " ")
    for i in range(3):
        sleep(0.3)
        print("." , end = " ")
    print("\nлогин успешно удален")
    return udali