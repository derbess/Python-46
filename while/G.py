x = int(input())
p = int(input())
y = int(input())
cnt = 0
while(x < y):
    x = x + p/100 * x
    cnt+=1
    print(x)
    x = int(x)
print(cnt)