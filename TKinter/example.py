from tkinter import *
from tkinter.ttk import Combobox
import requests

def getWeather():
    KEY = '186a2ae6b4e4a7465105495e3430df15'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    city = input1.get()
    params = {
        'q': city,
        'appid': KEY,
        'units': 'metric',
    }
    data = requests.get(URL, params=params)
    lblcityvalue.configure(text = city)
    lbltempvalue.configure(text = data.json()["main"]['temp'])
    print(data.json())



window = Tk()
window.geometry('500x500')

input1 = Entry(window)
input1.grid(row="0", column="0")

btn1 = Button(window, text="click", command=getWeather)
btn1.grid(row="0", column="1")

lblcity = Label(window, text="City:")
lblcity.grid(row='1', column='0')

lblcityvalue = Label(window, text="CITY")
lblcityvalue.grid(row='1', column='1')

lbltemp = Label(window, text="Temperature:")
lbltemp.grid(row='2', column='0')

lbltempvalue = Label(window, text="TEMP")
lbltempvalue.grid(row='2', column='1')

window.mainloop()





