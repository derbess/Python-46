n = int(input())
cnt = 0
for i in range(n):
    num = int(input("число: "))
    if num % 2 == 0:
        cnt = cnt + 1

print(cnt)