#Deion Hendrix
#11/21/2023
#Using If/Else Statements for employee

#Get Input From User
emp_name=input("Enter the employee name:" )
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
reg_pay = emp_pay * reg_hours
gross_pay = ot_pay + reg_pay


print("Hours Worked  Pay Rate  Overtime  Overtime  Pay RegHour Pay   Gross Pay")
print("---------------------------------------------------------------------------------------------")
print(emp_hours,  emp_pay,   ot_hours,     ot_pay,    reg_pay,    gross_pay,)
    
