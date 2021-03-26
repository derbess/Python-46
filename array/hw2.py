n = input()
arr = n.split()
arr2 = []
for i in arr:
    arr2.append(int(i))

mn = 1001

for i in arr2:
    if i > 0 and mn > i:
        mn = i

print(mn)
