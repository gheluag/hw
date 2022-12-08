from tkinter import *

def color():
    sel = select.get()
    match sel:
        case "violet":
          window["bg"] = "violet"
        case "blue"  : 
            window["bg"] = "blue"
        case "purple":
            window["bg"] = "purple"

window = Tk()
window.title("color")
window.geometry("300x300")
select = StringVar(window)
select.set("Select color")
namesList = OptionMenu(window, select, "violet", "blue", "purple")
namesList.place(x = 30, y = 250)
button = Button(text = "click me", command = color )
button.place(x = 150, y = 100)


window.mainloop()