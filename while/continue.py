cnt = 0
while cnt < 100:
    cnt += 1
    if cnt % 2 == 0:
        continue
    print(cnt, end="")
    print("-", end="")
