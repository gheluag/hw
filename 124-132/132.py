from tkinter import *

def dobav():
    chel = entry_box.get() + " " + entry_box2.get()
    file = open("124-138/124-132/nameage.csv", "a")
    file.write(f"{chel} \n")
    file.close()

def out():
    file = open("124-138/124-132/nameage.csv", "r")
    msg = Label(window, text = f"{file.read()}")
    msg.place(x = 160, y = 250)
    file.close()


window = Tk()
window.title("sozdai")
window.geometry("400x400")
label = Label(text = 'введите имя: ')
label.place(x = 140, y = 30)
entry_box = Entry()
entry_box.place(x = 140, y = 60)
label1 = Label(text = 'введите возраст: ')
label1.place(x = 140, y = 80)
entry_box2 = Entry()
entry_box2.place(x = 140, y = 100)
button = Button(text = "nazhmi!", command = dobav)
button.place(x = 140, y = 150, width = 120, height = 25)
button_out = Button(text = "вывести!", command = out)
button_out.place(x = 140, y = 200, width = 120, height = 25)

window.mainloop()