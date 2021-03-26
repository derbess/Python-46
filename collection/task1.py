students = [
    {
        "name": "Alice",
        "age": 19,
        "gpa": 3.5
    },
    {
        "name": "Richard",
        "age": 32,
        "gpa": 2.9
    },
    {
        "name": "Sam",
        "age": 20,
        "gpa": 3.25
    }
]
for i in students:
    if i["name"][0] == 'A':
        print(i["name"])
for i in students:
    if i["gpa"] > 3.0:
        print(i)
sum = 0
for i in students:
    sum += i["gpa"]
    # print(a)
print(sum/len(students))