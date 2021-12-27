count = 0
users = ["Dan", "rufus", "steve"]
pins = [8800, 9922, 1549]
balances = [200000, 150000, 250000]
balance = 0


def showBalance():
    if pin == pins[0]:
        print("Balance is ", balances[0])
    if pin == pins[1]:
        print("Balance is ", balances[1])
    if pin == pins[2]:
        print("Balance is ", balances[2])
    proceed = int(input("Enter your option(1-continue,2-exit): "))
    if proceed == 1:
        menu()
    else:
        close()


def deposit():
    global balance
    amount = int(input("Enter the amount you need to deposit: "))
    if pin == pins[0]:
        balance = balances[0] + amount
        print("your updated balance is:", balance)
    if pin == pins[1]:
        balance = balances[1] + amount
        print("your updated balance is:", balance)
    if pin == pins[2]:
        balance = balances[2] + amount
        print("your updated balance is:", balance)
    proceed = int(input("Enter your option(1-continue,2-exit): "))
    if proceed == 1:
        menu()
    else:
        close()


def withdraw():
    global balance
    amount = int(input("Enter the amount to withdraw: "))
    if pin == pins[0]:
        balance = balances[0] - amount
        print("your updated balance is:", balance)
    if pin == pins[1]:
        balance = balances[1] - amount
        print("your updated balance is:", balance)
    if pin == pins[2]:
        balance = balances[2] - amount
        print("your updated balance is:", balance)
    proceed = int(input("Enter your option(1-continue,2-exit): "))
    if proceed == 1:
        menu()
    else:
        close()


def fastcash():
    global balance
    fastcash = int(input("select your amount: 500 1000 5000 10000 15000 20000: "))
    print("take your cash:", fastcash)
    if pin == pins[0]:
        balance = balances[0] - fastcash
        print("your updated balance is:", balance)
    if pin == pins[1]:
        balance = balances[1] - fastcash
        print("your updated balance is:", balance)
    if pin == pins[2]:
        balance = balances[2] - fastcash
        print("your updated balance is:", balance)
    proceed = int(input("Enter your option(1-continue,2-exit): "))
    if proceed == 1:
        menu()
    else:
        close()


def close():
    print("****************************************************")
    print("                                                    ")
    print("---Thank you for using aryan National bank ATM.---")
    print("                                                    ")
    print("****************************************************")


def menu():
    option = int(input("Enter your option(1-show balance,2-deposit,3-withdraw,4-fastcash 5-exit): "))
    if option == 1:
        showBalance()
    elif option == 2:
        deposit()
    elif option == 3:
        withdraw()
    elif option == 4:
        fastcash()
    elif option == 5:
        close()


try:
    while count != 3:
        pin = int(input("Enter the pin: "))
        print("")


        def digit(pin):
            temp = pin
            count = 0
            while temp != 0:
                count += 1
                temp = temp // 10

            if count == 4:
                return pin
            else:
                print("Pin should be 4 digits only")


        if digit(pin) in pins:
            # sl = "select sno from users where pin = 'pin'"
            if pin == pins[0]:
                print("welcome to Atm", users[0])
                balance = balances[0]
            elif pin == pins[1]:
                print("welcome to Atm", users[1])
                balance = balances[1]
            else:
                print("welcome to Atm ", users[2])
                balance = balances[2]
            menu()
            break
        else:
            print("Incorrect Pin")
            count += 1

except ValueError:
    print("Enter only numbers...")
