from database_init import *
from dbtable import *
from SignUpTk import signUp, logIn
from tkinter import *
from OtherTk import productsTk,profileTk


window = Tk()
window.geometry("1200x700")

def openLoginPage():

    logIn(users, window)

def openRegPage():

    signUp(users, window)

lblwelcome = Label(window, text="Welcome to our class project!", font=("San Serif", 25))
lblwelcome.place(x=350, y=20)
lblarbuz = Label(window, text = "Arbuz.kz онлайн супермаркет",font=("San Serif", 25), fg="GREEN")
lblarbuz.place(x=350, y=100)
btnLogin = Button(window, text="Log In", command=openLoginPage, font=("San Serif", 12), width=6, height=1, bg="GREEN", fg="WHITE")
btnLogin.place(x=450, y=350)

btnReg = Button(window, text="Sign Up", command=openRegPage,font=("San Serif", 12), width=6, height=1, bg="GREEN", fg="WHITE")
btnReg.place(x=650, y=350)

window.mainloop()