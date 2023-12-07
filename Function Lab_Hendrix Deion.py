#Deion Hendrix
#12/5/2023
#User Define Function
#Create User Functions

#This function take a bool parameter an returns an integer
def day_in_feb(is_leap_year):
    if is_leap_year == True:
        days=29
    else:
        days = 28
    return days

#Create Main Functions
def main():

    is_leap_year = False



    input_year = int(input("Enter a Year:" ))

      

    if (input_year % 4) == 0:      # inputYear is divisible by 4

      if (input_year % 100) == 0:   # inputYear is divisible by 100 (century year)

        if (input_year % 400) == 0: # inputYear is divisible by 400

          is_leap_year = True

        else:           # inputYear is not divisible by 400

          is_leap_year = False

      else:             # inputYear is not divisible by 100

        is_leap_year = True

    else:               # inputYear is not divisible by 4

      is_leap_year = False

      
#Call Bool Function
    num_day=day_in_feb(is_leap_year)
    print(f'The year {input_year} has {num_day} days in February.')
#Calling The Main Function
if __name__=="__main__":
    main()



