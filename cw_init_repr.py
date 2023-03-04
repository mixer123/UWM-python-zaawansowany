# Ćwiczenia: Stwórz klasę Book z polami title, author, publisher, year.
# Dodaj w klasie inicjalizator oraz metodę zwracającą napis z reprezentacją obiektu.
# Stwórz listę 4 obiektów w typie Book
# a następnie wyświetl zawartość listy używając samej funkcji print.


class Book:
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

books = [Book('tytul1', 'autor1', 'publisher1', 1991),
         Book('tytul2', 'autor2', 'publisher2', 1992),
         Book('tytul3', 'autor3', 'publisher3', 1993),
         Book('tytul4', 'autor4', 'publisher4', 1994)]
print(books)

# Ćwiczenie. Stwórz klasę Godzina i Data w której dodasz metodę __str__
# opisującą obiekty w wybranym formacie.

class Godzina:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
    def __str__(self):
        return f'{self.hour:02}:{self.minute}'
godzina = Godzina('12', '23')
print(godzina)