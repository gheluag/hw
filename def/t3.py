name = input('введите имя: ')
list_name = ["азамат", "айзат", "ильдар", "артур"]
def hello_rob():
        if name in list_name:
            print(f"привет, {name}")
            
        else:
            list_name.append(name)
            print(f"привет, {name}, рад познакомиться!")
hello_rob()