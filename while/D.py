n = int(input())
cnt = 0
ans = False
while 2**cnt <= n:
    if 2**cnt == n:
        ans = True
        break
    cnt += 1
if ans == True:
    print("YES")
else: print("NO")