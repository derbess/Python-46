from tkinter import *

def signUp(users):
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
        else:
            print("all fields are required!!!")
            msg = "all fields are required!!!"
            color = "RED"
        err_field.configure(text = msg, bg = color)
        print(users.get_all_user())

    window = Tk()
    window.geometry("500x500")
    lblname = Label(window, text="name: ")
    lblname.grid(row="0", column="0")
    inpname = Entry(window)
    inpname.grid(row="0", column="1")

    lblusername = Label(window, text="username: ")
    lblusername.grid(row="1", column="0")
    inpusername = Entry(window)
    inpusername.grid(row="1", column="1")

    lbllastname = Label(window, text="lastname: ")
    lbllastname.grid(row="2", column="0")
    inplastname = Entry(window)
    inplastname.grid(row="2", column="1")

    lblemail = Label(window, text="email: ")
    lblemail.grid(row="3", column="0")
    inpemail = Entry(window)
    inpemail.grid(row="3", column="1")

    lblmobile = Label(window, text="mobile: ")
    lblmobile.grid(row="4", column="0")
    inpmobile = Entry(window)
    inpmobile.grid(row="4", column="1")

    lblpassword = Label(window, text="password: ")
    lblpassword.grid(row="5", column="0")
    inppassword = Entry(window)
    inppassword.grid(row="5", column="1")

    lblbalance = Label(window, text="balance: ")
    lblbalance.grid(row="6", column="0")
    inpbalance = Entry(window)
    inpbalance.grid(row="6", column="1")

    lbladdress = Label(window, text="address: ")
    lbladdress.grid(row="7", column="0")
    inpaddress = Entry(window)
    inpaddress.grid(row="7", column="1")

    lblisadmin = Label(window, text="isadmin: ")
    lblisadmin.grid(row="8", column="0")
    inpisadmin = Entry(window)
    inpisadmin.grid(row="8", column="1")

    lblid = Label(window, text="id: ")
    lblid.grid(row="9", column="0")
    inpid = Entry(window)
    inpid.grid(row="9", column="1")

    btnreg = Button(window, text="Sign Up", command=registration, bg="YELLOW")
    btnreg.grid(row="10", column="0")

    err_field = Label(window, text="")
    err_field.grid(row="10", column = "1")

    window.mainloop()

def logIn(users):

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
                else:
                    msg = "Invalid password or email"
            else:
                msg = "Password in required"
        else:
            msg = "Email is required"

        err_label.configure(text = msg, fg = color)



    window = Tk()
    window.geometry("500x500")

    lemail = Label(window, text="email: ")
    lemail.grid(row="0", column="0")
    iemail = Entry(window)
    iemail.grid(row="0", column="1")

    lpassword = Label(window, text="password: ")
    lpassword.grid(row="1", column="0")
    ipassword = Entry(window)
    ipassword.grid(row="1", column="1")

    btn = Button(window, command = login, text="Login")
    btn.grid(row="2", column="2")

    err_label = Label(window, text="")
    err_label.grid(row="2", column="1")
    window.mainloop()

