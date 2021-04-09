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

btnLogin = Button(window, text="login", command=openLoginPage)
btnLogin.pack()

btnReg = Button(window, text="Sign Up", command=openRegPage)
btnReg.pack()

window.mainloop()