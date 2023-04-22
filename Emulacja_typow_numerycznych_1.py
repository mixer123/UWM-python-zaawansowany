class X:
    def __init__(self, num):
        self.num = num


class Y:
    def __init__(self, num):
        self.num = num

    def __radd__(self, other_obj):
        return Y(self.num + other_obj.num)

    def __add__(self, other_obj):
        return Y(self.num + other_obj.num)

    def __str__(self):
        return str(self.num)


x = X(2)
y = Y(3)
print(x + y)
print(y + x)