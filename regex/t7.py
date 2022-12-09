from t6 import *
import hashlib
class User:
    def __init__(self):
        self.get_login()
        self.get_password()
    def get_login(self):
        return checker()
        
    def get_password(self):
        password = input('введите пароль: ')
        self.get_hash(password)
    def get_hash(self, str):
       self.password = hashlib.md5(str.encode("utf8"))
       

us_1 = User()
print(us_1)

# очень очень странно
# 2 раза просит логин..
# и выводит страшно: (<__main__.User object at 0x000001D798D1F610>)