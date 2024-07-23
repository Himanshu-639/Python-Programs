#Que.2:

import os
os.system('clear')
x=input("Enter a character :")
assert len(x)==1, "Enter a single character."

def char_check(x):
    number_words={
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero"
    }
    
    if x.isdigit():
        print("number")
        print(number_words[x])
        
    elif x.isalpha():
        print("alphabet")
        if x.islower():
            print("lower")
        if x.isupper():
            print("upper")
    else:
        print("special characters")
char_check(x)