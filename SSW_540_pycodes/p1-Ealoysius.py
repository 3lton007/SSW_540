"""
@Elton 

A Python Script where input() and print()
is used to describe the users 
First name and Last name

"""

fst_name = print("Please tell me your First name:") #Printing Firstname    
a = input(fst_name)                                 #Taking Firstname as Input (a)
lst_name = print("Please tell me your Last name")    #Printing Lastname
b = input(lst_name)                                  #Taking Lastname as Input(b)

while  True:
    if(a.isdigit() == True): 
        if(b.isdigit() == True):                   #To check if the input is proper String        
            print("First name is not a Proper String")
            print("Please Enter First name again:")
            a = input(fst_name)
            print("Please Enter Last name again:")
            print("Last name is not proper String")
            b = input(lst_name)
        else:
    
            break
            
    else:
       break
    

print("Hello",a,b)  

"""
while True:
    if(b.isdigit()) == True:                         #To check if the input is proper string

        print("Its not a Proper String")
        print("Please Enter Last name again:")
        b = input(lst_name)
    else:
        break  
       
                                 #Printing both Firstname and Lastname


print("Enter a no")
score = input()
while True:
    if score.isnumeric() == True:

        print("It is : proper")
        break         
        
    else:
        
        print("It is NOT proper")
        print("Enter numeric score again")
        score = input()
       
print("Number entered is :",score)
"""
# print("Enter a no")
# f = input()
# # while True:
# #     if()
# # print(f)
    