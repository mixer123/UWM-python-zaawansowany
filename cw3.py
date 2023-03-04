# Ćwiczenie. Napisz klasę Rectangle z dwoma polami width oraz height.
# Dodaj w tej klasie dwie metody: jedna zwraca pole a druga zwraca obwód prostokąta.
# Następnie dodaj metodę wyświetlającą informację o obiekcie
# np. Szerokość: 20, Wysokość: 30, Pole: 600, Obwód: 100.

class Rectangle:
    width = 20
    heigth = 30

    def square(self):
        return f'Obliczam pole {self.width * self.heigth}'

    def length(self):
        return 2 * self.width + self.heigth

    def show_width(self):
        return self.width

    def show_square(self):
        print('Pokazuje pole',  self.square())

rect = Rectangle()
print(rect.square())
rect.show_square()