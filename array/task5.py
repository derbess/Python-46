n = input()
arr = n.split()
arr2 = []
for i in arr:
    arr2.append(int(i))

mx = arr2[0]
indexmx = 0

for i in range(len(arr2)):
    if mx < arr2[i]:
        mx = arr2[i]
        indexmx = i

mn = arr2[0]
indexmn = 0

for i in range(len(arr2)):
    if mn > arr2[i]:
        mn = arr2[i]
        indexmn = i

arr2[indexmx] = mn
arr2[indexmn] = mx
print(arr2)
