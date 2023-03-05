'''
stwórz listę elementów różnych typów i ją posortuj. Wyświetl listę po sortowaniu.
Wskazówka: w razie potrzeby zamień funkcję __str__ na __repr__.
'''
class Car:

    def __init__(self, serial, capacity):
        self.serial = serial
        self.capacity = capacity

    def load(self, good):
        pass

    def __str__(self):
        return f"Car: {self.serial},{self.capacity}"


class PassengerCar(Car):

    def load(self, passengers):
        self.capacity += passengers

    def __str__(self):
        return f"PassengerCar: {self.serial},{self.capacity}"


class FirstClassCar(Car):

    def load(self, passengers):
        self.capacity += 2 * passengers

    def __str__(self):
        return f"FirstClassCar: {self.serial},{self.capacity}"


class FreightCar(Car):
    def __init__(self, serial):
        self.goods = []
        super().__init__(serial, 0)

    def load(self, good):
        self.capacity += 1
        self.goods.append(good)

    def __str__(self):
        return f"FreightCar: {self.serial},{self.capacity},{self.goods}"