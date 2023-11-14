#Deion Hendrix
#11/14/2023
#Mathemiatical expression,list and f-string
from statistics import mean 

#Get Input from User
Num_1=float(input("Enter a Float Value:"))
Num_2=float(input("Enter a Float Value:"))
Num_3=float(input("Enter a Float Value:"))
Num_4=float(input("Enter a Float Value:"))

#Create a Empty List
Num_List=[]

#Add Values to the list
Num_List.append(Num_1)
Num_List.append(Num_2)
Num_List.append(Num_3)
Num_List.append(Num_4)

#print to ensure value 
print(Num_List)

List_Sum=sum(Num_List)
List_Avg=mean(Num_List)
             
print(List_Sum)
print(List_Avg)

#output to user formatted with f strings
print(f"{List_Sum:.0f} {List_Avg:.0f}")
print(f"{List_Sum:.3f} {List_Avg:.3f}")
