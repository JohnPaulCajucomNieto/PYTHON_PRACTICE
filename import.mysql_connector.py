import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dbstore"
)

mycursor = mydb.cursor()

def insert_user():
    ORNo = input("Enter the ORNo: ")
    Amount = input("Enter the Amount: ")
    status = 1
    sql = "INSERT INTO tblsales (ORNo, Amount) VALUES (%s, %s)"
    val = (ORNo, Amount)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def delete_user():
    ORNo = input("Enter the ORNo: ")
    sql = "DELETE FROM tblsales WHERE ORNo= "+ORNo+""
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def update_user():
    ORNo = input("Enter the ORNo ")
    Amount = input("Enter the Amount: ")
    sql = "UPDATE tblsales SET Amount = "+Amount+" WHERE ORNo = "+ORNo+""
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

def search_user():
    ORNo = input("Enter the User ID: ")
    sql = "SELECT * FROM tblsales WHERE ORNo ="+ORNo+""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def main():
    while True:
        print("User Management Menu")
        print("1. Search User")
        print("2. Add User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Enter your choice [1/2/3/4/5]: ")

        if choice == '1':
            search_user()
        if choice == '2':
            insert_user()
        if choice == '3':
            update_user()
        if choice == '4':
            delete_user()
        if choice == '5':
            print("Thank you for using User Management System")
            exit()

if __name__ == "__main__":
    main()



