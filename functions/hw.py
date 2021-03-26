def calc(a,b,operation):
    ans = 0
    if operation == '+':
        ans = a + b
    elif operation == '-':
        ans = a - b
    elif operation == '*':
        ans = a * b
    elif operation == '/':
        ans = a / b
    else:
        return "Операция не поддерживается"
    return ans

def month_to_season(num):
    if num == 1 or num == 2 or num == 12:
        return "Winter"
    elif num >= 3 and num <= 5:
        return "Spring"
    elif num >= 6 and num <= 8:
        return "Summer"
    else:
        return "Autumn"

print(month_to_season(10))


