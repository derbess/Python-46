n = int(input())
a = []

for i in range(n):
    t = int(input())
    a.append(t)

cnt = 0
for i in a:
    if i > 0:
        cnt += 1

print(cnt)
