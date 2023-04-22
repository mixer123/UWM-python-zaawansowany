# Napisz funkcję lambda, która zwraca kwadrat liczby całkowitej.
x= lambda x: x ** 2
print(x(3))

#Napisz funkcję lambda, która zwraca sumę dwóch liczb całkowitych
sum_ = lambda x,y : x + y
print(sum_(2,3))

#Napisz funkcję lambda, która zwraca iloczyn dwóch liczb rzeczywistych
result_ = lambda x,y : x * y
print(result_(2,3))

#Napisz funkcję lambda, która zwraca największą z trzech liczb całkowitych.
more_ = lambda x,y,z : max(x, y,z)
print(more_(1,2,-3))

#Napisz funkcję lambda, która sprawdza, czy podana liczba jest parzysta.
odd_ = lambda x: x % 2 == 0
print(odd_(5))

#Napisz funkcję lambda, która sprawdza, czy podana liczba jest podzielna przez 3.
by_3_ = lambda x: x % 3 == 0
print(by_3_(6))

# Napisz funkcję lambda, która zwraca długość podanego ciągu znaków.
length_ = lambda x : len(x)
print(length_('text'))

#Napisz funkcję lambda, która zwraca pierwszą literę podanego ciągu znaków.
first_char = lambda x : x[0]
print(first_char('text'))

#Napisz funkcję lambda, która zamienia małe litery na duże i duże na małe w podanym ciągu znaków.

