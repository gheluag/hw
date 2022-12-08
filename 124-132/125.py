from tkinter import *
from random import randint

def dice():
    kubik = randint(1,6)
    msg = Label(window, text = f"ваше число: {kubik}")
    msg.place(x = 20, y = 60)


window = Tk()
window.title("Dice")
window.geometry("400x200")
label = Label(text = 'испытай судьбу! \nреролл или нет?... ')
label.place(x = 140, y = 30)
button = Button(text = "roll", command = dice)
button.place(x = 140, y = 90, width = 120, height = 25)
window.mainloop()