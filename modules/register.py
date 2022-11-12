log = input("введите логин: ")
# passw = input("введите пароль: ")
base_log = ["jaba", "ildar", "artur", "aizat"]
# base_passw = ["kva", "jab", "cat", "meow"]
def checker():
    
    if log not in base_log:
        prov = True
    else: prov = False
    return prov

def validate():
    nedop = ["#", "$", "%", "&"]
    if nedop[0] in log:
        return
    elif nedop[1] in log:
        return
    elif nedop[2] in log:
        return
    elif nedop[3] in log:
        return
    else:
        prov = True
    return prov


def register():
    if checker() == True and validate() == True:
        base_log.append(log)
        # base_passw.append(passw)
        print("вы успешно зарегестрировались!")
    else:
        print("произошла ошибка")