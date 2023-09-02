import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="dbinventory")
mycursor = mydb.cursor()

def add():
    ProductID = input("ENTER A PRODUCT ID: ")
    ProductName = input("ENTER A PRODUCT NAME: ")
    Price = float(input("ENTER A PRICE: "))
    status = 1
    sql = "INSERT INTO tblproducts (ProductID, ProductName, Price) VALUES (%s, %s, %s)"
    val = (ProductID, ProductName, Price)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def delete():
    ProductID = input("ENTER A PRODUCT ID: ")
    sql = "DELETE FROM tblproducts WHERE ProductID = %s"
    val = (ProductID,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def update():
    ProductID = input("ENTER A PRODUCT ID: ")
    ProductName = input("ENTER A PRODUCT NAME: ")
    Price = float(input("ENTER A PRICE: "))
    sql = "UPDATE tblproducts SET ProductName = %s, Price = %s WHERE ProductID = %s"
    val = (ProductName, Price, ProductID)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) updated")

def search():
    ProductID = input("ENTER A PRODUCT ID: ")
    sql = "SELECT * FROM tblproducts WHERE ProductID = %s"
    val = (ProductID,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def main():
    while True:
        print("---------------------------")
        print("CRUD STOCK INVENTORY SYSTEM")
        print("1] ADD")
        print("2] UPDATE")
        print("3] DELETE")
        print("4] SEARCH")
        print("5] EXIT")
        print("---------------------------")
        choice = input("CHOOSE ONE [1/2/3/4/5]: ")
        print("---------------------------")

        if choice == '1':
            add()
        if choice == '2':
            update()
        if choice == '3':
            delete()
        if choice == '4':
            search()
        if choice == '5':
            print("GOOD DAY, THANK YOU FOR USING MY STOCK INVENTORY SYSTEMS!")
            exit()

if __name__ == "__main__":
    main()