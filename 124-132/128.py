from tkinter import *

def km ():
    entry_box2.delete(0, END)
    entry_box2.insert(0, float(entry_box.get()) * 0.6214)
def mil():
    entry_box2.delete(0, END)
    entry_box2.insert(0, float(entry_box.get()) * 1.6093)

window = Tk()
window.title("rast")
window.geometry("500x200")
label = Label(text = "введите расстояние и выберете во что перевести")
label.place(x = 110, y = 30)
button1 = Button(text = "в км", command = km)
button1.place(x = 80, y = 70)
button2 = Button(text = "в мили", command = mil)
button2.place(x = 60, y = 100)
entry_box = Entry(text = 0)
entry_box.place(x = 140, y = 70, height = 50)
entry_box2 = Entry()
entry_box2.place(x = 250, y = 70, height = 50)

window.mainloop()