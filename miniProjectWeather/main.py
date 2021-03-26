import requests, json

inp = input()
citylist = inp.split()

KEY = '186a2ae6b4e4a7465105495e3430df15'
URL = 'https://api.openweathermap.org/data/2.5/weather'

for i in citylist:
    parameters = {
        'q': i,
        'appid': KEY,
        'units': 'metric'
    }
    data = requests.get(URL, params=parameters)
    print(data.json())
    res = {
        "city": i,
        "temp": data.json()["main"]["temp"]
    }
    f = open('data.json', 'a')
    f.write(json.dumps(res))
    # f.write(",")
    # print(data.json()['main'])
