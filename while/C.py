n = int(input())

cnt = 0

while 2**cnt <= n:
    print(2**cnt, end=" ")
    cnt += 1

