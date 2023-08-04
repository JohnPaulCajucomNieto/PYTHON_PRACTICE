#INPUT A STUDENT NAME
Student = input("\nENTER THE STUDENT NAME:")
#INPUT A PRELIM GRADE
Prelim_Grade = float(input("ENTER THE PRELIM GRADE:"))
#INPUT A MIDTERM GRADE
Midterm_Grade = float(input("ENTER THE MIDTERM GRADE:"))
#INPUT A FINAL GRADE
Final_Grade = float(input("ENTER THE FINAL GRADE:"))
#FORMULA OF AVERAGE GRADE TO PG*MG*FG GRADE
average_grade = Prelim_Grade * 0.3 + Midterm_Grade * 0.3 +Final_Grade * 0.4

#OUTPUT OF THIS PROGRAM
print("\nGRADE COMPUTATION")
print("------------------------------------")
print("STUDENT NAME:" ,Student)
print("AVERAGE GRADE:" ,average_grade)
print("------------------------------------")
