#Que.4:

str_1=input("Enter the first string : ")
str_2=input("Enter the second string. : ")
def swap_str(str_1, str_2):
    swap=str_1[0:3]
    new_str_1=str_1.replace(str_1[0:3], str_2[0:3])
    new_str_2=str_2.replace(str_2[0:3], swap)
    print("The string 1 after swaping first 3 letters withstring 2 : ", new_str_1)
    print("The string 1 after swaping first 3 letters withstring 2 : ", new_str_2)
swap_str(str_1, str_2)