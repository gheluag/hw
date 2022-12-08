from random import randint

class Box:
    def __init__(self, postcode, name, from_city, target_city):
        self.__postcode = postcode
        self.__name = name
        self.__from_city = from_city
        self.__target_city = target_city

    @property
    def postcode(self):
        return self.__postcode
    @property
    def name(self):
        return self.__name
    @property
    def from_city(self):
        return self.__from_city
    @property
    def target_city(self):
        return self.__target_city
    def __str__(self):
        return f"посылка {self.name} едет с {self.from_city} в {self.target_city}, postcode: {self.postcode} "
    def __repr__(self):
        return f'посылка {self.name} едет с {self.from_city} в {self.target_city} postcode: {self.postcode}'   # я запуталась... без этого не выводит добавленную коробку


box1 = Box(randint(100000, 999999), 'hikaru', 'Москва', 'Казань' )
box2 = Box(randint(100000, 999999), 'bushe', 'Санкт-Петербург', 'Алматы' )
box3 = Box(randint(100000, 999999), 'stershine', 'Челябинск', 'Набережные Челны')

