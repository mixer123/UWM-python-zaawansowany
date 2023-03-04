class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def _get_radius(self):
        print("Get radius")
        return self.__radius

    def _set_radius(self, value):
        print("Set radius")
        self.__radius = value

    def _del_radius(self):
        print("Delete radius")
        del self.__radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )


circle = Circle(42.0)
print(circle.radius)
circle.radius = 100.0
print(circle.radius)
del circle.radius
# print(circle.radius)
help(circle)