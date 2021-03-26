n = int(input())

cntEven = 0
cntOdd = 0
for i in range(n):
    t = int(input())
    if t % 2 == 0:
        cntEven += 1
    else:
        cntOdd += 1
print(cntEven, cntOdd)
