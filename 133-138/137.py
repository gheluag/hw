from tkinter import *

base = []

def but():
    
    dob = entry_box.get() + ", " + select.get()
    base.append(dob)
    file = open("124-138/133-138/base.txt", "a")
    file.write(f"{entry_box.get()}, {select.get()}") 
    file.close()
    entry_box.delete(0, END)

def out():
    file = open("124-138/133-138/base.txt", "r")
    msg = Label(window, text =  file.read() )
    msg.place(x = 80, y = 150)
    

window = Tk()
window.title("a?")
window.geometry("300x300")
select = StringVar(window)
select.set("Select")
label = Label(window, text = "введите имя")
label.place(x = 100, y = 180)
entry_box = Entry()
entry_box.place(x = 80, y = 200)
namesList = OptionMenu(window, select, "male", "female")
namesList.place(x = 30, y = 250)
button = Button(text = "click!", command = but )
button.place(x = 150, y = 250)
button_out = Button(text = "вывод", command = out)
button_out.place(x = 200, y = 250)

window.mainloop()

