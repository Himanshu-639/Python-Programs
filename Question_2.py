#Define a function to generate pyramid if number is odd or hollow square if number is even.

n=int(input("Enter a number :"))

#Defining pyramid function
def pyramid(n):
    for i in range(1, n+1):
        spaces=" " * (n-i)
        stars="*" * (2*i-1)
        print(spaces + stars)
    
    for i in range(n-1, 0, -1):
        spaces=" " * (n-i)
        stars="*" * (2*i-1)
        print(spaces + stars)
        

#Defining hollow square function
def hollowSquare(n):
    print("*" * n)
    spaces=" " * (n-2)
    for i in range(2,n):
        print("*" + spaces + "*")
    print("*" * n) 
    
    
#Checking the input number and calling the function
if n%2==0:
    hollowSquare(n)
    
else:
    pyramid(n)