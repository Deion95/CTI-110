#Deion Hendrix
#11/30/2023
#Using If/Else Statements for employee

#Creat Variables to hold totals paid
Total_Em = 0
Total_Reg = 0
Total_OT = 0
Total_gross = 0

#Get Input From User
emp_name=input('Enter the employee name or "Done":' )
Total_Em += 1
while emp_name != "Done":
    emp_hours=int(input("Enter the employee's hour: "))
    emp_pay=float(input("Enter employee's pay rate: "))
    print("------------------------------------------")


    print("Employee Name:", emp_name)
    print("\n")


    if emp_hours > 40:
        ot_hours = emp_hours - 40
        reg_hours = 40
    else:
        ot_hours=0
        reg_hours=emp_hours

#Calculate Pay
    ot_pay =(emp_pay * 1.5)*ot_hours
    Total_OT += ot_pay
    reg_pay = emp_pay * reg_hours
    Total_Reg += reg_pay
    gross_pay = ot_pay + reg_pay
    Total_gross += gross_pay


    print("Hours Worked  Pay Rate  Overtime  Overtime  Pay RegHour Pay   Gross Pay")
    print("---------------------------------------------------------------------------------------------")
    print(emp_hours,  emp_pay,   ot_hours,     ot_pay,    reg_pay,    gross_pay,)
    print("\n")
    emp_name=input('Enter the employee name or "Done":' )

print("Done with Employees")

print("\n")

print(f"Total number of employees : {Total_Em}")
print(f"Total amount of regular pay : {Total_Reg}")
print(f"Total amount paid for overtime: {Total_OT}")
print(f"Total paid in gross: {Total_gross}")


