#pickupCost = 0
#deliveryCost = 5
#running = True
import re

#global pizzaMenu
#global pizzaPrice
#LISTS
#pizz#           "Cheese",
  #            "Margherita",
 #             "BBQ Meatlovers",
#pizzaPrice = [ 9, 9, 9, 9, 9, 13, 13, 13 ]
#cost = []
#customerOrder = []
#def pick_or_deli():
#delivery = input("P - pick up / D - delivery:")
    #delivery = delivery.upper()
    #if delivery == "D":
      #  whil3global customer_name
            #customer_name = input("Name:")
            #if not re.match("^[a-zA-Z ]*$", customer_name):
             #elif len(customer_name) == 0:
           # whil#global customer_telephone
            #customer_telephone = input("Telephone:")
            #if not re.match("^[0-9 ]*$", customer_telephone):
            # while running == True:
            #house_no = input("House number:")
            #if not re.match("^[0-9 /]*$", house_no):
            # whil#global street_name
            #street_name = input("Street name:")
            #if not re.match("^[a-zA-Z ]*$", street_name):
             #elif len(street_name) == 0:
            # else:
          #       break
        #while running == True:
            #global suburb
            # if not re.match("^[a-zA-Z ]*$", suburb):
             #        break
       # whil#global city
            #city = input("City:")
            #if not re.match("^[a-zA-Z ]*$", city):
            #elif len(city) == 0:
           #        break
       # while running == True:
           # global post_code
          #     elif len(post_code) == 0 or len(post_code) > 4:
      #      else:
     #           break
                #   elif delivery == "P":


#      while running == True:
    #          customer_name = input("Name:")
            #         if not re.match("^[a-zA-Z ]*$", customer_name):
        #             print("Please use letters only")
                #         elif len(customer_name) == 0:
        #             print("Please enter a valid input")
                #         else:
        #              customer_name = customer_name.title()
                #             break
        #        while running == True:
    #         customer_telephone = input("Telephone:")
            #         if not re.match("^[0-9 ]*$", customer_telephone):
        #              print("Please use numbers only")
                #          elif len(customer_telephone) == 0:
        #            print("Please enter a valid input")
                #        else:
        #          break
                #   else:


#    print("Please enter P or D")
        #   pick_or_deli()

#pick_or_deli()

#def print_menu():
 #   print ("""
  #      -----------------------------------------------
   #     |          JP PIZZA ordering APP 2023         |
    #    |                                             |
     #  |            -------------------              |
#      |                1. Pepperoni                 |
#      |                2. Hawaiian                  |
#      |                3. Cheese                    |
#     |                4. Italian                   |
#    |                5. Margherita                |
#   |                                             |
#   |             ₱700 premium pizzas             |
#  |             -------------------             |
#   |               6. Apricot Chicken            |
#    |               7. BBQ Meatlovers             |
#     |               8. Chicken & Cranberry        |
#      """)
#print_menu()
#def order():
 #   global pizza_no
  #       try:
    #         if pizza_no < 1:
          #            break
   #          print("Please use numbers only")
 #order()
#def Choice_of_pizza():
  #  for i in range(1,pizza_no+1):
     #        try:
            #           else:
              #            if delivery == "D":
       #               continue
#Choice_of_pizza()

#def customerDetails():
#    if delivery == "D":
 #       print ("")
#        print ("CUSTOMER and ORDER DETAILS")
        #print ("")
        #print ("Name:", customer_name)
       # print ("Telephone:", customer_telephone)
        #print ("Address:", house_no, street_name)
        #print ("Suburb: ", suburb)
       # print ("City: ", city)
        #else:
       #customerDetails()
#print ("")
#def3 confirm():
    #confirmation = input("Y - confirm order / N - cancel order:")
  #  confirmation = confirmation.upper()
  #  if confirmation == "Y":
   #  elif confirmation == "N":
      #  print("DETAILS CANCELLED - order has been reset")
     #    cost[:] = []
        #       confirm()
#confirm()

