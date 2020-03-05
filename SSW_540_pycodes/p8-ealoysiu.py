"""
To find frequency of emails by a sender
@eltonaloys

"""

def main():
    """ Function to find frequency of emails sent"""
    try:
        filename = input("Enter a Filename ")
        fp = open(filename, "r")
    except FileNotFoundError:
        print("File not found in your directory!")
    else:
        with fp:
            " Using a list to find multiple instance of each sender as list takes multiple values"
            email = list()
            " Dictionary for key = email and frequency = values"
            dd = dict()
            for line in fp:
                line = line.lower().rstrip("\n")
                if line.startswith("from: "):
                    email.append(line)
            for c in email:
                """ incrementing the email freq by applying a counter """
                dd[c] = dd.get(c,0) + 1

            value = list(dd.values())
            key = list(dd.keys())
            try:
                res = key[value.index(max(value))]
            except ValueError:
                raise ValueError("No email addresses in file")
            else:
                return f"{res} = {dd[res]}"     #returning email and frequency of the maximum sender

print(main())

