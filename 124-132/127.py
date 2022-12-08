from tkinter import *

def name():
    list_box.insert(END, entry_box.get())

def clear():
    list_box.delete("0", END)
    entry_box.delete("0", END)

window = Tk()
window.title("name")
window.geometry("400x500")
label = Label(text = 'введите имя: ')
label.place(x = 140, y = 30)
entry_box = Entry(text = 0)
entry_box.place(x = 140, y = 60)
list_box = Listbox()
list_box.place(x = 140, y = 130, height = 150)
button = Button(text = "nazhmi!" , command = name)
button.place(x = 140, y = 90, width = 120, height = 25)
button_cls = Button(text = "uberi" , command = clear)
button_cls.place(x = 140, y = 300, width = 120, height = 25)
window.mainloop()