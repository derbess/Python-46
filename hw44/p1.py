while True:
    a = int(input())
    z1 = input()
    b = int(input())
    z2 = input()
    c = int(input())
    res1 = 0
    ans = 0
    if z1 == '+':
        res1 = a + b
    elif z1 == '-':
        res1 = a - b
    elif z1 == '*':
        res1 = a * b
    elif z1 == '/':
        if b == 0:
            print("ERROR, b = 0")
            continue
        res1 = a / b
    else:
        print("ERROR, znak!")

    if z2 == '+':
        ans = res1 + c
    elif z2 == '-':
        ans = res1 - c
    elif z2 == '*':
        ans = res1 * c
    elif z2 == '/':
        if c == 0:
            print("ERROR, c = 0")
            continue
        ans = res1 / c
    else:
        print("ERROR, znak!")

    print("answer = ", ans)


