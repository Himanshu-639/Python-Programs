#Define a function for generating number pattern

num_last=input("Enter the last number :")
num_last=int(num_last)
def numPattern(num_last=9):
    #Generating sequence
    for i in range (1, num_last):
        print(i, end='')
    #Generating inverse sequence
    for i in range (num_last, 0, -1):
        print(i, end='')

numPattern(num_last)      