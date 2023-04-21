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
# class MyException(Exception):
#     def __init__(self, message):
#         self.message = message

from datetime import datetime
class Car:
    def __init__(self,  make, model, year, mileage,price ):

        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._price = price
        if self._mileage < 0:
            raise ValueError('Błąd wartości')
        if self._price < 0:
            raise ValueError('Błąd wartości')

    def __repr__(self):
        return f'{self._make, self._model, self._year, self._mileage, self._price}'
    # Właściwość getter
    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value < 0:
            raise ValueError('Błąd wartości')
        self._mileage = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Błąd wartości')
        self._price = value

    def drive(self, value):
        if value <0:
            raise ValueError('Błąd wartości')
        self._mileage = value
        return self._mileage

#    Kalkulacja wartości 1 rok = 1% mniej , 10000 km = 1% mniej

    def calculate_depreciation(self):
        current_year = datetime.now().year
        years_depreciation_percents = (current_year - self._year) / 100
        mileage_depreciation_percents = (self._mileage // 10000) / 100
        value_car  = round(self._price * (1- (years_depreciation_percents + mileage_depreciation_percents)))
        return value_car



car1 = Car('toyota', 'corola',2021,2021,123455)
car1.mileage = 20000 #  to dzięki setter
print('Obecny stan wartości auta', car1) # tu wyświetli m.in. pole mileage
try:
 car1.drive(345)
except ValueError:
    print(car1, 'Nie dokonano zmiany')
print('Wartości po zmianach' , car1)
print('Cena auta nowego', car1.price)
print('Spadek wartości czyli aktualna cena ',car1.calculate_depreciation())

# make, model, year, mileage,price