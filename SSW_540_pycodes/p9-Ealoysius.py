"""

To understand how the file counts total number of words,
the count of unique words and also top 25 words occuring.
@eltonaloys

"""
#importing defaultdict, punctuation, itemgetter from collections, string and operator
from collections import defaultdict
from string import punctuation
from operator import itemgetter




def read(path):
    """ Function to read the file and count words in the file """
    filename = path
    try:
        fp = open(filename, "r")
    except FileNotFoundError:   #Exception handling for no file!
        raise FileNotFoundError("There is no such file in directory!")
    else:
        with fp:
            #initalizing a Default Dictionary
            dd = defaultdict(int)
            for words in fp.read().split():
                word = words.lower()
                #Removes Punctuations within a file.
                punc_translator = str.maketrans("","", punctuation)
                clean_str = word.translate(punc_translator)
                if clean_str not in dd:
                    dd[clean_str] = 1
                else:
                    dd[clean_str] += 1
            #Sorts the dictioanry according to the values
            sort = sorted(dd.items(), key = itemgetter(1), reverse = True)
            top25 = sort[:25]  #Sorts First 25 words occuring 
            total_words = "{:,}".format(sum(dd.values())) #Counts Total words
            unique_words = "{:,}".format(len(sort)) #counts Unique words

            return f"TOTAL WORDS = {total_words}\nTOTAL UNIQUE WORDS = {unique_words}\nTOP25 = {top25}"

r = input("Enter the Filename ")
print(read(r))



