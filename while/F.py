x = int(input())
y = int(input())
cnt = 1
while x < y:
    x = x * 1.1
    print(x)
    cnt += 1
print(cnt)