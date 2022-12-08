from tkinter import *


window = Tk()
window.geometry("250x300")

photo = PhotoImage(file = "124-138/133-138/2.gif")
photobox = Label(window, image = photo)
photobox.image = photo
photobox.place(x = 20, y = 50)

entry_box = Entry()
entry_box.place(x = 20, y = 20, width=200, height=20)


def prekoli():
    korten = entry_box.get()
    if korten == "1": 
            photo = PhotoImage(file = "124-138/133-138/1.gif") 
            photobox.image = photo 
            photobox["image"] = photo 
            photobox.update()
    elif korten == "2": 
            photo = PhotoImage(file = "124-138/133-138/2.gif") 
            photobox.image = photo
            photobox["image"] = photo 
            photobox.update()
    elif korten == "3": 
            photo = PhotoImage(file = "124-138/133-138/3.gif") 
            photobox.image = photo 
            photobox["image"] = photo 
            photobox.update()
    else: 
            photo = PhotoImage(file = "124-138/133-138/stare.gif") 
            photobox.image = photo 
            photobox["image"] = photo 
            photobox.update()
    
while True:
    prekoli()

window.mainloop()