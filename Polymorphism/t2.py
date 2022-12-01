class Queue:
    def __init__(self):
        self.inside = ["жаб", "китик", "ёжик"]
    def __add__(self, other):
        self.inside.append(other)
    def __isub__(self, other):
        self.inside.pop(other)
        return self
    def __str__(self):
        return " <= ".join(self.inside)   # в другую сторону не очень правильно
    def add(self):
        name = input("введите имя: ")     # или название животного в данном случае
        self.inside.append(name)
    def take_out(self):
        self.inside.pop(0)
q = Queue()
print(q)
q.add()
q.take_out()
print(q)
q.add()
q.take_out()
print(q)