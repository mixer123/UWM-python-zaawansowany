'''
Ćwiczenie. Stwórz klasę Calculator i dodaj w niej kilka metod (bez __) symulujących operacje arytmetyczne.
Zabezpiecz działanie przed wyrzucaniem błędów.
'''

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dodaj(self):
        try:
            return self.x + self.y
        except TypeError:
            print('Uwaga dodajesz stringi')


c = Calculator(2,'3')
c.dodaj()