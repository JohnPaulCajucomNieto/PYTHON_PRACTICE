books = {" "}
while True:
    print("Student Set")
    print("1. Add Books")
    print("2. Delete Books")
    print("3. Book list")
    print("4. Exit")
    opt = input("Choose Option [1/2/3/4]: ")
    if opt == '1':
        name = input("Enter Book Name to Add: ")
        books.add(name)
        print("Book Added Successfully ")
        print(books)
    elif opt =='2':
        names = input("Enter Name to Delete: ")
        if name in books:
            books.remove(names)
            print('Delete Successfully')
        else:
            print("Book Not Found!!")
    elif opt =='3':
        print("Books Set ")
        print(books)
    else:
        print("END OF PROGRAM!!!")