print("-----------------------------------")
print("COMPUTING EVENT RESERVATION BILL...")
print("-----------------------------------")
# ASK THE USER TO ENTER THE NUMBER OF DAYS
days = float(input("ENTER THE NUMBER OF DAYS\n:"))

#THE GIVEN OF THIS PROGRAM THE VARIABLE AND VALUE
#GIVEN OF PER DAY
rate_per_day = 15000
#GIVEN OF SS FEE
sound_system_fee = 4500
#GIVEN OF SD FEE
stage_decor_fee = 3000
#GIVEN OF CATERING FEE
catering_fee = 35000
#GIVEN OF EVAT
evat = .12

#FORMULA OF THIS PROGRAM
amount = rate_per_day * days
#COMPUTATION OF TOTAL
total = amount + sound_system_fee + stage_decor_fee + catering_fee
#COMPUTATION OF TAX
tax = total * evat
#COMPUTATION OF BILL
bill = total + tax

#THE COMPUTATION OF BILL AND THE & OUTPUT
print("-----------------------------------")
print("BILL\n:",bill )
print("-----------------------------------")
