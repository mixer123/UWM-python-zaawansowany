'''
Zadanie 3. Napisz klasę Vector2D, która będzie reprezentować wektor dwuwymiarowy.
Klasa powinna zawierać metody magiczne __add__ oraz __radd__,
 aby umożliwić dodawanie dwóch wektorów 2D oraz dodawanie krotek (x, y) do wektorów.
'''

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

# To też działa

    # def __add__(self, other):
    #     return other.x + self.x, other.y + self.y

v1 = Vector2D(2,3)
v2 = Vector2D(4,5)
v3 = v2 + v1
v4 = v1 + v2
print(v3)
print(v4)