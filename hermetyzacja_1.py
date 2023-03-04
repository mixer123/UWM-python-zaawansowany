class Person:
    __name = "Jan"

    def __get_name(self):
        return self.__name


p1 = Person()
print(p1.__get_name())
# print(p1._Person__get_name())