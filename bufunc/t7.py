# не удалось понять декораторы ;_;
# попытка что-то сделать

from os import name
def dec(funcdec):
  def wrapper():
    print("Hello,", name)
  funcdec()
  return wrapper

@dec
def get_name():
  name = input('Введите имя: ')
  # print(name)
  return name
  
get_name()