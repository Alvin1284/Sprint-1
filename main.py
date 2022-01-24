import Customer
import Product
import Purchases


def main():
    pass


def menu():
    print("Welcome to our service!!Choose option")
    print("1. Customer")
    print("2. Product")
    print("3. Purchases")
    print("4. Exit")


menu()

loop = 1
while loop == 1:
    choice = int(input("Select option: "))
    choice = int(choice)
    if choice == 1:
        Customer
        menu()
        pass
    elif choice == 2:
        Product
        menu()
        pass
    elif choice == 3:
        Purchases
        menu()
        pass

    elif choice == 4:
        loop = 0
        menu()

    else:
        print("Please enter 1, 2, 3 or 4")
        menu()
