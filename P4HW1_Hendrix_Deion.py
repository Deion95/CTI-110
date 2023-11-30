#Deion Hendrix
#11/28/2023
#P4HW1
#use loop to get user input
from statistics import mean

#get number of grades from user
num_grades=int(input("How many grades do you want to enter: "))

#Create List to store the grade entered
Mod_List=[]

#Get grades for user
for i in range(num_grades):

    Mod=float(input(f"Enter Module {i+1} Grade: "))
    while Mod < 0 or Mod >100:
        print("Invalid grade entered. Please submit another: ")
        Mod=float(input(f"Enter Module {i+1} Grade: "))
        Mod_List.append(Mod)
print(Mod_List)



#Creating White Space
print("\n")

print("------Results-------")


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

print("\n")

#Output to user fomatted with f strings
print(f"Lowest Grade: {List_Min:.2f}")
print(f"Highest Grade: {List_Max:.2f}")
print(f"Sum of Grades: {List_Sum:.2f}")
print(f"Average: {List_Avg:.2f}")

