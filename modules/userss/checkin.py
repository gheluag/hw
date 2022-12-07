from register import *
from time import sleep
passw = input("введите пароль: ")
base_passw = {"jaba" : "kva", "ildar" : "jab", "artur" : "cat", "aizat" : "meow" }
def login():
    pas = base_passw.get(log)
    if pas and pas == passw:
        print("доступ разрешён!")
    elif not pas:
        register()
        base_passw[log] = passw
        print("регистрация прошла успешно!")
    else:
        print("доступ запрещён!")
        

def del_user():
    udali = input("какой логин удалить? ")
    base_passw.pop(udali)
    sleep(0.7)
    print("подождите", end = " ")
    for i in range(3):
        sleep(0.3)
        print("." , end = " ")
    print("\nлогин успешно удален")
    return udali