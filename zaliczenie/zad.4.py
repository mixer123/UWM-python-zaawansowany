'''
Zadanie 4. Napisz klasę Polynomial, która będzie reprezentować wielomian jednej zmiennej.
Klasa powinna zawierać metody magiczne __add__, __radd__, __getitem__ oraz __setitem__,
 aby umożliwić dodawanie dwóch wielomianów, dodawanie liczby rzeczywistej do wielomianu,
 uzyskiwanie współczynników wielomianu oraz ustawianie wartości współczynników.


'''

class Polynomial:
    def __init__(self, count_factors):
        self.factors_ = count_factors
        ''' factors_ to jest lista wspolczynnikow wielomianu 
<<<<<<< HEAD
        Uwaga !!
=======
                Uwaga !!
>>>>>>> 5f4460e0d26e5bb2ef28cba5fb88b001d1de4430
        W(x) = a_0 + a_1 x^1 + ... +a_n x^n
        a_0 to pierwszy wspolczynnik listy self.factors_
        '''

    def __setitem__(self, factor_number, value):
        self.factors_[factor_number] = value

    def __getitem__(self, factor_number):
        return self.factors_[factor_number]

    def __repr__(self):
        return f'{self.factors_}'



    def __add__(self, other):
        if isinstance(other, Polynomial):
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
        if type(other) in (int, float):
                return Polynomial([a + other for a in self.factors_])
        return NotImplemented

    def __radd__(self, other):
        if type(other) in (int, float):
            return Polynomial([a + other for a in self.factors_])
        return NotImplemented








p1 = Polynomial([1,2,3,4,5,6])
<<<<<<< HEAD
p2 = Polynomial([1,2,3,4,5,6])
=======
p2 = Polynomial([3,4,5,4,5])
# Setery Setery Setery Setery
>>>>>>> 5f4460e0d26e5bb2ef28cba5fb88b001d1de4430
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
print('Getery')
print(p1[0], p2[0])
print(p1)
print(p2)
print('Dodawanie wektorów')
p3= p1+p2
print(p3)

<<<<<<< HEAD
print('Dodawanie liczby do wektora')
print('p1',p1)
p11 = 2 +p1
print('p11',p11)
=======
print(f'Dodawanie wektora do liczby: {p1} + 2')
p11 = p1 + 2
print(p11)
print(f'Dodawanie liczby do wektora: 3+ {p1}')
p12 = 3+ p1
print(p12)
>>>>>>> 5f4460e0d26e5bb2ef28cba5fb88b001d1de4430


