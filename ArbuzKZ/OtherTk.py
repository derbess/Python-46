from tkinter import *
from database_init import product, category, users
from PIL import Image, ImageTk
import json

def productsTk(product, screen):

    window = Frame(screen, width=1200, height=700)
    window.place(x=0, y=0)
    header = Canvas(window, width=1200, height=100, bg="#a6fc6d")
    header.place(x=0, y=0)

    load = Image.open("logo.png")
    load = load.resize((95, 95))
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render, bg="#a6fc6d")
    img.image = render
    img.place(x=0, y=2)


    products = product.get_all_products()
    baseX = 50
    baseY = 120

    ltp2 = Label(window)

    basket = [0]
    def draw_products(x,y, productTuple):

        def add():
            cnt = productTuple[3]
            id = productTuple[0]
            cnt = cnt - 1
            product.buy_product(id)
            update = product.get_all_products()


            basket[0] += productTuple[2]
            print(basket)
            refresh(50, 120, update)
            ltp2.configure(text=str(basket[0]))
            lcnt.configure(text=str(cnt))
            productData = list(productTuple)
            del productData[3]
            print(productData)
            basket.append(productData)


            dict = {
                "tp": basket[0],
                "products": basket[1::]
            }
            data = json.dumps(dict)
            f = open("storage.json", "w")

            f.write(data)


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

    def openCategories(event):
        categoryTk(category, screen)

    def openBasket(event):
        basketTk(product, screen)

    def refresh(baseX, baseY, productsLocal):
        baseY += 40
        for productItem in productsLocal:
            print(productItem)
            draw_products(baseX, baseY, productItem)
            baseY += 60

        ltp = Label(window, text="Total Price: ", font=("San Serif", 18))
        ltp.place(x=baseX + 750, y=baseY + 20)

        ltp2 = Label(window, text=str(basket[0]), font=("San Serif", 18))
        ltp2.place(x=baseX + 900, y=baseY + 20)

    refresh(baseX, baseY, products)

    title = Label(window, text="PRODUCTS", font=("San Serif",18,'underline'), fg="#000000",bg="#a6fc6d")
    title.place(x=300, y=40)

    titleCategory = Label(window, text="CATEGORIES", font=("San Serif",18), bg="#a6fc6d" )
    titleCategory.place(x=550, y=40)
    titleCategory.bind("<Button-1>", openCategories)

    titleBasket = Label(window, text="BASKET", font=("San Serif", 18), bg="#a6fc6d")
    titleBasket.place(x=800, y=40)
    titleBasket.bind("<Button-1>", openBasket)

    thname = Label(window, text="Product name",font=("San Serif",18), fg = "ORANGE")
    thname.place(x = baseX + 100, y = baseY+20 )

    thprice = Label(window, text="price", font=("San Serif", 18), fg="ORANGE")
    thprice.place(x=baseX + 500, y=baseY + 20)

    thcnt = Label(window, text="quantity", font=("San Serif", 18), fg="ORANGE")
    thcnt.place(x=baseX + 700, y=baseY + 20)



    # window.mainloop()

def categoryTk(category, screen):
    window = Frame(screen, width=1200, height=700)
    window.place(x=0, y=0)
    header = Canvas(window, width=1200, height=100, bg="#a6fc6d")
    header.place(x=0, y=0)

    load = Image.open("logo.png")
    load = load.resize((95, 95))
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render, bg="#a6fc6d")
    img.image = render
    img.place(x=0, y=2)

    def draw_categories(x,y, categoryTuple):

        name = categoryTuple[1]
        ci = categoryTuple[0]

        def getProducts():
            productofcategory = product.get_all_products_of_category(ci)
            productsOfCategoryTk(productofcategory, screen)

        lname = Label(window, text = name, font=("San Serif", 16))
        lname.place(x=x+150, y=y+20)

        btn = Button(window, text="products",font=("San Serif", 12), width=10, height=1, bg="GREEN", fg="WHITE", command=getProducts)
        btn.place(x=x + 900, y=y+15)

        line = Canvas(window, width=1000, height=2, bg="BLUE")
        line.place(x=x, y = y+50)

    def openProducts(event):
        productsTk(product, screen)

    def openBasket(event):
        basketTk(product, screen)

    categories = category.get_all_categories()
    baseX = 50
    baseY = 120


    titleProducts = Label(window, text="PRODUCTS", font=("San Serif",18), bg="#a6fc6d")
    titleProducts.place(x=300, y=40)
    titleProducts.bind("<Button-1>", openProducts)

    title = Label(window, text="CATEGORIES", font=("San Serif",18,"underline"), fg = "#000000",bg="#a6fc6d")
    title.place(x=550, y=40)

    titleBasket = Label(window, text="BASKET", font=("San Serif", 18), bg="#a6fc6d")
    titleBasket.place(x=800, y=40)
    titleBasket.bind("<Button-1>", openBasket)

    thname = Label(window, text="Category",font=("San Serif",18), fg = "ORANGE")
    thname.place(x = baseX + 100, y = baseY+20 )

    baseY+=40
    for categoryItem in categories:
        draw_categories(baseX, baseY, categoryItem)
        baseY += 60

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

