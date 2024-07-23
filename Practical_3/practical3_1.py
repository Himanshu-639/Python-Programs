#Que.1:

import os
os.system('clear')
x=input("Enter a string : ")

def vowel_count(x):
    vowels="aeiou"
    count=0
    a=x.lower()
    for char in a:
        count+=1
    print("The number of vowels in the given string is ", count)


def word_count(x):
    a=x.replace(" ", "")
    b=len(a)
    print("The total number of words in the given string is ", b)


def unique_word_count(x):
    a=set(x)
    b=len(a)
    print("The number of unique words in given string is ", b)


choice=int(input("Enter 1 for counting vowels \nEnter 2 for counting words \nEnter 3 for counting unique words : "))
assert choice>0 and choice<=3, 'Enter a valid choice.'


if choice==1:
    vowel_count(x)
elif choice==2:
    word_count(x)
elif choice==3:
    unique_word_count(x)