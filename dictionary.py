student = {
    "Name" : " ", "Course": " "
}
while True:
    print("1. Student Name ")
    print("2. Student Course ")
    print("3. Delete")
    print("4. Dictionary ")
    print("5. Exit")
    opt = input("Choose Option [1/2/3/4]")
    if opt =='1':
        student['Name'] = input("Enter Name ")
        print("Dictionary Updated")
    elif opt =='2':
        student['Course'] = input("Enter Course ")
    elif opt =='3':
        name = input("Choose Name or Course to Delete!")
        if name in student:
            student.pop(name)
            print("Name Delete!!")
        elif course in student:
            student.pop(course)
            print("Course Deleted!!")
        else:
            print("Type Name or Course")
    elif  opt =='4':
        print(student)
    else:
        print("Exit!!")
        break