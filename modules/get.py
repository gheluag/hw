def get_login():
    login = input("введите логи: ")
    return login
    




def get_password():
    password= input("введите пароль: ")
    hash_passw = hex(hash(password))
    return hash_passw
