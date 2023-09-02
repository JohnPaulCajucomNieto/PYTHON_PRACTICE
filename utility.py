import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root", password="", database="dbrentsystem")
mycursor = mydb.cursor()

def add():
    VideoID = input("ENTER A VIDEO ID: ")
    VideoTitle = input("ENTER A VIDEO TITLE: ")
    Amount = float(input("ENTER AMOUNT: "))
    status = 1
    sql = "INSERT INTO tblvideos (VideoID, VideoTitle, Amount) VALUES (%s, %s, %s)"
    val = (VideoID, VideoTitle, Amount)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def delete():
    VideoID = input("ENTER A VIDEO ID: ")
    sql = "DELETE FROM tblvideos WHERE VideoID = %s"
    val = (VideoID,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def update():
    VideoID = input("ENTER A VIDEO ID: ")
    VideoTitle = input("ENTER A VIDEO TITLE: ")
    Amount = float(input("ENTER AMOUNT: "))
    sql = "UPDATE tblvideos SET VideoTitle = %s, Amount = %s WHERE VideoID = %s"
    val = (VideoTitle, Amount, VideoID)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) updated")

def search():
    VideoID = input("ENTER A VIDEO ID: ")
    sql = "SELECT * FROM tblvideos WHERE VideoID = %s"
    val = (VideoID,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def main():
    while True:
        print("---------------------------")
        print("CRUD STOCK VIDEO TAPES INVENTORY SYSTEM")
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
        elif choice == '2':
            update()
        elif choice == '3':
            delete()
        elif choice == '4':
            search()
        else:
            print("GOOD DAY, THANK YOU FOR USING MY VIDEO TAPES INVENTORY SYSTEM!")
            mydb.close()
            exit()

if __name__ == "__main__":
    main()




