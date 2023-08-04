print("CHOOSE A CONVERSION")
print("1] CELSIUS TO FAHRENHEIT")
print("2] FAHRENHEIT TO CELSIUS")
print("3] EXIT")
print("CHOOSE[1/2/3]")
conversion = input("CHOOSE ONE IN MENU: ")


if conversion == "1":
    celsius= float(input("ENTER THE CELSIUS:"))
    fahrenheit = (celsius/1.+32)
    print("FAHRENHEIT IS: ", fahrenheit)

elif conversion == "2":
    fahrenheit = float(input("ENTER THE FAHRENHEIT:"))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("CELSIUS IS:",celsius)
else:
    print("THANK YOU FOR USING MY CONVERSION PROGRAM")