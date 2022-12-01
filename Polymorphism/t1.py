class Batary():
    def __init__(self):
        self.capacity = []
        self.max_charge = 5
        self.min_charge = 0

    def __str__(self):
        return '[' + ''.join(self.capacity) +']'

    def charge(self):
        if len(self.capacity) >= self.max_charge:
            print("заряжено!")
        else:
            self.capacity.append(')')

    def discharge(self):
        if len(self.capacity) <= 0:
            print("нет зарядки!")
        else:
            self.capacity.pop(0)
       
bat = Batary()
bat.charge()
bat.charge()
bat.discharge()
bat.charge()
bat.charge()
bat.charge()
bat.discharge()
print(bat)
