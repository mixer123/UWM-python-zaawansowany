# l1 = [1,2,3]
# l2 = [1,2,3,4]
#
# l4=list(map(lambda a,b: a+b, l1, l2))
# l4.append(l2[-1])
# print(l4)
# #
# # l3 = [i + j for i, j in zip(l1, l2)]
# # # if len(l1)==len(l2):
# # #     l3=l3
# # # elif len(l2) > len(l1):
# # #     l3.append(l2[-1])
# # # elif len(l1) > len(l2):
# # #     l3.append(l1[-1])
# #
# # print('l3',l3)
# # # x = (1,2)
# # # print(tuple(x))
# # l5 = [None] * 4
# # print('l5',l5)
# # l4=list(map(lambda a,b: a+b, l1, l2))
# # print(type(l4))
# # l5.append(4)
# # print('l4',l4)
# # print('l5',l5)
# # print(type(l5))
# # print(type(l2[-1]))

class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        if isinstance(other, Vector):
            # Vector-vector addition
            return Vector([a + b for a, b in zip(self.values, other.values)])
        if type(other) in (int, float):
            # Vector-scalar addition
            return Vector([a + other for a in self.values])
        return NotImplemented

    def __radd__(self, other):
        if type(other) in (int, float):
            return Vector([a + other for a in self.values])
        return NotImplemented


v1 = Vector([1, 2, 3])
v2 = v1 + 2  # Creates the vector [3, 4, 5]
v1 = Vector([1, 2, 3])
v2 = 2 + v1  # Raises an error
print(v2.values)