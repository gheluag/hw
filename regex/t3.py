from re import *

def find_email():
    str='Всем привет! Меня зовут Алексей. Мой email: alexVB@gmail.com. Привет, Алексей! Меня зовут Марина, моя почта: Marina@mail.ru'
    mail = findall(r"\w+@\w+.\w+", str)
    return mail
print(find_email())