def num_max(num1, num2):
    max=0
    if num1>num2:
        max=num1
    else:
        max=num2
    return max
        
        
num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
max=num_max(num1, num2)
print("Maximum number is :", max)



while True:
    a = input("Continue?: ")
    if a=="yes" or a=="Yes":
        pass
    else:
        break   
    num3=int(input("Enter a number :"))
    num1=max
    num2=num3
    max=num_max(num1, num2)
    print("Maximum number is :", max)
