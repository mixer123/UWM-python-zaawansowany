'''
Zadanie 4. Napisz klasę Polynomial, która będzie reprezentować wielomian jednej zmiennej.
Klasa powinna zawierać metody magiczne __add__, __radd__, __getitem__ oraz __setitem__,
 aby umożliwić dodawanie dwóch wielomianów, dodawanie liczby rzeczywistej do wielomianu,
 uzyskiwanie współczynników wielomianu oraz ustawianie wartości współczynników.
'''

class Polynomial:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'{self.a}-{self.b}'

    def __add__(self, other):
        return f' Suma wielomianów: s({self.a + other.a}, {self.b + other.b})'

p1 = Polynomial(1,2)
p2 = Polynomial(3,4)
print(p1+p2)