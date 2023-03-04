class House:
    """The class that describes houses."""

    area = 100

    def get_price(self):
        return 3000 * self.area


d = House()
print(d.get_price())
d2 = House()
d2.area = 123
print(d2.get_price())

