login_details = {"Name": " ", "Password": " "}
while True:
    print("------------------------------------")
    print("1] LOGIN")
    print("2] SHOW")
    print("3] CLEAR ")
    print("4] EXIT")
    print("------------------------------------")
    choose = input("CHOOSE ONE: [1/2/3/4] ")
    print("----------------------------------------------------")
    if choose == '1':
        name = input("ENTER YOUR NAME: ")
        password = input("ENTER YOUR PASSWORD: ")
        login_details['NAME'] = name
        login_details['PASSWORD'] = password
        print("SUCCESFUL ADD A DETAILS")
    elif choose == '2':
        print(login_details)
    elif choose == '3':
        login_details.clear()
        print("SUCCESFUL CLEAR DETAILS")
    else:
        print("THANK YOU FOR USING MY PROGRAM, HAVE A GOOD DAY!")
        print("----------------------------------------------------")
        break
