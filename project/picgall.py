import sqlite3
from tkinter import *

with sqlite3.connect("project/picture gallery.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS artist_info(
 artistID integer PRIMARY KEY,
 name text NOT NULL,
 adress text NOT NULL,
 town text NOT NULL,
 country text NOT NULL,
 postcode text NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS pictures(
 pieceID integer PRIMARY KEY,
 artistID integer,
 title text NOT NULL,
 medium text NOT NULL,
 price integer,
 FOREIGN KEY (artistID) REFERENCES artist_info (artistID));""")

def find():
    window.withdraw()
    def mm():
        findwindow.withdraw()
        window.deiconify()
    def buy():
        def mainm():
            buywin.withdraw()
            window.deiconify()
        def oformi():
            uspeh = Label(buywin, text = "успешно", font = "georgia 12")
            uspeh["bg"] = "#a49eba"
            uspeh.place(x = 180, y = 100)
            kuplen = entry1.get()
            deliv = select.get()
            cursor.execute(f"SELECT * FROM pictures WHERE pieceID = '{kuplen}'")
            for x in cursor.fetchall():
                file = open("project/sold.txt", "a")
                file.write(f"sold   pieceID: {x[0]}  artistID: {x[1]}   title: {x[2]}   medium: {x[3]}  price: {x[4]}\n customer: {entry2.get()}, phone number: {entry3.get()}, delivery: {deliv}\n\n\n")
                file.close()
            cursor.execute(f"DELETE FROM pictures WHERE pieceID = '{kuplen}'")
            db.commit()


        findwindow.withdraw()
        buywin = Tk()
        buywin.geometry("500x300")
        buywin["bg"] = "#a49eba"
        buywin.title("покупка")
        
        label = Label(buywin, text = "введите ID картины", font = "georgia 8")
        label.place(x = 10, y = 10)
        label["bg"] = "#a49eba"
        
        entry1 = Entry(buywin)
        entry1.place(x = 10, y = 30)
        
        label2 = Label(buywin, text = "введите имя", font = "georgia 8")
        label2.place(x = 10, y = 50)
        label2["bg"] = "#a49eba"
        
        entry2 = Entry(buywin)
        entry2.place(x = 10, y = 70)
        
        label3 = Label(buywin, text = "введите номер телефона", font = "georgia 8")
        label3.place(x = 10, y = 100)
        label3["bg"] = "#a49eba"
        
        entry3 = Entry(buywin)
        entry3.place(x = 10, y = 120)
        
        select = StringVar(buywin)
        select.set("выберете способ доставки")
        option = OptionMenu(buywin, select, "самовывоз", "доставка")
        option.place(x = 150, y = 10, width = 150)
        option["bg"] = "#948eab"
        option["activebackground"] = "#7f7994"
        
        button1 = Button(buywin, text = "оформить", command = oformi, font = "georgia 8")
        button1["bg"] = "#948eab"
        button1["activebackground"] = "#7f7994"
        button1.place(x = 150, y = 50)
        
        button_q = Button(buywin, text = "выйти", command = quit, font = "georgia 8")
        button_q["bg"] = "#948eab"
        button_q["activebackground"] = "#730e1d"
        button_q.place(x = 450, y = 270)
        
        button_mm = Button(buywin, text = "вернуться в главное меню", command = mainm, font = "georgia 8" )
        button_mm.place(x = 300, y = 270)
        button_mm["bg"] = "#948eab"
        button_mm["activebackground"] = "#7f7994"

        buywin.mainloop()

        
    def opt():
        def name_find():

            name = entry1.get()
            listbox = Listbox(findwindow)
            listbox.place(x = 0, y = 150, width = 500)
            listbox["bg"] = "#a49eba"
           
            cursor.execute(f"SELECT * FROM artist_info WHERE name = '{name}'")
            for na in cursor.fetchall():
                cursor.execute(f"SELECT * FROM pictures WHERE artistId = '{na[0]}'")
                for x in cursor.fetchall():
                    viv = f"pieceID: {x[0]}  artistID: {x[1]}   title: {x[2]}   medium: {x[3]}  price: {x[4]}\n\n\n"
                    listbox.insert(0, viv)
            
            label = Label(findwindow, text = "запомните id картины", font = "georgia 8")
            label.place(x = 20, y = 420)
            label["bg"] = "#a49eba"
            
            button_buy = Button(findwindow, text = "купить", command = buy, font = "georgia 8")
            button_buy.place(x = 20, y = 450)
            
        def med_find():
            tech = entry1.get()
            listbox = Listbox(findwindow)
            listbox.place(x = 0, y = 150, width = 500)
            listbox["bg"] = "#a49eba"
            
            cursor.execute(f"SELECT * FROM pictures WHERE medium =  '{tech}' ")
            for x in cursor.fetchall():
                viv = f"pieceID: {x[0]}  artistID: {x[1]}   title: {x[2]}   medium: {x[3]}  price: {x[4]}\n\n\n"
                listbox.insert(0, viv)
            
            label = Label(findwindow, text = "запомните id картины", font = "georgia 8")
            label.place(x = 20, y = 420)
            label["bg"] = "#a49eba"
            
            button_buy = Button(findwindow, text = "купить", command = buy, font = "georgia 8")
            button_buy.place(x = 20, y = 450)
        
        def price_find():
            price = entry1.get()
            listbox = Listbox(findwindow)
            listbox.place(x = 0, y = 150, width = 500)
            listbox["bg"] = "#a49eba"
            cursor.execute(f"SELECT * FROM pictures WHERE price <=  '{price}' ")  # нам кажется лучше еще и до введенной цены вывести
            
            for x in cursor.fetchall():
                viv = f"pieceID: {x[0]}  artistID: {x[1]}   title: {x[2]}   medium: {x[3]}  price: {x[4]}\n\n\n"
                listbox.insert(0, viv)
            
            label = Label(findwindow, text = "запомните id картины", font = "georgia 8")
            label.place(x = 20, y = 420)
            label["bg"] = "#a49eba"
            
            button_buy = Button(findwindow, text = "купить", command = buy, font = "georgia 8")
            button_buy.place(x = 20, y = 450)
        
        sel = select.get()
       
        match sel:
           
            case "имя художника":
                
                name = Label(findwindow, text = "введите имя художника", font = "georgia 8")
                name.place(x = 200, y = 20)
                name["bg"] = "#a49eba"
                
                entry1 = Entry(findwindow)
                entry1.place(x = 200, y = 50)
                
                button_op = Button(findwindow, text = "найти", command = name_find)
                button_op.place(x = 200, y = 90)
                button_op["bg"] = "#948eab"
                button_op["activebackground"] = "#7f7994"
                
            case "техника исполнения":
                
                name = Label(findwindow, text = "введите технику исполнения", font = "georgia 8")
                name.place(x = 200, y = 20)
                name["bg"] = "#a49eba"
                
                entry1 = Entry(findwindow)
                entry1.place(x = 200, y = 50)
                
                button_op = Button(findwindow, text = "найти", command = med_find, font = "georgia 8")
                button_op.place(x = 200, y = 90)
                button_op["bg"] = "#948eab"
                button_op["activebackground"] = "#7f7994"
            
            case "ценовая категория":
                
                name = Label(findwindow, text = "введите цену", font = "georgia 8")
                name.place(x = 200, y = 20)
                name["bg"] = "#a49eba"
               
                entry1 = Entry(findwindow)
                entry1.place(x = 200, y = 50)
               
                button_op = Button(findwindow, text = "найти", command = price_find, font = "georgia 8")
                button_op.place(x = 200, y = 90)
                button_op["bg"] = "#948eab"
                button_op["activebackground"] = "#7f7994"
                
    
    
    findwindow = Tk()
    findwindow.title("find picture")
    findwindow.geometry("500x500")
    findwindow["bg"] = "#a49eba"

    select = StringVar(findwindow)
    select.set("выберете парметр")
    option = OptionMenu(findwindow, select, "имя художника", "техника исполнения", "ценовая категория")
    option.place(x = 30, y = 10, width = 150)
    option["bg"] = "#948eab"
    option["activebackground"] = "#7f7994"
    
    button_op = Button(findwindow, text = "выбрать", command = opt, font = "georgia 8")
    button_op.place(x = 30, y = 50)
    button_op["bg"] = "#948eab"
    button_op["activebackground"] = "#7f7994"
    
    button_q = Button(findwindow, text = "выйти", command = quit, font = "georgia 8" )
    button_q.place(x = 430, y = 450)
    button_q["bg"] = "#948eab"
    button_q["activebackground"] = "#730e1d"
    
    button_mm = Button(findwindow, text = "вернуть в главное меню", command = mm, font = "georgia 8" )
    button_mm.place(x = 250, y = 450)
    button_mm["bg"] = "#948eab"
    button_mm["activebackground"] = "#7f7994"
    
    
    findwindow.mainloop()

    
def insert():

    # можно было бы сделать еще с доступом, потому что не каждый пользователь может добавлять, так ведь?
    # но оно и так очень мудренное получилось...

    def clear():
        ent_addr.delete(0, END)
        ent_cou.delete(0, END)
        ent_id.delete(0, END)
        ent_ida.delete(0, END)
        ent_idp.delete(0, END)
        ent_med.delete(0, END)
        ent_name.delete(0, END)
        ent_post.delete(0, END)
        ent_pr.delete(0, END)
        ent_title.delete(0, END)
        ent_town.delete(0, END)

    def mm(): 
        ins.withdraw()
        window.deiconify()

    def dob():
        try:
            newid = ent_id.get()
            newname = ent_name.get()
            newadd = ent_addr.get()
            newtow = ent_town.get()
            newcou = ent_cou.get()
            newpost = ent_post.get()
            
            cursor.execute("""INSERT INTO artist_info(artistID, name, adress, town, country, postcode)
            VALUES(?, ?, ?, ?, ?, ?)""",(newid, newname, newadd, newtow, newcou, newpost))
            db.commit()
        
        except sqlite3.IntegrityError:
           
            newid = "09 "
            newname = "09"
            newadd = "09"
            newtow = "09"
            newcou = "09"
            newpost = "09"
            
            cursor.execute("""INSERT INTO artist_info(artistID, name, adress, town, country, postcode)
            VALUES(?, ?, ?, ?, ?, ?)""",(newid, newname, newadd, newtow, newcou, newpost))
            db.commit()
            cursor.execute(f"DELETE FROM artist_info WHERE artistID = '09'")
            db.commit()

        newidp = ent_idp.get()
        newida = ent_ida.get()
        newtitle = ent_title.get()
        newmed = ent_med.get()
        newpr = ent_pr.get()
        
        cursor.execute("""INSERT INTO pictures(pieceID, artistID, title, medium, price)
        VALUES(?, ?, ?, ?, ?)""",(newidp, newida, newtitle, newmed, newpr))
        db.commit()

    window.withdraw()
    ins = Tk()
    ins.title("insert data")
    ins.geometry("500x500")
    ins["bg"] = "#a49eba"
    
    lab_name = Label(ins, text = "введите имя", font = "georgia 8")
    lab_name["bg"] = "#a49eba"
    lab_name.place(x = 50, y = 40)
    
    ent_name = Entry(ins)
    ent_name.place(x = 50, y = 60)
    
    lab_adress = Label(ins, text = "введите адрес", font = "georgia 8")
    lab_adress["bg"] = "#a49eba"
    lab_adress.place(x = 50, y = 80)
    
    ent_addr = Entry(ins)
    ent_addr.place(x = 50, y = 100)
    
    lab_town = Label(ins, text = "введите город", font = "georgia 8")
    lab_town["bg"] = "#a49eba"
    lab_town.place(x = 50, y = 120)
    
    ent_town = Entry(ins)
    ent_town.place(x = 50, y = 140)
    
    lab_cou = Label(ins, text = "введите страну", font = "georgia 8")
    lab_cou["bg"] = "#a49eba"
    lab_cou.place(x = 50, y = 160)
    
    ent_cou = Entry(ins)
    ent_cou.place(x = 50, y = 180)
    
    lab_post = Label(ins, text = "введите индекс", font = "georgia 8")
    lab_post["bg"] = "#a49eba"
    lab_post.place(x = 50, y = 200)
    
    ent_post = Entry(ins)
    ent_post.place(x = 50, y = 220)
    
    lab_id = Label(ins, text = "введите ID", font = "georgia 8")
    lab_id["bg"] = "#a49eba"
    lab_id.place(x = 50, y = 240)
    
    ent_id = Entry(ins)
    ent_id.place(x = 50, y = 260)
    
    lab_idp = Label(ins, text = "введите ID картины", font = "georgia 8")
    lab_idp["bg"] = "#a49eba"
    lab_idp.place(x = 250, y = 40)
    
    ent_idp = Entry(ins)
    ent_idp.place(x = 250, y = 60)
    
    lab_ida = Label(ins, text = "введите ID художника", font = "georgia 8")
    lab_ida["bg"] = "#a49eba"
    lab_ida.place(x = 250, y = 80)
    
    ent_ida = Entry(ins)
    ent_ida.place(x = 250, y = 100)
    
    lab_title = Label(ins, text = "введите название картины", font = "georgia 8")
    lab_title["bg"] = "#a49eba"
    lab_title.place(x = 250, y = 120)
    
    ent_title = Entry(ins)
    ent_title.place(x = 250, y = 140)
    
    lab_med = Label(ins, text = "введите технику исполнения", font = "georgia 8")
    lab_med["bg"] = "#a49eba"
    lab_med.place(x = 250, y = 160)
    
    ent_med = Entry(ins)
    ent_med.place(x = 250, y = 180)
    
    lab_pr = Label(ins, text = "введите цену", font = "georgia 8")
    lab_pr["bg"] = "#a49eba"
    lab_pr.place(x = 250, y = 200)
    
    ent_pr = Entry(ins)
    ent_pr.place(x = 250, y = 220)
    
    button_dob = Button(ins, text = "добавить", command = dob, font = "georgia 8" )
    button_dob.place(x = 50, y = 400)
    button_dob["bg"] = "#948eab"
    button_dob["activebackground"] = "#7f7994"
    
    button_cl = Button(ins, text = "очистить", command = clear, font = "georgia 8" )
    button_cl.place(x = 120, y = 400)
    button_cl["bg"] = "#948eab"
    button_cl["activebackground"] = "#7f7994"
    
    button_q = Button(ins, text = "выйти", command = quit, font = "georgia 8" )
    button_q.place(x = 400, y = 450)
    button_q["bg"] = "#948eab"
    button_q["activebackground"] = "#730e1d"
    
    button_mm = Button(ins, text = "вернуться в главное меню", command = mm, font = "georgia 8" )
    button_mm.place(x = 230, y = 450)
    button_mm["bg"] = "#948eab"
    button_mm["activebackground"] = "#7f7994"

    ins.mainloop()


window = Tk()
window.title("Picture Gallery")
window.geometry("500x300")
window["bg"] = "#a49eba"             # фиолетовое царство, хихи

great = Label(window, text ="Добро пожаловать в картинную галерею!\n какое действие хотите совершить?", font = "georgia 12")
great["bg"] = "#a49eba"
great.place(x = 100, y = 10)

label_find = Label(window, text = "купить картину", font = "georgia 9")
label_find.place(x = 50, y = 100)
label_find["bg"] = "#a49eba"

button_find = Button(text = "нажми сюда :)", command = find, font = "georgia 8")
button_find.place(x = 50, y = 120)
button_find["bg"] = "#948eab"
button_find["border"] = "2"
button_find["activebackground"] = "#7f7994"

label_ins = Label(window, text = "добавить информацию о художнике и картине", font = "georgia 9")
label_ins.place(x = 200, y = 100)
label_ins["bg"] = "#a49eba"

button_ins = Button(text = "нажми меня :)", command = insert, font = "georgia 8")
button_ins.place(x = 280, y = 120)
button_ins["bg"] = "#948eab"
button_ins["border"] = "2"
button_ins["activebackground"] = "#7f7994"

button_quite = Button(text = "выход", command = quit, font = "georgia 8" )
button_quite.place(x = 400, y = 250)
button_quite["bg"] = "#948eab"
button_quite["activebackground"] = "#730e1d"

window.mainloop()
db.close()