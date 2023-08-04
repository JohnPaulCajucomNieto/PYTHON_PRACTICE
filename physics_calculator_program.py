print("PHYSICS CALCULATOR MENU")
print("1] Force")
print("2] Momentum")
print("3] Velocity")
print("4] Acceleration")
print("5] EXIT")
print("CHOOSE[1/2/3/4/5]")
calculator = input("CHOOSE ONE IN MENU: ")


if calculator == "1":
    mass = int(input("ENTER A MASS:"))
    acceleration = int(input("ENTER A ACCELERATION:"))
    force = mass * acceleration
    print("FORCE IS: ", force)

elif calculator == "2":
    mass = int(input("ENTER A MASS:"))
    velocity = int(input("ENTER A VELOCITY:"))
    memontum = mass * velocity
    print("MOMENTUM IS ", memontum)

elif calculator == "3":
    diplacement = int(input("ENTER A DISPLACEMENT:"))
    time = int(input("ENTER A TIME:"))
    velocity = diplacement * time
    print("VELOCITY IS ", velocity)

elif calculator == "4":
    initial = int(input("ENTER INITAL VELOCITY:"))
    final = int(input("ENTER A FINAL VELOCITY:"))
    time = int(input("ENTER TIME"))
    acceleration = (initial - final) / time
    print("ACCELEARION IS ", acceleration)

else:
    print("THANK YOU FOR USING MY PHYSICS CALCULATOR PROGRAM")