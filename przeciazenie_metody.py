class Number:
    def sum(self, a=None, b=None, c=None):
        s = 0
        if a is not None and b is not None and c is not None:
            s = a + b + c
        elif a is not None and b is not None:
            s = a + b
        else:
            s = a
        return s


x = Number()
print(x.sum(1))
print(x.sum(3, 5))
print(x.sum(1, 2, 3))