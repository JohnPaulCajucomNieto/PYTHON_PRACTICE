#ASK A USER TO ENTER A NUMBER OF DAYS
print("==================================")
days = float(input("NUMBER OF DAYS YOU STAY IN HOTEL:\n"))
print("==================================")
#GIVEN AMENTITIES RATES
#ROOM RATE 250 PER DAY
Room_Rate = 250
#INTERNET RATE 150 PER DAY
Internet_Rate = 150
#AIRCON RATE 350 PER DAY
Aircon_Rate = 350
#REFRIGERETOR 400 PER DAY
Refrigerator_Rate = 400
#POOL RATE 500 PER DAY
Pool_Rate = 500
#AMENTITIES AMOUNT COMPUTATION
Room_Amount = Room_Rate * days
Internet_Amount = Internet_Rate * days
Aircon_Amount = Aircon_Rate * days
Refrigerator_Amount = Refrigerator_Rate * days
Pool_Amount = Pool_Rate * days
#FORMULA
Bill = Room_Amount + Internet_Amount + Aircon_Amount + Refrigerator_Amount + Pool_Amount
#OUTPUT
print("==================================")
print("YOUR TOTAL BILLS:\n", Bill)
print("==================================")
