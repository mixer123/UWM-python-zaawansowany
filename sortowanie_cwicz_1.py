# Ćwiczenia. Stwórz listę osób, książek, filmów itp i posortują ją różnymi sposobami.

class Book:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __eq__(self, other):
        return ((self.title, self.year) == (other.year, other.title))

    def __ne__(self, other):
        return ((self.year, self.title) != (other.year, other.title))

    def __lt__(self, other):
        return ((self.year, self.title) < (other.year, other.title))

    def __le__(self, other):
        return ((self.year, self.title) <= (other.year, other.title))

    def __gt__(self, other):
        return ((self.year, self.title) > (other.year, other.title))

    def __ge__(self, other):
        return ((self.year, self.title) >= (other.year, other.title))
    def __repr__(self):
        return f'{self.title} {self.year}'
b1 = Book('Potop', 1923)
b2 = Book('Potop', 1967)
b3 = Book("ogniem i mieczem", 1967)

lista = [b3,b2,b1]

print(lista)
lista.sort()
print(lista)