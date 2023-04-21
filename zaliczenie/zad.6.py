'''
Zadanie 6. Napisz klasę Car, która będzie reprezentować samochód.
Klasa powinna zawierać atrybuty instancyjne make, model, year, mileage oraz price,
 inicjalizator,
 właściwości dla mileage oraz price  (umożliwiające odczyt i zapis z walidacją wartości)
   oraz metody magiczne __str__ i __repr__. Dodatkowo,
   klasa powinna posiadać metody drive
    (aktualizującą przebieg samochodu) oraz calculate_depreciation
     (obliczającą spadek wartości samochodu na podstawie jego przebiegu i wieku).
'''
class MyException(Exception):
    def __init__(self, message):
        self.message = message
class Car:
    def __init__(self,make, model, year, mileage ,price ):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price

    # Właściwość getter
    @property
    def mileage(self):
        return self.mileage

    @mileage.setter
    def mileage(self, value):
        # if value < 0:
        #     raise MyException("Wstaw wartość dodatnią")
        self.mileage = value

# make, model, year, mileage, price,
car1 = Car('toyota', 'corola',1934,2021,123455)