from database_init import *
from dbtable import *
from SignUpTk import signUp, logIn
from tkinter import *
from OtherTk import productsTk, profileTk
from PIL import Image, ImageTk

window = Tk()
window.geometry("1200x700")

def openLoginPage():

    logIn(users, window)

def openRegPage():

    signUp(users, window)
header = Canvas(window, width=1200, height=100, bg="#a6fc6d")
header.place(x=0, y = 0)

title = Label(window, text = "Arbuz.kz", font=("Architects Daughter", 35), bg="#a6fc6d", fg = "#ff3636")
title.place(x=520, y=30)

load = Image.open("logo.png")
load = load.resize((95,95))
render = ImageTk.PhotoImage(load)
img = Label(window, image=render, bg = "#a6fc6d")
img.image = render
img.place(x=0, y=2)

lblwelcome = Label(window, text="Welcome to our class project!", font=("San Serif", 25))
lblwelcome.place(x=350, y=120)

lblarbuz = Label(window, text = "Arbuz.kz онлайн супермаркет",font=("San Serif", 25), fg="GREEN")
lblarbuz.place(x=350, y=200)

btnLogin = Button(window, text="Log In", command=openLoginPage, font=("San Serif", 12), width=6, height=1, bg="GREEN", fg="WHITE")
btnLogin.place(x=450, y=450)

btnReg = Button(window, text="Sign Up", command=openRegPage,font=("San Serif", 12), width=6, height=1, bg="GREEN", fg="WHITE")
btnReg.place(x=650, y=450)

window.mainloop()
# cursor = connection.cursor()
# cursor.execute(f"UPDATE product SET cnt = {100} WHERE cnt < {0}")
# connection.commit()

