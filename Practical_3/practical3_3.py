#Que.3:

str=input("Enter your string :")

def count_word(str):
    target_word=input("Enter the character to count the frequency :")
    count=0
    for char in str:
        if char==target_word:
            count+=1
    return count
    
def replace_fn(str):
    original_word=input("Enter the you want to replace :")
    assert original_word in str, "word is not in string"
    replacing_word=input("Enter the word to be replaced with :")
    new_str=str.replace(original_word, replacing_word)
    print(new_str)

def remove(str):
    ch_to_remove=input("Enter the character to remove :")
    new_str=str.replace(ch_to_remove, '', 1)
    print(new_str)

def remove_all(str):
    ch_to_remove=input("Enter the character to remove :")
    new_str=str.replace(ch_to_remove, '')
    print(new_str)


choice=int(input("Enter 1 for counting frequency of a character in given string \nEnter 2 for replacing a character \nEnter 3 for removing the first occurance of character from the string \nEnter 4 for removing all the occurance of character from the string : "))
assert choice>0 and choice<=4, 'Enter a valid choice.'

if choice==1:
    freq=count_word(str)
    print(freq)
elif choice==2:
    replace_fn(str)
elif choice==3:
    remove(str)
elif choice==4:
    remove_all(str)
    

