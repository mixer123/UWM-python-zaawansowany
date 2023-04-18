'''
Zadanie 1. Stwórz klasę Time zajmującą się obsługą czasu.
Dodaj w niej dwa pola (zmienna) o nazwie hour i minute do przechowywania godzin i minut.
W klasie dodaj następujące metody:

    funkcja, która zwraca wartość logiczną sprawdzającą czy zawartość pól może być poprawną godziną
    w formacie 24-godzinnym

    funkcja, która odpowiada za dodawanie dwóch obiektów typu Time.
    W środku należy dodać godziny do godzin, minuty do minuty.
    Jeśli minuty są większe lub równe niż 60,
    to należy odpowiednie zwiększyć pole godzin i pomniejszyć o 60 minuty.
    Jeśli godziny są większe lub równe niż 24, to należy od godzin odjąć 24.
    Funkcja ma zwrócić obiekt typu Time przechowujący “sumę”.

    dodaj odpowiednią metodę, która odpowiada za sortowanie obiektów typu Time
    (wg dowolnego wybranego przez siebie klucza)

Następnie stwórz co najmniej 3 obiekty i wywołaj na nich każdą z funkcji co najmniej 1 raz.
'''

class Time:


    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f'{self.hour}:{self.minute}'

# Sprawdzenie czy dobry format
    def check(self):
        if self.hour >= 0 and self.hour < 24 and self.minute >= 0 and self.minute < 60:
            return f'To jest dobry format godziny {self}'
        return f'To NIE jest dobry format godziny {self}'

# Dodawanie obiektów
    def __add__(self, other):
        if self.hour + other.hour >= 24:
            hour = self.hour + other.hour -1
        else:
            hour = self.hour + other.hour

        if self.minute + other.minute >= 60:
            hour +=1
            minute = self.minute + other.minute -60
        else:
            minute = self.minute + other.minute
        return Time(hour, minute)

    # Porównywanie obiektów
    def __lt__(self, other):
        if ((self.hour) < (other.hour)) or ((self.hour) == (other.hour) and (self.minute) < (other.minute)):
            return f'{self} jest wcześniej niż {other}'


    def __gt__(self, other):
        if ((self.hour) > (other.hour)) or ((self.hour) == (other.hour) and (self.minute) > (other.minute)):
            return f'{self} jest póżniej niż {other}'



    def __eq__(self, other):
        return (((self.hour) == (other.hour) and (self.minute) == (other.minute)) )



# Sortowanie obiektów
def count_min(obj):
        return obj.hour * 60 + obj.minute





time1 = Time(4,44)
time2 = Time(4,23)
time3 = time1 + time2
print(time1 > time2)
listobj = sorted([time1, time2, time3], key=count_min)
print(listobj)

print(str(time3.hour) + ':' + str(time3.minute))
print(time1.check())
print(time2.check())
print(time3.check())