#Deion Hendrix
#11/21/2023
#Using If/Else Statement

#Get Value From user
Total_Change=int(input("Enter your amount  of change: "))

if Total_Change==0:
    print("No change")

#Calculate coins needed
Num_Quarters = Total_Change // 25
Total_Change = Total_Change - (25*Num_Quarters)

Num_Dimes = Total_Change // 10
Total_Change = Total_Change - (10*Num_Dimes)

Num_Nickels= Total_Change // 5
Total_Change = Total_Change - (5*Num_Nickels)

Num_Pennies = Total_Change // 1
Total_Change = Total_Change - (1*Num_Pennies)

#Display Results
if Num_Quarters > 0:
    if Num_Quarters==1:
        print("Quarter:", Num_Quarters)
    else:
        print("Quarters:", Num_Quarters)
if Num_Dimes > 0:
    if Num_Dimes==1:
        print("Dime:" ,Num_Dimes)
    else:
       print("Dimes:" ,Num_Dimes) 

if Num_Nickels > 0:
    if Num_Nickels==1:
        print("Nickel:" ,Num_Nickels)
    else:
        print("Nickels:" ,Num_Nickels)
if Num_Pennies > 0:
    if Num_Pennies==1:
        print("Penny:",Num_Pennies)
    else: 
        print("Pennies:" ,Num_Pennies)
