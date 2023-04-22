class Model:

    def __init__(self, dane, wynik, nazwa):
        self.dane = dane
        self.wynik = wynik
        self.nazwa = nazwa

    def __repr__(self):
        return f"{self.nazwa}: dane: {self.dane}, wynik: {self.wynik}."

    def __add__(self, other):
        if isinstance(other, Model):
            nowe_dane = self.dane + other.dane
            nowy_wynik = self.wynik + other.wynik
            nowa_nazwa = self.nazwa + other.nazwa
            return Model(nowe_dane, nowy_wynik, nowa_nazwa)
        if isinstance(other, int):
            nowe_dane = [elem + other for elem in self.dane]
            return Model(nowe_dane, self.wynik, self.nazwa)

    def __radd__(self, other):
        if isinstance(other, int):
            nowy_wynik = self.wynik+other
            return Model(self.dane, nowy_wynik, self.nazwa)


m1 = Model([2, 3, 4, -3, 3.4], 2.5, "model1")
print(m1)
m2 = Model([-22,33], 98, "model2")
print(m2)
m3 = m1 + m2
print(m3)
m4 = m1 + 4
print(m4)
m5 = 3 + m1
print(m5)