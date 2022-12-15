import csv

file = open("105-117/111-117/books.csv", "r")
leng = len(file.read().split("\n"))
file.close()

num_list = []

file = open("105-117/111-117/books.csv", "r")
for i in range(leng):
    num_list.append(i + 1)
for i, row in zip(num_list, file):
    print(f"{i}) {row}")
file.close()
