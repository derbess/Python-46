# a = True
#
# if a == True:
#     print("TRUE")
# if a == False:
#     print("FALSE")


# b = int(input())
# if b == 5:
#     print("FIVE")
# if b > 5:
#     print("Больше чем 5")
# if b < 5:
#     print("Less than Five")

# num1 = int(input())
# num2 = int(input())
#
# if num1 > num2:
#     print(num1)
# elif num1 < num2:
#     print(num2)
# else:
#     print(num2)

# a = int(input())
# if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
#     print("YES")
# else:
#     print("NO")

# b = int(input())
# if b > 0:
#     print(1)
# elif b < 0:
#     print(-1)
# else:
#     print(0)
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = 0
# if a > b:
#     d = a
# else:
#     d = b
# if d > c:
#     print(d)
# else:
#     print(c)





# if a >= b and a >= c:
#     print(a)
# elif b >= c and b >= a:
#     print(b)
# elif c >= a and c >= b:
#     print(c)
# else:
#     print(a)


x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())


# if x1 == x2 or y1 == y2:
#     print("YES")
# else:
#     print("NO")

d1 = x1 - x2 #разница по X
d2 = y1 - y2 #зарница по Y
if d1 < 0:
    d1 = d1 * -1  #Модуль
if d2 < 0:
    d2 = d2 * -1  #Модуль
if d1 == d2 or x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")






