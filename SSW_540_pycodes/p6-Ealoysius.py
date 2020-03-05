"""
Slicing and Dicing Files
@eltonaloys
"""

def main():
    """ Function to calcualte average from the numbers inside the file"""

    try:
        #Get the File name
        filename = input("Enter a Filename: ")

        #Open the file
        fp = open(filename, "r")
    except FileNotFoundError:
        raise FileNotFoundError("File Not FOund")
    else:
        total = 0.0
        length = 0.0

        with fp:
           for line in fp:
                if "X-DSPAM-Confidence:" in line:
                    line = line.rstrip("\n")
                    word , number = line.split()
                    try:
                        amount = float(number)
                    except ValueError:
                        raise ValueError("Invalid Value for Confidence")     
                    total = total + amount
                    length = length + 1
                    print(line)

                try:
                    print(f" Result: {round(total/length, 4)}")
                except ZeroDivisionError:
                    raise ZeroDivisionError("Not a Single Spam Confidence value found")
main()            



     