
"""
To check how many emails sent in a week and plotting a graph of it.
@eltonaloys
"""

from collections import defaultdict
import matplotlib.pyplot as plt
import datetime
from datetime import date

plt.style.use('ggplot')

def read():
    """To check how many emails sent in a week and plotting a graph of it."""
    fname = input("Enter the name of the file:  ")
    try:
        fp = open(fname, 'r')
    except FileNotFoundError:
        print(f"can't open {fname}")
    else:
        e_days = defaultdict(int)
        cnt = 0
        with fp:
            for line in fp:
                cnt += 1
                if line.startswith("Date:"):
                    n_line = line.split(" ")
                    n_line = n_line[1].strip("\n")
                    if n_line in ["Mon,", "Tue,", "Wed,", "Thu,", "Fri,", "Sat,", "Sun,"]:
                        e_days[n_line[:-1]] += 1             #Adding file to a dictionary
            try:
                if cnt == 0:
                    raise ValueError("The file that was given is Empty!")
            except ValueError:
                return(0,0)
            try:
                if len(e_days) == 0:
                    raise ValueError("Didn't find any email addresses in the file given")
            except ValueError:
                return(0,0)
            else:
                print(e_days)   #Returning a tuple containing email and its values
                x = ['Sunday','Monday','Tuesday','Wednessday','Thursday','Friday','Saturday']
                
                x_pos = [item + 1 for item, _ in enumerate(x)] #increating values for plotting graph
                plt.bar(x_pos, e_days.values(), color='green')
                plt.xlabel("Day of the week")
                plt.ylabel("No of Emails")
                plt.title("Count of emails per week")
                plt.xticks(x_pos, e_days)
                plt.show()

read()