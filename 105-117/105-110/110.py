name_list = []
name2_list = []

file =  open("105-117/105-110/names.txt", "r")
name_list = file.read().split()
print(" \n".join(name_list))

name = input("введите имя: ")

for n in name_list:
    if name == n:
        continue
    name2_list.append(n)

new_file = open("105-117/105-110/names2.txt", "w")
name2 = "\n".join(name2_list) 
new_file.write(name2)
new_file.close()

