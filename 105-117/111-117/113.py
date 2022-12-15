import csv

file = open("105-117/111-117/books.csv", "a")
count = int(input("сколько записей добавить? "))
for i in range(count):
    book = input("введите название книги: ")
    auth = input("введите автора: ")
    year = input("введитте год: ")
    new_b = book + ", " + auth + ", " + year + "\n"
    file.write(str(new_b))
file.close()
file = open("105-117/111-117/books.csv","r")
who = input("кого ищем? ")
read_who = csv.reader(file)

for row in file:
    if who in row:
        print(row)
        break
    else:
        print("такого нет!")  # почему-то не видит новых добавленных
        break
file.close()