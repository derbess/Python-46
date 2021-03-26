import re
s = input().split()

x = re.findall(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-zA-Z]{2,9}", s)

print(x)
