file = open("105-117/105-110/names.txt", "a")
name = input("введите имя: ")
file.write(f"\n{name}")
file = open("105-117/105-110/names.txt", "r")
print(file.read())
file.close()
