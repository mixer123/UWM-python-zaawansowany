# To tzw. przykład funkcji anonimowej.#
# By uruchomić to też w skrypcie, to potrzebujemy argumentu:

print((lambda x: x + 1)(2))

# Możemy również skorzystać z różnych opcji argumentów jak dla funkcji:

print((lambda x, y, z: x + y + z)(1, 2, 3))
print((lambda x, y, z=3: x + y + z)(1, 2))
print((lambda x, y, z=3: x + y + z)(1, y=2))
print((lambda *args: sum(args))(1,2,3))
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))
print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))