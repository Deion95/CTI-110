#Deion Hendrix
#P2LAB2
#11/28/2023
#Using a for loop with the range

#Get Input from user

num1=int(input('Enter an integer: '))
num2=int(input('Enter an integer higher than the first: '))

#Make an if Statement(if the first number is smaller)
if num1 < num2:
    for i in range(num1,num2 + 1,5):
         print(i)
else:
    #print("Second integer can't be less than the first")
    #while the input is invaild
    while num1 > num2 or num1 == num2:
        print("Second integer can't be less than the first")
        #Get Input from user 
        num1=int(input('Enter an integer: '))
        num2=int(input('Enter an integer higher than the first: '))
    for i in range(num1,num2 + 1,5):
         print(i)
    

