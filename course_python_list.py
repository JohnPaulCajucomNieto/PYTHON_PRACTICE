#PYTHON LIST
course = []
#INFINITE LOOP THAT CONDITION IS TRUE
while True:
    #PRINT ENROLLEMENT SYSTEM
    print("\nENROLLMENT SYSTEM")
    print("-----------------------------------------------")
    #LIST OF COURSE
    print("\nLIST OF AVAILABLE COURSE:")
    #BSIT
    print("1] BS INFORMATION TECHNOLOGY")
    #BSIS
    print("2] BS INFORMATION SYSTEMS ")
    #BSCS
    print("3] BS COMPUTER SCEINCE")
    #BSIT
    print("4] BS INDUSTRIAL TECHNOLOGY")
    print("-----------------------------------------------")
    #CHECK AND TO CLARIFY YOUR INFO
    print("5] CHECK YOUR INFORAMTION")
    #DELETE RECORDS
    print("6] DELETE THE STUDENTS THAT NOT DID NOT INFORM")
    #ENROLLED STUDENTS
    print("7] LIST OF ENROLLED STUDENTS")
    #EXIT END OF A PROGRAM
    print("8] EXIT")
    print("-----------------------------------------------")
    #INPUT A CHOICES 1 TO 8
    choices = input("Choose [1/2/3/4/5/6/7/8]: ")
    print("-----------------------------------------------")

    #CONDITIONAL STATEMENTS IF CHOICES IS TO 1
    if choices == "1":
        print("\n-----------------------------------------------")
        #INPUT F NAME
        freshmen_student = input("ENTER YOUR FIRST NAME: ")
        # INPUT M NAME
        freshmen_student = input("ENTER YOUR MIDDLE NAME: ")
        # INPUT L NAME
        freshmen_student = input("ENTER YOUR LAST NAME: ")
        # INPUT E NAME
        freshmen_student = input("ENTER YOUR NAME EXTENSION, EG:JR: ")
        # INPUT A DATE OF BIRTH
        freshmen_student = input("ENTER YOUR DATE OF BIRTH: ")
        # INPUT ADDRESS
        freshmen_student = input("ENTER YOUR ADDRESS: ")
        # INPUT A CITY
        freshmen_student = input("ENTER YOUR CITY: ")
        # INPUT A PROVINCE
        freshmen_student = input("ENTER YOUR PROVINCE: ")
        # INPUT A ZIPCODE
        freshmen_student = input("ENTER YOUR ZIP CODE: ")
        # INPUT A GENDER
        freshmen_student = input("ENTER YOUR GENDER: ")
        # INPUT A RELIGION
        freshmen_student = input("ENTER YOUR RELIGION: ")
        # INPUT A PHONE NUMBER
        freshmen_student = input("ENTER YOUR PHONE NUMBER: ")
        # INPUT GUARDIAN NAME
        freshmen_student = input("ENTER YOUR GUARDIAN NAME: ")
        # INPUT FB ACC
        freshmen_student = input("ENTER YOUR FACE BOOK ACCOUNT NAME: ")
        #COURSE  TO ADD IN FREESHMEN STUDENT
        course.append(freshmen_student)
        print("YOU ARE ALREADY ENROLL IN BS INFORMATION TECHNOLOGY.")
        print("-----------------------------------------------")
        # CONDITIONAL STATEMENTS IF CHOICES IS TO 2
    elif choices == "2":
        print("-----------------------------------------------")
        #INPUT FIRST NAME
        freshmen_student = input("ENTER YOUR FIRST NAME: ")
        #INPUT MIDDLE NAME
        freshmen_student = input("ENTER YOUR MIDDLE NAME: ")
        #INPUT LAST NAME
        freshmen_student = input("ENTER YOUR LAST NAME: ")
        #INPUT EXTENSION NAME
        freshmen_student = input("ENTER YOUR NAME EXTENSION, EG:JR: ")
        #INPUT DATE OF BIRTH
        freshmen_student = input("ENTER YOUR DATE OF BIRTH: ")
        # INPUT ADDRESS
        freshmen_student = input("ENTER YOUR ADDRESS: ")
        # INPUT CITY
        freshmen_student = input("ENTER YOUR CITY: ")
        # INPUT  PROVINCE
        freshmen_student = input("ENTER YOUR PROVINCE: ")
        # INPUT ZIP CODE
        freshmen_student = input("ENTER YOUR ZIP CODE: ")
        # INPUT GENDER
        freshmen_student = input("ENTER YOUR GENDER: ")
        # INPUT RELIGION
        freshmen_student = input("ENTER YOUR RELIGION: ")
        # INPUT PHONE NUMBER
        freshmen_student = input("ENTER YOUR PHONE NUMBER: ")
        # INPUT GUARDIAN NAME
        freshmen_student = input("ENTER YOUR GUARDIAN NAME: ")
        # INPUT FB ACCOUNT
        freshmen_student = input("ENTER YOUR FACE BOOK ACCOUNT NAME: ")
        #COURSE THAT ADD IN FRESHMEN STUDENT
        course.append(freshmen_student)
        print("YOU ARE ALREADY ENROLL IN BS INFORMATION SYSTEM.")
        print("-----------------------------------------------")
        # CONDITIONAL STATEMENTS IF CHOICES IS TO 3
    elif choices == "3":
        print("-----------------------------------------------")
        # INPUT FIRST NAME
        freshmen_student = input("ENTER YOUR FIRST NAME: ")
        # INPUT MIDDLE NAME
        freshmen_student = input("ENTER YOUR MIDDLE NAME: ")
        # INPUT LAST NAME
        freshmen_student = input("ENTER YOUR LAST NAME: ")
        # INPUT NAME EXTENSION
        freshmen_student = input("ENTER YOUR NAME EXTENSION, EG:JR: ")
        # INPUT DATE OF BIRTH
        freshmen_student = input("ENTER YOUR DATE OF BIRTH: ")
        # INPUT ADDRESS
        freshmen_student = input("ENTER YOUR ADDRESS: ")
        # INPUT CITY
        freshmen_student = input("ENTER YOUR CITY: ")
        # INPUT PROVINCE
        freshmen_student = input("ENTER YOUR PROVINCE: ")
        # INPUT ZIP CODE
        freshmen_student = input("ENTER YOUR ZIP CODE: ")
        # INPUT GENDER
        freshmen_student = input("ENTER YOUR GENDER: ")
        # INPUT RELIGION
        freshmen_student = input("ENTER YOUR RELIGION: ")
        # INPUT PHONE NUMBER
        freshmen_student = input("ENTER YOUR PHONE NUMBER: ")
        # INPUT GUARDIAN NAME
        freshmen_student = input("ENTER YOUR GUARDIAN NAME: ")
        # INPUT FB NAME
        freshmen_student = input("ENTER YOUR FACE BOOK ACCOUNT NAME: ")
        print("-----------------------------------------------")
        # COURSE TO ADD IN FRESHMEN STUDENT
        course.append(freshmen_student)
        print("YOU ARE ALREADY ENROLL IN BS COMPUTER SCIENCE.")
        # CONDITIONAL STATEMENTS IF CHOICES IS TO 4
    elif choices == "4":
        print("-----------------------------------------------")
        # INPUT FIRST NAME
        freshmen_student = input("ENTER YOUR FIRST NAME: ")
        # INPUT MIDDLE NAME
        freshmen_student = input("ENTER YOUR MIDDLE NAME: ")
        # INPUT LAST NAME
        freshmen_student = input("ENTER YOUR LAST NAME: ")
        # INPUT NAME EXTENSION
        freshmen_student = input("ENTER YOUR NAME EXTENSION, EG:JR: ")
        # INPUT DATE OF BIRTH
        freshmen_student = input("ENTER YOUR DATE OF BIRTH: ")
        # INPUT ADDRESS
        freshmen_student = input("ENTER YOUR ADDRESS: ")
        # INPUT CITY
        freshmen_student = input("ENTER YOUR CITY: ")
        # INPUT PROVINCE
        freshmen_student = input("ENTER YOUR PROVINCE: ")
        # INPUT ZIP CODE
        freshmen_student = input("ENTER YOUR ZIP CODE: ")
        # INPUT GENDER
        freshmen_student = input("ENTER YOUR GENDER: ")
        # INPUT RELIGION
        freshmen_student = input("ENTER YOUR RELIGION: ")
        # INPUT PHONE NUMBER
        freshmen_student = input("ENTER YOUR PHONE NUMBER: ")
        # INPUT GUARDIAN NAME
        freshmen_student = input("ENTER YOUR GUARDIAN NAME: ")
        # INPUT FB NAME
        freshmen_student = input("ENTER YOUR FACE BOOK ACCOUNT NAME: ")
        print("-----------------------------------------------")
        # COURSE TO ADD IN FRESHMEN STUDENT
        course.append(freshmen_student)
        print("YOU ARE ALREADY ENROLL IN BS INDUSTRIAL TECHNOLOGY.")
        # CONDITIONAL STATEMENTS IF CHOICES IS TO 5
        #ELSE IF = 5
    elif choices == "5":
        #INPUT ENROLLED STUDENTS
        info = input("ENTER THE NAME OF ENROLLED STUDENTS: ")
        #TO CHECK THE DICTIONARY OF COURSE
        if info in course:
            #INPUT A CLARIFY INFO
            student_edited = input("CLARIFY YOUR INFORMATION: ")
            clarify= course.index(info)
            course[clarify] = student_edited
            print("THE ENROLLED STUDENTS IS SUCCESSFUL UPDATE HIS INFORMATION.")
        else:
            print("SORRY YOUR NAME IS NOT ON THE RECORD!")
            # CONDITIONAL STATEMENTS IF CHOICES IS TO 6
            # ELSE IF = 6
    elif choices == "6":
        #DECLARED A VARIABLE AND TO INPUT A NAME OF ENROLLED STUDENTS
        record = input("ENTER THE NAME OF ENROLLED STUDENTS: ")
        # TO CHECK THE DICTIONARY OF COURSE
        if record in course:
            loc = course.index(record)
            course.remove(record)
            print("REMOVE")
        else:
            print("SORRY YOUR NAME IS NOT ON THE RECORD!")
    # CONDITIONAL STATEMENTS IF CHOICES IS TO 7
    elif choices == "7":
        print("LIST OF ENROLLED A STUDENTS")
        #LENGTH OF COURSE
        #LENGTH LIST OF DICTIONARIES
        if len(course) > 0:
            #ITERATE A ELEMENTS
            for record_student in course:
                print(record_student)
        else:
            print("SORRY YOUR NAME IS NOT ON THE RECORD!")
    else:
        print("-----------------------------------------------")
        print("GOOD LUCK TO YOUR JOURNEY IN CHOOSING A COURSE, PADAYON!")
        exit()
        print("-----------------------------------------------")
