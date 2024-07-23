#Ques.2:

file_name=input("Enter the name of file you want to work with (eg:file.txt) : ")

with open(file_name, 'r') as file_in:
    text=file_in.readlines()

with open('File1.txt', 'w') as file_even:
    for i in text[1::2]:
        file_even.write(i)
        
with open('File2.txt', "w") as file_odd:
    for i in text[::2]:
        file_odd.write(i)