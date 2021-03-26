n = int(input())
cnt = 1
while cnt * cnt <= n:
    if cnt * cnt == 16:
        print("sixteen")
    print(cnt*cnt)
    cnt += 1
print("HELLO")

