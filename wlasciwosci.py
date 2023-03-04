class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value


point = Point(12, 5)
print(point.get_x())
print(point.get_y())
point.__x = 23 # !!!! Tu tworzę nwoy atrybut który przesłania  ten z init-a
# print(point.__x)
# point.set_x(42)
print(point.get_x())