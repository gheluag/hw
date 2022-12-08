from tkinter import *

def okno():
   msg = Label(window, text = f"привет, \n {entry_box.get()}! ")
   msg.place(x = 30, y = 50)
   msg["bg"] = "violet"
   msg ["fg"] = "yellow"


window = Tk()
window.title("ku")
window.geometry("400x200")
label = Label(text = 'введите имя: ')
label.place(x = 150, y = 30)
entry_box = Entry(text = 0)
entry_box.place(x = 140, y = 60)
button = Button(text = "nazhmi", command = okno)
button.place(x = 140, y = 90, width = 120, height = 25)

window.mainloop()