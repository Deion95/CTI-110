#Deion Hendrix
#11/9/2023
#CTI-110 P1HW2-Travel Expense

print("This program calculates and displays travel expenses")

Budget=int(input("Enter Budget:"))

Destination=input("Enter your travel destination:")

Fuel=int(input("How much do you think you will spend on gas?:"))

Accomodations=int(input("How much do you think you will spend on Accomodations?:"))

Food=int(input("How much do yo think you will spend on Food?:"))

print("Total Travel Expenses")

print("Destination:",Destination)

print("Initial Budget:",Budget)

print("Fuel:",Fuel)

print("Accomodations:",Accomodations)

print("Food:",Food)

print("Remaining Balance:",Budget-Fuel-Accomodations-Food)


