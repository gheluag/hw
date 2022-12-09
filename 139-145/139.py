import sqlite3

with sqlite3.connect("139-145/phonebook.db") as db:
    cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS names(
id integer PRIMARY KEY,
name text NOT NULL,
surname text NOT NULL,
phonenumb text NOT NULL);""")
cursor.execute("""INSERT INTO names(id, name, surname, phonenumb)
VALUES("1", "Simon", "Howeis", "01223 349752")""")
cursor.execute("""INSERT INTO names(id, name, surname, phonenumb)
VALUES("2", "Karen", "Phillips", "01954 295773")""")
cursor.execute("""INSERT INTO names(id, name, surname, phonenumb)
VALUES("3", "Darren", "Smith", "01583 749012")""")
cursor.execute("""INSERT INTO names(id, name, surname, phonenumb)
VALUES("4", "Anne", "Jones", "01323 567322")""")
cursor.execute("""INSERT INTO names(id, name, surname, phonenumb)
VALUES("5", "Mark", "Smith", "01223 855534")""")
db.commit()
cursor.execute("SELECT * FROM names")
for x in cursor.fetchall():
    print(x)
db.close()
