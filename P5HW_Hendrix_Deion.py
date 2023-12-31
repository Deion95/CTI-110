#Deion Hendrix
#12/7/2023
#Using Functions , Loops and Random Numbers

#Importing Random
import random

#Creating Menu Functions
def show_menu():
    print("Welcome to Math Quiz")
    print("Main Menu")
    print("-------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

#This function adds two random numbers
def add():
    ran1=random.randint(0,10)
    ran2=random.randint(0,10)
    print(f"{ran1} + {ran2}" )
    return ( ran1 + ran2)

#This function subtract two random numbers
def subtract():
    ran1=random.randint(0,10)
    ran2=random.randint(0,10)
    print(f"{ran1} - {ran2}")
    return ( ran1 - ran2)
#This function simulates the user guessing
#While the guess is create while
def guessing(guess,correct_answer):
    num_guess=0
    

    while guess != correct_answer:
        num_guess += 1
        if guess > correct_answer:
            print("Your guess is too high")
            guess = int(input("Please enter another answer: ")) #Represents user guess

        else:
            print("Your guess is too low")
            guess = int(input("Please enter another answer: ")) #Represents user guess


    print("This answer is correct")
    print(f"It took you {num_guess} incorrect guesses")



#Main Function
def main():
    show_menu()
    select=int(input("Please select an menu option: "))
    while select !=3:
        if select == 1:
            ran_sum=add()#Represent correct answers
            my_guess = int(input("What is your answer: ")) #Represents user guess
            guessing(my_guess,ran_sum)
            print()
            show_menu()
            select=int(input("Please select an menu option: "))

        if select == 2:
            ran_sum=subtract()#Represent correct answers
            my_guess = int(input("What is your answer: ")) #Represents user guess
            guessing(my_guess,ran_sum)
            print()
            show_menu()
            select=int(input("Please select an menu option: "))
            

   #if user choice == 3 the while loop breaks
    print("Thanks you for playing, goodbye")
    
        
        
if __name__ == "__main__":
    main()
