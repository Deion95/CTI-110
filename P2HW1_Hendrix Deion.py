#Deion Hendrix
#11/14/2023
#P2HW2
from statistics import mean

#Get Input from user
Mod1=float(input("Enter Module 1 Grade:"))
Mod2=float(input("Enter Module 2 Grade:"))
Mod3=float(input("Enter Module 3 Grade:"))
Mod4=float(input("Enter Module 4 Grade:"))
Mod5=float(input("Enter Module 5 Grade:"))
Mod6=float(input("Enter Module 6 Grade:"))

#Create a Number List
Mod_List=[]

#Add Values to List
Mod_List.append(Mod1)
Mod_List.append(Mod2)
Mod_List.append(Mod3)
Mod_List.append(Mod4)
Mod_List.append(Mod5)
Mod_List.append(Mod6)

#Creating White Space
print("\n")

print("---Results---")


#Using Functions for calc
List_Sum=sum(Mod_List)
List_Avg=mean(Mod_List)
List_Min=min(Mod_List)
List_Max=max(Mod_List)

#Printing using normal string
print("Lowest Grade:",List_Min)
print("Highest Grade:",List_Max)
print("Sum of Grades:",List_Sum)
print("Average:",List_Avg)

#Output to user fomatted with f strings
print(f"Lowest Grade: {List_Min:.2f}")
print(f"Highest Grade: {List_Max:.2f}")
print(f"Sum of Grades: {List_Sum:.2f}")
print(f"Average: {List_Avg:.2f}")
