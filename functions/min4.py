def min4(a, b, c, d):
    list1 = []
    list1.append(a)
    list1.append(b)
    list1.append(c)
    list1.append(d)
    mn = 111111111
    for i in list1:
        if i < mn:
            mn = i
    return mn


def min4v2(a, b, c, d):
    mnAB = 0
    if a > b:
        mnAB = b
    else:
        mnAB = a
    mnCD = 0
    if c > d:
        mnCD = d
    else:
        mnCD = c
    if mnAB < mnCD:
        return mnAB
    return mnCD

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4v2(a, b, c, d))