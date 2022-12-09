import sqlite3

book_year = []

with sqlite3.connect("139-145/bookinfo.db") as db:
    cursor = db.cursor()

year = input("введите год: ")
cursor.execute(f"SELECT * FROM books WHERE date > '{year}' ")
for x in cursor.fetchall():
        book_year.append(x)

sort = sorted(book_year)
print(sort)

db.close()