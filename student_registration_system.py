students = []

while True:
    print("STUDENT REGISTRATION SYSTEM")
    print("1] New Student")
    print("2] Edit Student")
    print("3] Delete Student")
    print("4] List Students")
    print("5] Exit")

    choice = input("Choose [1/2/3/4/5]:")

    if choice == '1':
        new_student = input("Enter the name of the student:")
        students.append(new_student)
        print("The new student is successfully added.")
    elif choice == '2':
        student_orig = input("Enter the name of the student:")
        if student_orig in students:
            student_edited = input("Enter the new name of the student:")
            location = students.index(student_orig)
            students[location] = student_edited
            print("The student is successfully edited.")
        else:
            print("Record not found!")
    elif choice == '3':
        student_name = input("Enter the name of the student:")
        if student_name in students:
            location = students.index(student_name)
            students.remove(student_name)
            print("The student is successfully deleted.")
        else:
            print("Record not found!")
    elif choice == '4':
        print("Students List")
        if len(students) > 0:
            for s in students:
                print(s)
        else:
            print("No records found!")
    else:
        print("Thank you for using my Student Registration System")
        exit()