def minFunction(arr):
    mn = 1111111111
    for i in arr:
        if i < mn:
            mn = i
    return mn

list1 = [1, 2, 3, 4, 5]
a = minFunction(list1)
print(a)