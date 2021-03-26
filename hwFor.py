# 1
# n = int(input())
# cnt0 = 0
# cnt1 = 0
# cntMinus = 0
# for i in range(n):
#     num = int(input())
#     if num == 0:
#         cnt0 += 1
#     elif num > 0:
#         cnt1 += 1
#     else:
#         cntMinus += 1
#
# print(cnt0, cnt1, cntMinus)

# 2
# n = int(input())
# ans = False
# for i in range(n):
#     num = int(input())
#     if num == 0:
#         ans = True
# if ans == True:
#     print("YES")
# else:
#     print("NO")

# # 3
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# for x in range(1000):
#     if (a * x**3) + (b * x**2) + (c * x) + d == 0:
#         print(x, end=' ')
#         # 1 * 8 + (-5)*4 + 12 + 0 = 0



# 4
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for x in range(1000, 0, -1):
    if (a * x**3) + (b * x**2) + (c * x) + d == 0:
        print(x, end=' ')
        # 1 * 8 + (-5)*4 + 12 + 0 = 0