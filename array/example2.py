n = input()
arr = n.split()
arr2 = []
for i in arr:
    arr2.append(int(i))
for i in arr2:
    if arr2[i] > arr2[i-1]:
        print(arr2[i])

for i in range(len(arr)):
    if int(arr[i]) > int(arr[i-1]):
        print(arr[i])


# arr = list(n)
# print(arr2)

# "1 2 3 4 5"