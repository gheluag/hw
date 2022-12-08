print("1) Create a new file \n2) Display the file \n3) Add a new item to the file ")
chislo = int(input("1,2,3: "))
if chislo == 1:
    file = open("105-117/105-110/subject.txt", "w")
    pred = input("введите название школьного предмета:\n")
    file.write(f"\n{pred}")
elif chislo == 2:
    file = open("105-117/105-110/subject.txt", "r")
    print(file.read())
elif chislo == 3:
    file = open("105-117/105-110/subject.txt", "a")
    pred2 = input("введите название школьного предмета:\n")
    file.write(f"\n{pred2}")
    file = open("105-117/105-110/subject.txt", "r")
    print(file.read())
else:
    print("ошибка!")
file.close()