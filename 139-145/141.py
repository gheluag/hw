import sqlite3

with sqlite3.connect("139-145/bookinfo.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS authors(
 name text NOT NULL,
 place text NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS books(
 id integer PRIMARY KEY,
 title text NOT NULL,
 author text NOT NULL,
 date integer NOT NULL);""")

db.close()