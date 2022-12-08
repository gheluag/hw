import csv

file = open("105-117/111-117/books.csv", "r")
year1 = int(input("введите начальный год: "))
year2 = int(input("введите конечный год год: "))

for row in file:
    if row in range(year1-1, year2 +1):
        print(row)
    else:
        print("net")
file.close()
