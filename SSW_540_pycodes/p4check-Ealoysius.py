import random
"""

Guess a number game!!
@EltonAloys

"""

ran = random.randint(1,20)          #Using pythons inbuilt random function for randomizing the values 
print(">>>>>Guess The Number Game<<<<<<")
print("A number is generated between 1- 20")
print("Enter a number")

try:                                #Catching exception 
    a = int(input())
except ValueError:
    print("Invalid Integer")
    a = int(input())  

print("The guessed number by player is: ",a)

i = 0                               #Using a while loop for 6 iteration of guessing chances for the player
while i <= 4:
    if a < ran:
        print("Guess is low")
        a = int(input("Guess Again:"))
        i = i + 1 
        continue
    elif a > ran:
        print("Guess is High")
        a = int(input("Guess Again:"))
        i = i + 1
        continue
    else:
        print("You guessed it correctly")
    break       
print("The target number was :",ran)
