#Que.5:

str1=input("Enter the first string : ")
str2=input("Enter the second string : ")

def str_indices(str1, str2):
    indices=[]
    start=0
    while start < len(str1):
        index=str1.find(str2, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1
    return indices
        
a=str_indices(str1, str2)
print(a)