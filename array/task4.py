n = input()
arr = n.split()

arr2 = []

for i in arr:
    arr2.append(int(i))

mx = arr2[0]
index = 0

for i in range(len(arr2)):
    if mx < arr2[i]:
        mx = arr2[i]
        index = i
print(mx, index)