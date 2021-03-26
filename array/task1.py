n = int(input())
a = []
for i in range(n):
    t = int(input())
    a.append(t)
    # print(a)
# print(a)
for i in a:
    if i % 2 != 0:
        print(i, end=" ")