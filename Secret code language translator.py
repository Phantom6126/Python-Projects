#exercise - secret code language translator

"""
conditions and logics-
    coding the message: 
        - if the word contains atleast 3 characters , remove the first letter of word and append it to the ending of word.
        - now append(i.e add) three random characters at the starting and ending of the word.
        - else the word contains only two characters then reverse it.

    decoding the message:
        - if the word contains atleast 3 characters , remove the three random letters from starting and ending of the word.
        - now remove the last letter of word and append the letter to the starting of word.
        - else the word contains only two characters then reverse it.

"""

import random 
import string as s

def rand_char(length):
    letters = s.ascii_letters
    return "".join(random.choice(letters) for i in range(length))

print(" \\\\\\\\\\","SECRET CODE LANGUAGE TRANSLATOR","///// ")

mode = input("Enter 'c' for coding and 'd' for decoding:")

str = input("Enter the message :")
words = str.split(" ")

if(mode=='c'):
    new_words = []
    for word in words:
        if(len(word)>=3):
            random1 = rand_char(3)
            random2 = rand_char(3)
            str_new = random1+word[1:]+word[0]+random2
            new_words.append(str_new)
        else:
            new_words.append(word[::-1])
    print(" ".join(new_words))

else:
    new_words = []
    for word in words:
        if(len(word)>=3):
            str_new = word[3:-3]
            str_new = str_new[-1]+str_new[:-1]
            new_words.append(str_new)
        else:
            new_words.append(word[::-1])
    print(" ".join(new_words))

print(" ~Thank You~ ")

