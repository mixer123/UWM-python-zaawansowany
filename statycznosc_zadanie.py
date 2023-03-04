'''
Ćwiczenie Na bazie wcześniej stworzonej klasy Produkt dodaj w niej metodę statyczną check_quality,
 przyjmującą jeden argument – obiektu typu Product.
Metoda ma sprawdzić,
czy jakość jest większa niż 5 – jeśli tak, to zwiększa cenę o 10% W przeciwnym wypadku, nie robi nic.
'''
class Product:
    def __init__(self, name, price, quality, tax):
        self.__name = name
        self.__price = price
        self.__quality = quality
        self.__tax = tax
        if self.__price <0:
            self.__price = 0
        if self.__tax <0:
            self.__tax = 0
        if not isinstance(name, str):
            self.__name = ''

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quality(self):
        return self.__quality

    @property
    def tax(self):
        return self.__tax

    @tax.setter
    def tax(self, value):
        if value < 0:
            value = 0
        self.__tax = value

    @staticmethod
    def check_quality(value):
        if isinstance(value, Product):
            if value.__quality == 'good':
                value.__price *= 1.1



    def __str__(self):
        return f'Product {self.__name}'

p1 = Product('auto', 123, 'good', 23)
print(p1.price)
Product.check_quality(p1)
print(p1.price)
print()