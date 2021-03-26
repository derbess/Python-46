n = int(input())
a = []

for i in range(n):
    t = int(input())
    a.append(t)

for i in range(n):
    if a[i] > a[i-1]:
        print(a[i])
