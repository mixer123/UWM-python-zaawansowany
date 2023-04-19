'''
Zadanie 4. Napisz klasę Polynomial, która będzie reprezentować wielomian jednej zmiennej.
Klasa powinna zawierać metody magiczne __add__, __radd__, __getitem__ oraz __setitem__,
 aby umożliwić dodawanie dwóch wielomianów, dodawanie liczby rzeczywistej do wielomianu,
 uzyskiwanie współczynników wielomianu oraz ustawianie wartości współczynników.
'''

class Polynomial:
    def __init__(self, count_factors):
        self.factors_ = [None]  * count_factors
        ''' factors_ to jest lista wspolczynnikow wielomianu count_factors okresla
        ile tych wspolczynnikow jest'''

    def __setitem__(self, factor_number, value):
        self.factors_[factor_number] = value

    def __getitem__(self, factor_number):
        return self.factors_[factor_number]

    def __repr__(self):
        return f'{self.factors_}'

    def __add__(self, other):
        sum_factors = [i + j for i, j in zip(self.factors_, other.factors_)]
        if len(self.factors_) == len(other.factors_):
            return [i + j for i, j in zip(self.factors_, other.factors_)]
        elif len(self.factors_) > len(other.factors_):
            sum_factors = [i + j for i, j in zip(self.factors_, other.factors_)]
            sum_factors.append(self[-1])
            return sum_factors
        elif len(self.factors_) < len(other.factors_):
                sum_factors = [i + j for i, j in zip(self.factors_, other.factors_)]
                sum_factors.append(other[-1])
                return sum_factors




p1 = Polynomial(6)
p2 = Polynomial(5)
p1[0] = 2
p1[1] = 21
p1[2] = 23
p1[3] = 24
p1[4] = 24
p1[5] = 24

p2[0] = 2
p2[1] = 21
p2[2] = 23
p2[3] = 24
p2[4] = 24
print(p1)
print(p2)
p3= p1+p2
print(p3[0])


