class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
    def view(self):
        print(f"я, {self.login} - пользователь и могу просматривать содержимое! ")
class Moderator(User):
    def __init__(self, group_id):
        super().__init__("jaba", "kva")
        self.group_id = group_id
    def view(self):
        print(f"я, {self.login} - модератор и я могу просматривать содержимое!")
    def redact(self):
         print(f"я, {self.login} - модератор и я могу редактировать содержимое!")

user_1 = User("kitik", "meow")
user_2 = Moderator("moder123")
user_1.view()
user_2.view()
user_2.redact()