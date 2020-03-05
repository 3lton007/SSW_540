"""
@Elton ALoys

A python Script where user takes three input
and returns a maximum value
"""

try:
        a, b, c = input("Enter Three numbers:").split()
        a, b, c = int(a), int(b), int(c)
except ValueError:
        print("User input is not a proper Integer")

while True:
        if (isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
                if (a > b) and (a > c):
                        print ("a is max")
                elif (b > a) and (b > c):
                        print ("b is max")
                elif (c > a) and (c > b):
                        print("c is max")
                else:
                        print("Two or all the three numbers are equal")
                exit()           
        else:
                a, b, c = input("Enter Three numbers again:")
                a, b, c = int(a), int(b), int(c)   
                

      
