from tkinter import *
from random import randint

def chto():
    rand1 = randint(10,50)
    rand2 = randint(10,50)
    sum = rand1 + rand2
    return sum


def rand():
    sum = chto()
    if sum == int(entry2.get()):
        msg = Label(window, image = ura )
        msg.place(x = 170, y = 50)
        msg2 = Label(window, text =f"сумма чисел: {sum} ")
        msg2.place(x = 220, y = 270)
    else:
        msg = Label(window, image = no)
        msg.place(x = 170, y = 50)
        msg2 = Label(window, text =f"сумма чисел: {sum} ")
        msg2.place(x = 220, y = 270)
    button1["state"] = "disabled"
    msg.update()
def again():
    entry2.delete(0, END)
    button1["state"] = "active"
    

window = Tk()
window.title("ugadai")
window.geometry("500x500")

entry2 = Entry(text = 0)
entry2.place(x = 190, y = 300, height = 40)
button1 = Button(text = "otvet", command = rand)
button1.place(x = 160, y = 400, heigh = 40)
button2 = Button(text = "next", command = again)
button2.place(x = 300, y = 400, heigh = 40)
ura = PhotoImage(file = "124-138/133-138/hypers.gif")
no = PhotoImage(file = "124-138/133-138/sadge.gif")


window.mainloop()