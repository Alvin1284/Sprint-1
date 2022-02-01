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
            pass
        elif queries_op == 2:
            pass
        elif queries_op == 3:
            pass
        elif queries_op == 4:
            pass
        elif queries_op == 5:
            loop = 0
            pass
        else:
            print("Wrong input, Try again")
            queries()
