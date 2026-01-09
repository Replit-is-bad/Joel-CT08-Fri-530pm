list1 = [37, 39, 41, 29, 9, 25, 43, 21, 3, 42]
# task 1 #
# for i in range(len(list1)):
#     for j in range(len(list1)-1):
#         if list1[j] > list1[j+1]:
#             list1[j], list1[j+1] = list1[j+1], list1[j]
# print(list1)

# task 2 #

for i in range(len(list1)):
    for j in range(len(list1)-1):
        if list1[j] < list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
print(list1)