#print ("")
#def order_some_more():
 # 3  order_more = input("Z - order more / X - exit program:")
  #  order_more = order_more.upper()
  #  '''cost[:] = []'''
  #  if order_more == "Z":
    #    print_menu()
    #    order()
    #    Choice_of_pizza()
     #   customerDetails()
     #   confirm()
    #    print ("")
      #  print ("THANK YOU FOR YOUR ORDER")
     #   if delivery == "D":
     #       print ("Your order will be delivered in 25mins")
    #    elif delivery == "P":
   #         print ("Your order will be ready to pick up in 20mins")
  #  elif order_more == "X":
 #       print ("")
 #       print ("THANK YOU FOR YOUR ORDER")
#        if delivery == "D":
#            print ("Your order will be delivered in 25mins")
#        elif delivery == "P":
#            print ("Your order will be ready to pick up in 20mins")
   # else:
  #      print ("Please enter X or Z")
 #       order_some_more()

#order_some_more()

pickupCost = 0
deliveryCost = 5
running = True
import re

global pizzaMenu
global pizzaPrice
#LISTS
pizzaMenu = [ "Pepperoni",
              "Hawaiian",
              "Cheese",
              "Italian",
              "Margherita",
              "Apricot Chicken",
              "BBQ Meatlovers",
              "Chicken and Cranberry" ]
pizzaPrice = [ 9, 9, 9, 9, 9, 13, 13, 13 ]
cost = []
customerOrder = []

def pick_or_deli():
    global delivery
    delivery = input("P - pick up / D - delivery:")
    delivery = delivery.upper()
    if delivery == "D":
        while running == True:
            global customer_name
            customer_name = input("Name:")
            if not re.match("^[a-zA-Z ]*$", customer_name):
                print("Please use letters only")
            elif len(customer_name) == 0:
                print("Please enter a valid input")
            else:
                customer_name = customer_name.title()
                break
        while running == True:
            global customer_telephone
            customer_telephone = input("Telephone:")
            if not re.match("^[0-9 ]*$", customer_telephone):
                print("Please use numbers only")
            elif len(customer_telephone) == 0:
                print("Please enter a valid input")
            else:
                break
        while running == True:
            global house_no
            house_no = input("House number:")
            if not re.match("^[0-9 /]*$", house_no):
                print("Please use numbers only")
            elif len(house_no) == 0:
                print("Please enter a valid input")
            else:
                break
        while running == True:
            global street_name
            street_name = input("Street name:")
            if not re.match("^[a-zA-Z ]*$", street_name):
                print("Please use letters only")
            elif len(street_name) == 0:
                print("Please enter a valid input")
            else:
                street_name = street_name.title()
                break
        while running == True:
            global suburb
            suburb = input("Suburb:")
            if not re.match("^[a-zA-Z ]*$", suburb):
                print("Please use letters only")
            elif len(suburb) == 0:
                print("Please enter a valid input")
            else:
                suburb = suburb.title()
                break
        while running == True:
            global city
            city = input("City:")
            if not re.match("^[a-zA-Z ]*$", city):
                print("Please use letters only")
            elif len(city) == 0:
                print("Please enter a valid input")
            else:
                city = city.title()
                break
        while running == True:
            global post_code
            post_code = input("Postcode:")
            if not re.match("^[0-9 /]*$", post_code):
                print("Please use numbers only")
            elif len(post_code) == 0 or len(post_code) > 4:
                print("Please enter a valid input")
            else:
                break
    elif delivery == "P":
        while running == True:
            customer_name = input("Name:")
            if not re.match("^[a-zA-Z ]*$", customer_name):
                print("Please use letters only")
            elif len(customer_name) == 0:
                print("Please enter a valid input")
            else:
                customer_name = customer_name.title()
                break
        while running == True:
            customer_telephone = input("Telephone:")
            if not re.match("^[0-9 ]*$", customer_telephone):
                print("Please use numbers only")
            elif len(customer_telephone) == 0:
                print("Please enter a valid input")
            else:
                break
    else:
        print("Please enter P or D")
        pick_or_deli()

