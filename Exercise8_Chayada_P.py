usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "admin" and passwordInput == "123" :
    print("Done!")
    print("----Welcome To iShope----")
    print("Please select product")
    print("1.apple 30THB")
    print("2.banana 8THB")
    print("3.water 10THB")
    print("-------------------------")

    select = int(input("Select product :"))
    quantity = int(input("Quantity :"))
    vat = 100*7/100
    if select == 1:
        print("Total",30*quantity+vat,"THB")
    elif select == 2:
        print("Total", 8 * quantity + vat, "THB")
    elif select == 3:
        print("Total", 10 * quantity + vat, "THB")
    print("(vat included)")
    print("-------Thank You-------")
elif usernameInput >= "admin" and passwordInput >= "123":
    print("Incorrect Username or Password!")
    print("please try again!")