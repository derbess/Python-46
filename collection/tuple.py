list1 = [1, 2, 3, 4, 5]
list1[1] = 5
print(list1)

tuple1 = (1, 2, "Decode", 2.3, True)
list2 = list(tuple1)
list2[1] = 5
tuple1 = tuple(list2)
# tuple1[1] = 5

print(tuple1)
