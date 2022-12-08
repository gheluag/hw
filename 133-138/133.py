from tkinter import *

def name():
    entrybox.delete(0, END)
    entrybox.insert(0, f"hello, {entry.get()} ")
    

window = Tk()
window.title("name")
window.geometry("500x500")
logo = PhotoImage(file = "124-138/133-138/stare.gif")
logoss = Label(window, image = logo)
logoss.place(x = 140, y = 40)
label = Label(window, text = "введите имя")
label.place(x = 200, y = 270)
entry = Entry(text = 0)
entry.place(x = 180, y = 300)
entrybox = Entry()
entrybox.place(x = 180, y = 400)
button = Button(text = "press" , command = name)
button.place(x = 140, y = 350)

window.mainloop()