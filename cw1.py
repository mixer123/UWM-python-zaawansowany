#
# 1)Stwórz klasę Movie z polem title. Stwórz dwa obiekty w tym typie.
#


class Movie:
    title = 'tytul'


movie1 = Movie()
print(movie1.title)
movie1 = Movie()


# Stwórz klasę Person, dodaj w niej 5 wybranych przez siebie pól i dwie metody.
# Stwórz dwa obiekty i poćwicz na nich ustawianie pól i wywoływanie metod.
class Person:
    imie = 'jan'

    def show_imie(self):
        return self.imie


person = Person()
print(person.show_imie())