def productsOfCategoryTk(product, screen):
    window = Frame(screen, width=1200, height=700)
    window.place(x=0, y=0)
    header = Canvas(window, width=1200, height=100, bg="#a6fc6d")
    header.place(x=0, y=0)

    load = Image.open("logo.png")
    load = load.resize((95, 95))
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render, bg="#a6fc6d")
    img.image = render
    img.place(x=0, y=2)
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

    def openCategories(event):
        categoryTk(category, screen)

    products = product
    category_id = products[0][4]
    baseX = 50
    baseY = 120
    currentCategory = category.get_category_by_id(category_id)
    category_name = currentCategory[0][1]


    title = Label(window, text=f"PRODUCTS of {category_name}", font=("San Serif",18, "underline"), bg="#a6fc6d")
    title.place(x=350, y=40)

    titleCategory = Label(window, text="CATEGORIES", font=("San Serif", 18), bg="#a6fc6d")
    titleCategory.place(x=700, y=40)
    titleCategory.bind("<Button-1>", openCategories)


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

def basketTk(product, screen):

    window = Frame(screen, width=1200, height=700)
    window.place(x=0, y=0)
    header = Canvas(window, width=1200, height=100, bg="#a6fc6d")
    header.place(x=0, y=0)

    load = Image.open("logo.png")
    load = load.resize((95, 95))
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render, bg="#a6fc6d")
    img.image = render
    img.place(x=0, y=2)

    f = open("storage.json", "r")
    row = f.read()
    data = json.loads(row)
    productsDict = {}
    for i in data["products"]:
        listkeys = list(productsDict.keys())
        if listkeys.count(i[0]):
            productsDict[i[0]] += 1
        else:
            productsDict[i[0]] = 1
    # print(products)


    tp = data["tp"]
    baseX = 50
    baseY = 120

    ltp2 = Label(window)

    basket = [0]
    def draw_products(x,y, productTuple):

        name = productTuple[1]
        price = productTuple[2]
        cnt = productTuple[3]

        lname = Label(window, text = name, font=("San Serif", 16))
        lname.place(x=x+150, y=y+20)

        lprice = Label(window, text=str(price),font=("San Serif", 16))
        lprice.place(x=x+500, y = y+20)

        lcnt = Label(window, text=str(cnt), font=("San Serif", 16))
        lcnt.place(x=x + 700, y=y + 20)


        line = Canvas(window, width=1000, height=2, bg="BLUE")
        line.place(x=x, y = y+50)

    def openProducts(event):
        productsTk(product, screen)

    def openCategories(event):
        categoryTk(category, screen)

    def refresh(baseX, baseY, productsLocal):
        baseY += 40
        for productItem in productsLocal:

            data1 = list(product.get_product_by_id(productItem))
            data1.append(productsLocal[productItem])

            draw_products(baseX, baseY, data1)
            baseY += 60

        ltp = Label(window, text="Total Price: ", font=("San Serif", 18))
        ltp.place(x=baseX + 750, y=baseY + 20)

        ltp2 = Label(window, text=str(tp), font=("San Serif", 18))
        ltp2.place(x=baseX + 900, y=baseY + 20)

    refresh(baseX, baseY, productsDict)

    title = Label(window, text="PRODUCTS", font=("San Serif",18),bg="#a6fc6d")
    title.place(x=300, y=40)
    title.bind("<Button-1>", openProducts)

    titleCategory = Label(window, text="CATEGORIES", font=("San Serif",18), bg="#a6fc6d" )
    titleCategory.place(x=550, y=40)
    titleCategory.bind("<Button-1>", openCategories)

    titleBasket = Label(window, text = "BASKET", font=("San Serif",18,'underline'), bg="#a6fc6d")
    titleBasket.place(x=800, y=40)

    thname = Label(window, text="Product name",font=("San Serif",18), fg = "ORANGE")
    thname.place(x = baseX + 100, y = baseY+20 )

    thprice = Label(window, text="price", font=("San Serif", 18), fg="ORANGE")
    thprice.place(x=baseX + 500, y=baseY + 20)

    thcnt = Label(window, text="quantity", font=("San Serif", 18), fg="ORANGE")
    thcnt.place(x=baseX + 700, y=baseY + 20)



    # window.mainloop()