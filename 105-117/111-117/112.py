import csv

file = open("105-117/111-117/books.csv", "a")

book = input("введите название книги: ")
auth = input("введите автора: ")
year = input("введите год: ")

new_b = book + ", " + auth + ", " + year  + "\n" 
file.write(new_b)
file.close()

file = open("105-117/111-117/books.csv", "r")
for row in file:
    print(row)
file.close()