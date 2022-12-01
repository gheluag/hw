class Good:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight
    def calcul(self):
        self.cost = self.price * self.weight
apple = Good(price = 100, weight= 1.5)
pear = Good(price = 120, weight =  0.8)
apple.calcul()
pear.calcul()
print(f"стоимость яблок {apple.cost}")
print(f"стоимость груш {pear.cost}")