pick_or_deli()

def print_menu():
    print ("""
        -----------------------------------------------
        |          JP PIZZA ordering APP 2023         |
        |                                             |
        |            php 9 classic pizzas             |
        |            -------------------              |
        |                1. Pepperoni                 |
        |                2. Hawaiian                  |
        |                3. Cheese                    |
        |                4. Italian                   |
        |                5. Margherita                |
        |                                             |
        |             ₱700 premium pizzas             |
        |             -------------------             |
        |               6. Apricot Chicken            |
        |               7. BBQ Meatlovers             |
        |               8. Chicken & Cranberry        |
        |                                             | 
        ----------------------------------------------- 
        """)
print_menu()

def order():
    global pizza_no
    while True:
        try:
            pizza_no = int(input("No. of pizzas (min 1 - max 5):"))
            if pizza_no < 1:
                print("Please order between 1 - 5 pizzas")
                continue
            if pizza_no > 5:
                print("Please order between 1 - 5 pizzas")
                continue
            else:
                break
        except ValueError:
            print("Please use numbers only")
            continue
order()

def Choice_of_pizza():
    for i in range(1,pizza_no+1):
        while True:
            try:
                pizza_kind = int(input("Choice of pizza(s):"))
                if pizza_kind < 1:
                    print("Refer to PIZZA MENU for pizza number")
                    continue
                if pizza_kind > 8:
                    print("Refer to PIZZA MENU for pizza number")
                    continue
                else:
                    pizza = pizza_kind - 1
                    cost.append(pizzaPrice[pizza])
                    customerOrder.append(pizzaMenu[pizza])
                    global total_cost
                    total_cost = sum(cost)
                    global grandTotal
                    if delivery == "D":
                        grandTotal = total_cost + deliveryCost
                    else:
                        grandTotal = total_cost
                    break
            except ValueError:
                print("Please use numbers only")
                continue
Choice_of_pizza()

def customerDetails():
    if delivery == "D":
        print ("")
        print ("CUSTOMER and ORDER DETAILS")
        print ("")
        print ("Name:", customer_name)
        print ("Telephone:", customer_telephone)
        print ("Address:", house_no, street_name)
        print ("Suburb: ", suburb)
        print ("City: ", city)
        print ("Postcode: ", post_code)
        print ("ORDER:", customerOrder)
        print ("Total: $", total_cost)
        print ("Total + Delivery: $", grandTotal)
    else:
        print ("")
        print ("CUSTOMER and ORDER DETAILS")
        print ("")
        print ("Name:", customer_name)
        print ("Telephone:", customer_telephone)
        print ("ORDER:", customerOrder)
        print ("Total: $", total_cost)
customerDetails()

print ("")
def confirm():
    confirmation = input("Y - confirm order / N - cancel order:")
    confirmation = confirmation.upper()
    if confirmation == "Y":
        print("DETAILS CONFIRMED")
    elif confirmation == "N":
        print("DETAILS CANCELLED - order has been reset")
        customerOrder[:] = []
        cost[:] = []
        print_menu()
        order()
        Choice_of_pizza()
        customerDetails()
        confirm()
    else:
        print("Please enter Y or N")
        confirm()
confirm()

print ("")
def order_some_more():
    order_more = input("Z - order more / X - exit program:")
    order_more = order_more.upper()
    '''cost[:] = []'''
    if order_more == "Z":
        print_menu()
        order()
        Choice_of_pizza()
        customerDetails()
        confirm()
        print ("")
        print ("THANK YOU FOR YOUR ORDER")
        if delivery == "D":
            print ("Your order will be delivered in 25mins")
        elif delivery == "P":
            print ("Your order will be ready to pick up in 20mins")
    elif order_more == "X":
        print ("")
        print ("THANK YOU FOR YOUR ORDER")
        if delivery == "D":
            print ("Your order will be delivered in 25mins")
        elif delivery == "P":
            print ("Your order will be ready to pick up in 20mins")
    else:
        print ("Please enter X or Z")
        order_some_more()
order_some_more()