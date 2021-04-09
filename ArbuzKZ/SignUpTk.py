from tkinter import *
from database_init import product, category, users
import tkinter.font as tkFont
from OtherTk import productsTk

def signUp(users, screen):

    window = Frame(screen, width=1200, height=1000)
    window.place(x=0, y=0)
    def registration():
        id = int(inpid.get())
        name = inpname.get()
        lastname = inplastname.get()
        username = inpusername.get()
        mobile = inpmobile.get()
        balance = int(inpbalance.get())
        email = inpemail.get()
        password = inppassword.get()
        address = inpaddress.get()
        isadmin = bool(inpisadmin.get())
        msg = ""
        color = ""
        if id and name and lastname and username and mobile and balance and email and password and address and isadmin:
            users.insert_user(id, username, name, lastname, email, mobile, password, balance, address, isadmin)
            msg = "SUCCESS"
            color = "GREEN"
            productsTk(product, screen)
        else:
            print("all fields are required!!!")
            msg = "all fields are required!!!"
            color = "RED"
        err_field.configure(text = msg, fg = color)
        print(users.get_all_user())



    title = Label(window, text="REGESTRATION", font=("San Serif", 18))
    title.place(x=150, y= 10)
    lblname = Label(window, text="name: ", font=("San Serif", 14))
    lblname.place(x=80, y=50)
    inpname = Entry(window, font=("San Serif", 14))
    inpname.place(x=180, y=50)

    lblusername = Label(window, text="username: ",font=("San Serif", 14))
    lblusername.place(x=80, y= 80)
    inpusername = Entry(window,font=("San Serif", 14))
    inpusername.place(x=180,y=80)
    lbllastname = Label(window, text="lastname: ",font=("San Serif", 14))
    lbllastname.place(x=80, y= 110)
    inplastname = Entry(window,font=("San Serif", 14))
    inplastname.place(x=180,y=110)
    lblemail = Label(window, text="email: ",font=("San Serif", 14))
    lblemail.place(x=80, y=140)
    inpemail = Entry(window,font=("San Serif", 14))
    inpemail.place(x=180, y=140)
    lblmobile = Label(window, text="mobile: ",font=("San Serif", 14))
    lblmobile.place(x=80,y=170)
    inpmobile = Entry(window,font=("San Serif", 14))
    inpmobile.place(x=180,y=170)
    lblpassword = Label(window, text="password: ",font=("San Serif", 14))
    lblpassword.place(x=80,y=210)
    inppassword = Entry(window,font=("San Serif", 14))
    inppassword.place(x=180,y=210)
    lblbalance = Label(window, text="balance: ",font=("San Serif", 14))
    lblbalance.place(x=80,y=240)
    inpbalance = Entry(window,font=("San Serif", 14))
    inpbalance.place(x=180,y=240)
    lbladdress = Label(window, text="address: ",font=("San Serif", 14))
    lbladdress.place(x=80,y=270)
    inpaddress = Entry(window,font=("San Serif", 14))
    inpaddress.place(x=180,y=270)
    lblisadmin = Label(window, text="isadmin: ",font=("San Serif", 14))
    lblisadmin.place(x=80,y=300)
    inpisadmin = Entry(window,font=("San Serif", 14))
    inpisadmin.place(x=180,y=300)
    lblid = Label(window, text="id: ",font=("San Serif", 14))
    lblid.place(x=80,y=330)
    inpid = Entry(window,font=("San Serif", 14))
    inpid.place(x=180,y=330)
    btnreg = Button(window, text="Sign Up",font=("San Serif", 14), command=registration, bg="YELLOW")
    btnreg.place(x=220,y=370)
    err_field = Label(window, text="",font=("San Serif", 14))
    err_field.place(x=180,y=410)
    window.mainloop()

def logIn(users, screen):

    window = Frame(screen, width=1200, height=700)
    window.place(x=0,y=0)
    def login():
        email = iemail.get()
        password = ipassword.get()
        msg = ""
        color = "RED"
        if email:
            if password:
                data = users.login(email, password)
                if len(data) != 0:
                    print(data)
                    msg = "SUCCESS"
                    color = "GREEN"
                    productsTk(product, screen)
                else:
                    msg = "Invalid password or email"
            else:
                msg = "Password in required"
        else:
            msg = "Email is required"

        err_label.configure(text = msg, fg = color)




    lblTitle = Label(window, text="Авторизация", font=("San Serif", 16))
    lblTitle.place(x=175, y = 0)

    lemail = Label(window, text="email: ", font=("San Serif", 12))
    lemail.place(x=120, y = 30)
    iemail = Entry(window, font="30px")
    iemail.place(x = 200, y = 30)

    lpassword = Label(window, text="password: ", font=("San Serif", 12))
    lpassword.place(x=110, y=65)
    ipassword = Entry(window,font="30px")
    ipassword.place(x=200, y=65)

    btnLogin = Button(window, command = login, text="Login", font=("San Serif", 12), bg="#68c6fc", fg="WHITE")
    btnLogin.place(x = 140, y=100)

    btnSignUp = Button(window, text="Sign Up", font=("San Serif", 12), bg="#52fa7f")
    btnSignUp.place(x=270, y=100)

    err_label = Label(window, text="", font=("San Serif", 12))
    err_label.place(x=180, y = 150 )
    # window.mainloop()

