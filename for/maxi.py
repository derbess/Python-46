n = int(input())

mx = -1
for i in range(n):
    t = int(input())
    if t > mx:
        mx = t
print(mx)
#
# 5
# 1 2 5 4 3
# mx = -1
# 1 > -1
# mx = 1
# 2 > 1
# mx = 2
# 5 > 2
# mx = 5
# 4 > 5
# 3 > 5
#
# mx = 5