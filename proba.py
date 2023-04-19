l1 = [1,2,3]
l2 = [1,2,3,4]

l4=list(map(lambda a,b: a+b, l1, l2))
l4.append(l2[-1])
print(l4)
#
# l3 = [i + j for i, j in zip(l1, l2)]
# # if len(l1)==len(l2):
# #     l3=l3
# # elif len(l2) > len(l1):
# #     l3.append(l2[-1])
# # elif len(l1) > len(l2):
# #     l3.append(l1[-1])
#
# print('l3',l3)
# # x = (1,2)
# # print(tuple(x))
# l5 = [None] * 4
# print('l5',l5)
# l4=list(map(lambda a,b: a+b, l1, l2))
# print(type(l4))
# l5.append(4)
# print('l4',l4)
# print('l5',l5)
# print(type(l5))
# print(type(l2[-1]))