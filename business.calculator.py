print("BUSINESS CALCULATOR MENU")
print("1] SIMPLE INTEREST")
print("2] COMPOUND INTEREST")
print("3] EXIT")
print("CHOOSE[1/2/3]")
business_calculator = input("CHOOSE ONE IN MENU: ")


if business_calculator == "1":
    principal_amount = int(input("ENTER PRINCIPAL AMOUNT:"))
    interest_rate = float(input("ENTER INTEREST RATE:"))
    time_years = int(input("ENTER TIME:"))
    interest = principal_amount * interest_rate * time_years
    print("INTEREST IS: ", interest)

elif business_calculator == "2":
    principal = int(input("ENTER PRINCIPAL AMOUNT:"))
    rate = float(input("ENTER  RATE:"))
    time_in_years = int(input("ENTER TIME:"))
    compound_interest = principal * pow((1 + (rate/100)),time_in_years)
    print("COMPOUND INTEREST IS: ", compound_interest);

else:
    print("THANK YOU FOR USING MY BUSINESS CALCULATOR PROGRAM")