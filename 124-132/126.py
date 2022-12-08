from tkinter import *

sum = 0

def chto():
    global sum
    sum += int(entry_box.get())
    entry_box1.delete(0, END)
    entry_box1.insert(0, sum)
    
def clear():
    global sum
    sum = 0
    entry_box1.delete(0, END)
    entry_box.delete(0, END)

window = Tk()
window.title("schet")
window.geometry("400x500")
label = Label(text = 'введите число: ')
label.place(x = 140, y = 30)
entry_box = Entry(text = 0)
entry_box.place(x = 140, y = 60)
entry_box1 = Entry()
entry_box1.place(x = 140, y = 100)
button = Button(text = "сумма!", command = chto)
button.place(x = 140, y = 150, width = 120, height = 25)
button_clear = Button(text = "clear", command = clear)
button_clear.place(x = 140, y = 200, width = 120, height = 25)
window.mainloop()