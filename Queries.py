def queries():
    print("Welcome to Queries")
    loop = 1
    while loop == 1:
        queries_op = int(input("Choose query:\n "
                               "[1]Search for product\n"
                               "[2]List all Customers\n"
                               "[3]List all Products\n"
                               "[4]List a Customer\n"
                               "[5]Quit"
                               ))
        if queries_op == 1:
            search_product()
        elif queries_op == 2:
            all_customers()
        elif queries_op == 3:
            all_products()
        elif queries_op == 4:
            list_customer()
        elif queries_op == 5:
            loop = 0
            pass
        else:
            print("Wrong input, Try again")
            queries()


def search_product():
    file = open("ProductData.txt", "r")
    product_id = int(input("Enter product id: "))

    s = ' '

    while s:
        s = file.readline()
        li = s.split("~")
        if len(s) > 0:
            if int(li[0]) == product_id:
                print("Product id:", li[0])
                print("Product Name:", li[1])
                print("Product Amount:", li[2])
                print("Product Price:", li[3])


def all_customers():
    file = open("CustomerData.txt", "r")
    s = ' '
    s = file.readlines()

    print(s)
    pass


def all_products():
    file = open("ProductData.txt", "r")
    s = ' '
    s = file.readlines()

    print(s)


def list_customer():
    file = open("CustomerData.txt", "r")
    customer_id = int(input("Enter Customer id: "))

    s = ' '

    while s:
        s = file.readline()
        li = s.split("~")
        if len(s) > 0:
            if int(li[0]) == customer_id:
                print("Customer id:", li[0])
                print("Customer Name:", li[1])
                print("Customer Address:", li[2])
