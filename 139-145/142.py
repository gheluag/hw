import sqlite3

with sqlite3.connect("139-145/bookinfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM authors")
for x in cursor.fetchall():
    print(x)

birth_p = input("введите место рождения автора: ")
cursor.execute(f"SELECT * FROM authors WHERE place = '{birth_p}'") 
for bp in cursor.fetchall():
    cursor.execute(f"SELECT * FROM books WHERE author = '{bp[0]}'") 
    for x in cursor.fetchall():
        print(x)
db.close()
