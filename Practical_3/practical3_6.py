#Que.6:

user_input = []
size = int(input("Enter the number of elements you want to input: "))

for i in range(size):
    temp = input("Enter the element: ")
    user_input.append(temp)
print(user_input)

for i in user_input:
    if i.isdigit():
        j=int(i)
        if j%2==0:
            print("The even integers in the given inputs are : ", j)
            print("The cube of", j, "is : ", j**3)