def login():
    baza = {}
    while True:
        login = input("Введите логин: ")
        parol = input("Введите пароль: ")

        passw = baza.get(login)
        if passw == parol:
            print("Вы успешно авторизовались")
        elif not passw:
            baza[login] = parol
            print("Регистрация прошла успешно")
        else:
            print("Неверный пароль, доступ запрещен")
            break

login()