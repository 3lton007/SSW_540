"""
    To interact with web sites
    from Python and to get more
    experience with regular expressions

by: @eltonaloys
"""
import urllib.request  #importing URL and REGEX package libraries
from re import findall


def urlcount(r):
    httpurl = [] #Taking All the Values in a List
    
    try:
        req = urllib.request.urlopen(r).read() #Requesting for opening url
    except ValueError:
        raise ValueError("URL is Invalid")
    else:
        urls = findall(b'"(http[s]?://.*?)"', req) #Using regex to find "http/https"
    for items in urls:
        httpurl.append(items)
    allhttps = set(httpurl) #Taking Unique Values in a set
    counthttps = len(allhttps)
    return f"The count of distinct http/https is: {counthttps}" #Printing count of distinct values
            
def main():
    r = input("Enter URL(Eg: https://www.youtube.com) \n")
    print(urlcount(r))

main()




