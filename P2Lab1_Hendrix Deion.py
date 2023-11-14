#Deion Hendrix
#11/14/2023/
#Use Float values to tr

#Get Input
MPG=float(input("Enter Miles Per Gallon Decimal:"))
Price_Gallon=float(input("Enter The Cost for One Gallon Decimal:"))

#Calc Cost to Drive 20 miles
Drive_Cost20=(MPG/20)*Price_Gallon

#Calc Cost to Drive 75 miles
Drive_Cost75=(75/MPG)*Price_Gallon

#Calc Cost to Drive 500 miles
Drive_Cost500=(500/MPG)*Price_Gallon

#Cost
print(f"Cost to drive 20 miles is {Drive_Cost20:.2f}")
print(f"Cost to drive 75 miles is {Drive_Cost75:.2f}")
print(f"Cost to drive 500 miles is {Drive_Cost500:.2f}")
