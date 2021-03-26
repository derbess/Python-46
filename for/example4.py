n = int(input())

cnt = 0
for i in range(n):
    t = int(input())
    if t % 10 == 7:
        cnt += 1
print(cnt)
