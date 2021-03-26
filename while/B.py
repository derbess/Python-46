n = int(input())

cnt = 2
while n % cnt != 0:
    cnt += 1
print(cnt)
# 25 % 2 != 0   True
# 25 % 3 != 0   True
# 25 % 4 != 0   True
# 25 % 5 == 0  False
