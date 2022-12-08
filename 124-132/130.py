from tkinter import *
import csv

lst= []

def isdig():
    if entry_box.get().isdigit() == True:
        list_box.insert(END, entry_box.get())
        lst.append(entry_box.get())

    else: 
        entry_box.delete(0, END)
        
    

def clear():
    global lst
    lst = []
    list_box.delete(0, END)

def save():
    tmp_list = "\n".join(lst)
    file = open("124-138/124-132/tmp.csv", "a")
    file.write(tmp_list)
    file.close()


window = Tk()
window.title("int?")
window.geometry("400x500")
label = Label(text = 'введите число: ')
label.place(x = 140, y = 30)
entry_box = Entry(text = 0)
entry_box.place(x = 140, y = 60)
list_box = Listbox()
list_box.place(x = 140, y = 130, height = 150)
button = Button(text = "nazhmi!" , command = isdig)
button.place(x = 140, y = 90, width = 120, height = 25)
button_cls = Button(text = "uberi" , command = clear)
button_cls.place(x = 140, y = 300, width = 120, height = 25)
button_save = Button(text = "save" , command = save)
button_save.place(x = 140, y = 350, width = 120, height = 25)

window.mainloop()