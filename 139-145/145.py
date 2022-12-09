from tkinter import *
import sqlite3

with sqlite3.connect("139-145/testscore.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS student(
 name text NOT NULL,
 grade integer NOT NULL);""")

def add():
    name = namebox.get()
    grade = gradebox.get()
    cursor.execute("""INSERT INTO student (name, grade)
    VALUES(?, ?)""", (name, grade))
    db.commit()


def clear():
    namebox.delete(0, END)
    gradebox.delete(0, END)


window = Tk()
window.title("testscore")
window.geometry("300x300")
label1 = Label(window, text = "enter student's name")
label1.place(x = 100, y = 50)
namebox = Entry()
namebox.place(x = 100, y = 80)
label2 = Label(window, text = "enter student's grade")
label2.place(x = 100, y = 110)
gradebox = Entry()
gradebox.place(x = 100, y = 130)
button_add = Button(text = "add", command = add)
button_add.place(x = 100, y = 160)
button_clear = Button(text = "clear", command = clear)
button_clear.place(x = 180, y = 160)


window.mainloop()
db.close()