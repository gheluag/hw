import sqlite3

with sqlite3.connect("139-145/phonebook.db") as db:
    cursor = db.cursor()

print("\nmain menu \n 1) View phone book\n2) Add to phone book\n3) Search for surname\n4) Delete person from phone book\n5) Quit ")
chos = int(input())
while chos != 5:
    if chos == 1:
        cursor.execute("SELECT * FROM names")
        for x in cursor.fetchall():
            print(x)
    elif chos == 2:
        newID = input("Enter ID number: ")
        newname = input("Enter name: ")
        newsurn = input("Enter surname: ")
        newphone = input("Enter phone: ")
        cursor.execute("""INSERT INTO names(id, name, surname, phonenumb)
        VALUES(?, ?, ?, ?)""",(newID, newname, newsurn, newphone))
        db.commit()
    elif chos == 3:
        surn = input("enter surn: ")
        cursor.execute(f"SELECT * FROM names WHERE surname = '{surn}'") 
        for sur in cursor.fetchall():
            print('\n', sur)
    elif chos == 4:
        id = input("enter id: ")
        cursor.execute(f"DELETE FROM names WHERE id = '{id}'")
        
    elif chos == 5:
        db.close()
        break

    else:
        print("err")
    print("\nmain menu \n 1) View phone book\n2) Add to phone book\n3) Search for surname\n4) Delete person from phone book\n5) Quit ")
    chos = int(input())

