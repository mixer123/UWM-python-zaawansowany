'''
Zadanie 2. Stwórz klasę Movie z polami przechowującymi tytuł, rok oraz ocenę filmu.
Dodaj w klasie konstruktor (metodę __init__) ustawiającą wszystkie pola tej klasy.

Następnie stwórz listę zawierającą co najmniej 10 obiektów tego typu.
Posortuj listę wg różnych klucz na co najmniej 5 różnych sposobów.
 W komentarzach umieść informację o zasadach sortowania.
'''
class Movie:
    def __init__(self, title, year, mark):
        self.title = title
        self.year = year
        self.mark = mark

    def __repr__(self):
        return f'{self.title}-{self.year}-{self.mark}'

film1 = Movie('Potop', 1976, 5)
film2 = Movie('Lalka', 1977, 4)
film3 = Movie('Pan Tadeusz', 1976, 3)
film4 = Movie('Wesele', 1978, 44)
film5 = Movie('Ogniem i mieczem', 1980, 55)
film6 = Movie('Noce i dnie', 1981, 56)
film7 = Movie('Krzyżacy', 1977, 66)
film8 = Movie('Nikodem', 1976, 33)
film9 = Movie('Historia Polski', 1976, 22)
film10 = Movie('Pieprz i wanilia', 1976, 11)
list_obj = [film1, film2, film3, film4, film5, film6, film7, film8, film9, film1]

# Sortowanie wg tytułu
def title(obj):
    return obj.title
listobj = sorted(list_obj, key=title)
print(listobj)

# Sortowanie wg roku
def year(obj):
    return obj.year
listobj = sorted(list_obj, key=year)
print(listobj)


# Sortowanie wg oceny
def mark(obj):
    return obj.mark
listobj = sorted(list_obj, key=mark)
print(listobj)


# Sortowanie wg oceny i tytułu
def mark_title(obj):
    return obj.mark, obj.title
listobj = sorted(list_obj, key=mark_title)
print(listobj)
# Sortowanie wg tytułu i oceny
listobj = sorted(list_obj, key = lambda x: (x.title, x.mark))
print(listobj)