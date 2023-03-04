class Person:
    __name = "Jan" # to jest pole prywatne


p1 = Person()
# print(p1.__name) # brak dostępu do pola
print(p1._Person__name) #  jest dostęp do pola