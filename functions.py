def minFunction(arr):
    mn = 1111111111
    for i in arr:
        if i < mn:
            mn = i
    print(mn)


list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 6]
list3 = [5, 9, 11, -1]
minFunction(list1)
minFunction(list2)
minFunction(list3)