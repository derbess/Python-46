a = [["apple", "orange", "banana"], ["cherry", "pineapple"]]

for i in a:
    for j in i:
        for k in j:
            print(k, end=" ")
    print()
