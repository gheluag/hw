import csv

file = open("105-117/111-117/books.csv", "w")
book = [
    "to kill a mockingbird",
    "a brief history of time",
    "the great gatsby",
    "the man who mistook his wife for a hat",
    "pride and prejudice"
]

auth = [
    "hasper lee",
    "stephen hawking",
    "f. scott fitzgerald",
    "oliver sacks",
    "jan austen"
]

year = [1960, 1988, 1922, 1985, 1813]

for i in range(len(book)):
    new_books = book[i] + ", " + auth[i]+ ", " + str(year[i]) + "\n"
    file.write((new_books))
file.close()
