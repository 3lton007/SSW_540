"""

Using Regular Expression 

@eltonaloys

"""
import os
from re import findall


def regex(path):
    file_name = path
    try:
        fp = open(file_name, "r")
    except FileNotFoundError:
        raise FileNotFoundError("There is no such file in directory!")
    else:
        if os.stat(file_name).st_size <= 0:
            raise FileNotFoundError
        with fp:
            for line in fp:
                line = line.split("\n")
                check = findall("New Revision: ([0-9]+)", fp.read())
                try:
                    value = [int(item) for item in check]
                except ValueError:
                    raise ValueError("Invalid Integer")
                number = round(sum(value)/len(value), 1)
                a = len(check)
            try:
                return f"Average = {number}\nNUmber of lines = {a}"
            except ZeroDivisionError:
                raise ZeroDivisionError("Not a Single Revision: Value Found")
def main():
    r = input("Enter filename ")
    print(regex(r))

main()

