print("------------------------------------")
#INPUT A PRODUCT TO SEARCH
product = input("ENTER THE PRODUCT TO SEARCH:")
#LIST OF A PRODUCTS
products_list = ["Magnolia Chicken","555 Sardines",
                 "Palmolive Soap","Sunsilk Shampoo",
                 "Tide Ultra","Gillette Blade"]
#EMPTY
empty_list = [" "]

#CONDITIONAL STATEMENTS TO PROCUCT TO EMPTY
if(products_list > empty_list):
    print("MESSAGE: PRODUCT FOUND")
    print("-----------------------------------")
else:
    print("PRODUCT NOT FOUND!")

print("\n------------------------------------")
#INPUT A COURSE TO SEARCH
search = input("ENTER THE COURSE TO SEARCH:")
#CONDITIONAL STATEMENTS
if(products_list < empty_list):
    print("MESSAGE: PRODUCT FOUND")
else:
    print("PRODUCT NOT FOUND!")
    print("-------------------------------------")