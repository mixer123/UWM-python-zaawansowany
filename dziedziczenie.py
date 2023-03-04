# class Person:
#     def __init__(self, fname, lname, pesel):
#         self.firstname = fname
#         self.lastname = lname
#         self.pesel = pesel
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#
# class Student(Person):
#     def __init__(self, fname, lname, pesel,  year):
#         super().__init__(fname, lname, pesel)
#         self.graduationyear = year
#
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, self.pesel, "to the class of", self.graduationyear)
#
#
# s = Student('jan', 'kowalski', 12345, 1966)
# s.welcome()
#################
'''
B. Stwórz inicjalizator z czterema argumentami (zachowaj kolejność i nazwy jak wcześniejszym punkcie). 
Zadbaj również o to aby inicjalizator w razie podania argumentów liczbowych jako ujemne, 
to ustawiał je niezależnie na zero. Nazwa musi być napisem – jeśli nie jest, ustaw napis pusty ('').
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


    def __str__(self):
        return f'Product {self.__name}'

'''D. Zaimplementuj klasę Book dziedziczącą po klasie Product.
 Klasa ta powinna posiadać atrybuty instancyjne prywatne:
    authors jako lista napisów (pol. autorzy).
    title typu str (pol. tytuł)
'''

class Book(Product):
    def __init__(self, name, price, quality, tax, authors, title):
        super().__init__(name, price, quality, tax)
        if len(authors) >0:
            authors = ['Adam Mickiewicz']
        self.__authors = authors
        self.__title = title
        self.__tax = 0




    def __str__(self):
        return f'Book {self.name} {self.price} {self.quality} {self.tax}'

p1 = Product('auto', 123, 'good', 23)
print(p1)
b1 = Book('Ksiazka', 30.23, 'good', 23, ['sienk','mick'], 'Tytuł')
print(b1)
