"""

@FInding Unique Strings

"""
import os

def get_lines(path):
    """ To get the file directory and check for From: """
    try:
        fp = open(path, "r")
    except FileNotFoundError:
        raise FileNotFoundError("File not Found")
    else:
        
        
            #To check for empty file
            with fp:
                c = 'From:'
                email_id = set()
                for line in fp:
                    if c in line:
                        email_id.add(line)
                if len(email_id) == 0:
                    print("The keyword From, is not present")
                else:
                    print(len(email_id))     
        else:
            print("Empty File")

def main():
    """ Get the input user! """
    filename = input("Enter a Filename ")
    get_lines(filename)

main()



              