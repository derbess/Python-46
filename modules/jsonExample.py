import json
f = open('data.json', 'r') #read
x = f.read()
print(type(x))
# data = json.dumps(x)  #dict -> str
data = json.loads(x)   #str -> dict
data["name"] = "Derbes"

# f3 = open('data3.json', 'x')
f2 = open('data2.json', 'w')
data2 = json.dumps(data)
f2.write(data2)
