"""
String Manipulation
Converting words to singular and plural
@eltonaloys

"""
def plural(str):   
    """ Convert a word to its plural form. """

    if str[-2:] in ['ay','ey','iy','oy','uy']:
        return str + 's'    
    elif str.endswith('y'):
        return str[:-1] + 'ies'     
    elif str.endswith(('o','z','s','x','ch','sh')): 
        return str + 'es'
    else:
        return str + 's'
      

def main():
    """ Asking for a string from the user input """
    print("Enter a String or a list of strings seperated by space")
    try:
        mystring = input().split()
    except ValueError:
        raise ValueError("Invalid String")
    for item in mystring:
        print(plural(item))
    
main()  