users = [
    {
        "login": "alice19",
        "password": "alice19",
        "name": ""
    },
    {
        "login": "richard18",
        "password": "richard18",
        "name": "Richard"
    },
    {
        "login": "sam22",
        "password": "",
        "name": "Sam"
    }
]

for i in users:
    for j in i.values():
        # print(j)
        if j == "":
            users.remove(i)
            break
print(users)

for i in users:
    if i["login"] == "" or i["password"] == 0 or i["name"] == "":
        users.remove(i)
print(users)
