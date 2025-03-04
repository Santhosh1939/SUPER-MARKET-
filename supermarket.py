name = input("Enter your Name:")

lists = '''
Rice         Rs 52/kg
Sugar        Rs 35/kg
Oil          Rs 90/liter
Atta         Rs 25/kg
Chillipowder Rs 40/kg
Biscuts      Rs 12/pack
Cashews      Rs 200/kg
'''


price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []

items = {'rice': 52, 'sugar': 35 , 'oil': 90, 'Atta': 25, 'Chillipowder': 40, 'Biscuts': 12, 'Cashews': 200}

while True:
    option = input("Press 1 for list or 2 to exit: ")
    if option == '2':
        print("Thank you for shopping with us... see you later")
        break
    elif option == '1':
        print(lists)

        while True:
            inp1 = input("To Purchase any item press 1 or press 2 to exit: ")
            if inp1 == '2':
                print("Thank you for shopping with us... see you later")
                break
            elif inp1 == '1':
                item = input("Choose your items: ").lower()
                while True:
                    quantity_input = input("Enter quantity: ")
                    if quantity_input.isdigit():  # Check if input is a digit
                        quantity = int(quantity_input)
                        break
                    else:
                        print("Please enter a valid quantity.")

                if item in items:
                    price = quantity * items[item]
                    pricelist.append((item, quantity, items[item], price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("Selected item is not available. Sorry for the inconvenience.")

        if totalprice > 0:
            tax = (totalprice * 12) / 100
            finalamount = tax + totalprice

            print(25 * "=", "Pythonlife Supermarket", 25 * "=")
            print(28 * " ", "Hyderabad")
            print("Name:", name, 30 * " ")
            print(75 * "-")
            print("sno", 10 * " ", 'items', 8 * " ", 'quantity', 8 * " ", 'price')
            for i in range(len(pricelist)):
                print(i, 13 * " ", ilist[i], 8 * " ", qlist[i], 8 * " ", plist[i])
            print(75 * "-")
            print(50 * " ", 'Total amount:', 'Rs', totalprice)
            print("Tax amount", 50 * " ", 'Rs', tax)
            print(75 * "-")
            print(50 * " ", 'Final amount:', 'Rs', finalamount)
            print(75 * "-")
            print(20 * " ", "Thank you & Visit again")
            print(75 * "-")
