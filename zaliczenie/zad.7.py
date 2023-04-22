'''
Zadanie 7. Napisz klasę Samochod, która będzie mieć następujące atrybuty instancyjne:

    marka - marka samochodu
    model - model samochodu
    rok_produkcji - rok produkcji samochodu
    przebieg - przebieg samochodu

Klasa powinna mieć następujące metody:

    __init__(self, marka, model, rok_produkcji, przebieg) -
    konstruktor, który będzie inicjalizował atrybuty marka, model, rok_produkcji i przebieg
    __str__(self) - metoda magiczna,
    która będzie zwracać reprezentację napisową obiektu klasy Samochod
    __lt__(self, other) - metoda magiczna,
    która będzie porównywać dwa samochody po ich przebiegu. Metoda ma zwracać True,
    jeśli przebieg samochodu self jest mniejszy niż przebieg samochodu other,
    a w przeciwnym wypadku False.

'''

class Car:
    def __init__(self,  marka, model, year, mileage):

        self._marka = marka
        self._model = model
        self._year = year
        self._mileage = mileage

        if self._mileage < 0:
            raise ValueError('Błąd wartości')


    def __repr__(self):
        return f'{self._marka, self._model, self._year, self._mileage}'

    def __lt__(self, other):
        if self._mileage < other._mileage:
            return True
        return False

car1 = Car('toyota', 'corola',2021,202100)
car2 = Car('volvo', 's40',2021,10000)
print('car1 < car2: ',car1 < car2 )
print('car1 > car2 :',car1 > car2 )