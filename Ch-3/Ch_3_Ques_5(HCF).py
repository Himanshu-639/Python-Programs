a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
  
def fn_HCF(a, b):
    if a>b:
        smallest=b
    else:
        smallest=a
        
    while True:
        if a%smallest==0 and b%smallest==0:
            HCF=smallest
            break
        smallest-=1
    return HCF

x=fn_HCF(a, b)
print("The HCF of", a, "and", b, "is : ", x)