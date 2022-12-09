import sqlite3

with sqlite3.connect("139-145/bookinfo.db") as db:
    cursor = db.cursor()

name = input("введите имя: ")
cursor.execute(f"SELECT * FROM books WHERE author =  '{name}' ")
for x in cursor.fetchall():
    file = open("139-145/auth.txt", "a")
    file.write(f"{x[0]} - {x[1]} - {x[2]} - {x[3]}\n")
    file.close()
db.close()