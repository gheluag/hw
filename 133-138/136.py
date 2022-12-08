from tkinter import *

base = []

def but():
    
    dob = entry.get() + ", " + select.get()
    base.append(dob)
    entry.delete(0, END)
    

window = Tk()
window.title("a?")
window.geometry("300x300")
select = StringVar(window)
select.set("Select")
label = Label(window, text = "введите имя")
label.place(x = 100, y = 100)
entry = Entry()
entry.place(x = 80, y = 150)
namesList = OptionMenu(window, select, "male", "female")
namesList.place(x = 30, y = 250)
button = Button(text = "click!", command = but )
button.place(x = 150, y = 250)


window.mainloop()

