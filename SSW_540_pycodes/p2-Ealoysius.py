"""

@Elton Aloysius

A Python SCript
TO Convert NUmerical Scores To Grades

"""

print("Enter a numeric score:")
s = input()                                         #Storing Input Value

while True:                                         #Loop To Check whether the value is a proper Integer.
    if s.isnumeric() == True:
        print("It is a proper Integer")
        break
    else:
        print("It is not proper Integer")
        try:
            raise ValueError
        except ValueError as error:
            print("Enter numeric score again")
        s = input()

print("Number entered is :",s) 
score = int(s)                                      #Converting the value to Integer.

if score > 100 or score < 0:                       #Exception applied for Integer Beyond the Grading System.
    try:
        raise ValueError
    except ValueError as error:
        print('Given no. is invalid, Keep a no. between [1-100]')
    
elif score >= 93:
    print("A")
elif score >= 90 and score < 93:
    print("A-")
elif score >= 87 and score < 90:
    print("B+")
elif score >= 83 and score < 87:
    print("B")
elif score >= 80 and score < 83:
    print("B-")
elif score >= 70 and score < 80:
    print("C")
else:
    print("F")

    
