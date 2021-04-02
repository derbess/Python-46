from tkinter import *

def productsTk(product):

    basket = [0]
    def draw_products(x,y, productTuple):

        def add():
            basket.append(productTuple)
            basket[0] += productTuple[2]
            print(basket)
            ltp2.configure(text=str(basket[0]))




        name = productTuple[1]
        price = productTuple[2]
        cnt = productTuple[3]
        category_id = productTuple[4]

        lname = Label(window, text = name, font=("San Serif", 16))
        lname.place(x=x+150, y=y+20)

        lprice = Label(window, text=str(price),font=("San Serif", 16))
        lprice.place(x=x+500, y = y+20)

        lcnt = Label(window, text=str(cnt), font=("San Serif", 16))
        lcnt.place(x=x + 700, y=y + 20)

        btn = Button(window, text="add",font=("San Serif", 12), width=3, height=1, bg="GREEN", fg="WHITE", command=add)
        btn.place(x=x + 900, y=y+15)

        line = Canvas(window, width=1000, height=2, bg="BLUE")
        line.place(x=x, y = y+50)


    products = product.get_all_products()
    baseX = 50
    baseY = 40

    window = Tk()
    window.geometry("1200x700")
    title = Label(window, text="PRODUCTS", font=("San Serif",18))
    title.place(x=500, y=10)
    thname = Label(window, text="Product name",font=("San Serif",18), fg = "ORANGE")
    thname.place(x = baseX + 100, y = baseY+20 )

    thprice = Label(window, text="price", font=("San Serif", 18), fg="ORANGE")
    thprice.place(x=baseX + 500, y=baseY + 20)

    thcnt = Label(window, text="quantity", font=("San Serif", 18), fg="ORANGE")
    thcnt.place(x=baseX + 700, y=baseY + 20)


    baseY+=40
    for productItem in products:
        draw_products(baseX, baseY, productItem)
        baseY += 60

    ltp = Label(window, text="Total Price: ",font=("San Serif",18))
    ltp.place(x=baseX+ 750,y=baseY+20 )

    ltp2 = Label(window, text="0",font=("San Serif",18))
    ltp2.place(x=baseX+ 900,y=baseY+20 )

    window.mainloop()


def profileTk(user):
    id = str(user[0])
    username = user[1]
    name = user[2]
    lastname = user[3]
    email = user[4]
    phone = user[5]
    password = user[6]
    balance = str(user[7])
    address = user[8]
    isadmin = str(user[9])
    window = Tk()
    window.geometry("500x500")

    title = Label(window, text="Profile", font=("San Serif", 18))
    title.place(x=150, y=10)
    lblname = Label(window, text="name: ", font=("San Serif", 14))
    lblname.place(x=80, y=50)
    inpname = Label(window,text=name, font=("San Serif", 14))
    inpname.place(x=180, y=50)

    lblusername = Label(window, text="username: ", font=("San Serif", 14))
    lblusername.place(x=80, y=80)
    inpusername = Label(window, text=username,font=("San Serif", 14))
    inpusername.place(x=180, y=80)
    lbllastname = Label(window, text="lastname: ", font=("San Serif", 14))
    lbllastname.place(x=80, y=110)
    inplastname = Label(window,text=lastname, font=("San Serif", 14))
    inplastname.place(x=180, y=110)
    lblemail = Label(window, text="email: ", font=("San Serif", 14))
    lblemail.place(x=80, y=140)
    inpemail = Label(window,text=email, font=("San Serif", 14))
    inpemail.place(x=180, y=140)
    lblmobile = Label(window, text="mobile: ", font=("San Serif", 14))
    lblmobile.place(x=80, y=170)
    inpmobile = Label(window,text=phone, font=("San Serif", 14))
    inpmobile.place(x=180, y=170)
    lblpassword = Label(window, text="password: ", font=("San Serif", 14))
    lblpassword.place(x=80, y=210)
    inppassword = Label(window,text=password, font=("San Serif", 14))
    inppassword.place(x=180, y=210)
    lblbalance = Label(window, text="balance: ", font=("San Serif", 14))
    lblbalance.place(x=80, y=240)
    inpbalance = Label(window,text=balance, font=("San Serif", 14))
    inpbalance.place(x=180, y=240)
    lbladdress = Label(window, text="address: ", font=("San Serif", 14))
    lbladdress.place(x=80, y=270)
    inpaddress = Label(window,text=address, font=("San Serif", 14))
    inpaddress.place(x=180, y=270)
    lblisadmin = Label(window, text="isadmin: ", font=("San Serif", 14))
    lblisadmin.place(x=80, y=300)
    inpisadmin = Label(window,text=isadmin, font=("San Serif", 14))
    inpisadmin.place(x=180, y=300)
    lblid = Label(window, text="id: ", font=("San Serif", 14))
    lblid.place(x=80, y=330)
    inpid = Label(window,text=id, font=("San Serif", 14))
    inpid.place(x=180, y=330)

    window.mainloop()
