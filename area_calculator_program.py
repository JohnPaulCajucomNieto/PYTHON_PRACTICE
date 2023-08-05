print("AREA CALCULATOR PROGRAM")
print("1] SQUARE")
print("2] RECTANGLE")
print("3] EXIT")
print("CHOOSE[1/2/3]")
shape = input("CHOOSE ONE IN MENU: ")


if shape == "1":
    side= float(input("ENTER THE SIDE: "))
    area_square = side * side
    print("ARE OF SQUARE: ", area_square)

elif shape == "2":
    length = float(input("ENTER THE LENGTH:"))
    width = float(input("ENTER THE WIDTH:"))
    area_rectangle = length * width
    print("AREA OF RECTANGLE IS:",area_rectangle)
else:
    print("THANK YOU FOR USING MY CALCULATOR PROGRAM")