from checkin import *

login()

print("\nжелаете удалить пользователя? 'да/нет:' ")
otv = input()
if otv == "да":
    del_user()
