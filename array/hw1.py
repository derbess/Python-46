n = input()
arr = n.split()
arr2 = []
for i in arr:
    arr2.append(int(i))

mn = 11111111111
ans = False

for i in arr2:
    if i % 2 == 1 and i <= mn:
        mn = i
        ans = True

if ans == True:
    print(mn)
else:
    print(0)


