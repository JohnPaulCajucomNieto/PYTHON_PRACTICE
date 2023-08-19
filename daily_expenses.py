daily_expenses = {0}
sum = 0
while True:
    print("------------------------------------")
    print("1.] ADD")
    print("2.] COMPUTE")
    print("3.] DISPLAY")
    print("4.] EXIT")
    print("------------------------------------")
    choose = input("CHOOSE ONE: [1/2/3/4] ")
    print("----------------------------------------------------")
    if choose == '1':
        expense = float(input("ENTER YOUR EXPENSES: "))
        daily_expenses.add(expense)
        print("ADDED SUCCESSFULL")
    elif choose == '2':
        print("COMPUTE SUCCESS")
        for total in daily_expenses:
            sum += total
    elif choose == '3':
        print("TOTAL: ", sum)
    else:
        print("THANK YOU FOR USING MY PROGRAM, HAVE A GOOD DAY!")
        print("----------------------------------------------------")
        break
