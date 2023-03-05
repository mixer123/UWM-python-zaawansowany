# Ćwiczenie 1. Stwórz klasę Book z polami author, title, price.
# Stwórz listę 10 książek i posortuj je po długości tytułu (od najkrótszego do najdłuższego).
class Book:
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price

    def __lt__(self, other):
        return len(self.title) <= len(other.title)

    def __repr__(self):
        return f'{self.title} {self.price} {self.author}'
b1 = Book('Sienkiwicz1', 'Potop1', 1923)
b2 = Book('Sienkiwicz2', 'Potop2', 1923)
b3 = Book('Sienkiwicz3', 'Potop3', 1923)
b4 = Book('Sienkiwicz4', 'Potop4', 1923)
b5 = Book('Sienkiwicz5', 'Potop5', 1923)
b6 = Book('Sienkiwicz6', 'Potop6', 1923)
b7 = Book('Sienkiwicz7', 'Potop7', 1923)
b8 = Book('Sienkiwicz8', 'Potop8', 1923)
b9 = Book('Sienkiwicz9', 'Potop9', 1923)
b10 = Book('Sienkiwicz10', 'Potop10', 1923)

lista = [b3,b2,b1,b4,b5,b6,b7,b8,b9,b10]

print(lista)
lista.sort()
print(lista)