a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
  
def fn_LCM(a, b):
    if a>b:
        greater=a
    else:
        greater=b
    
    while True:
        if greater%a==0 and greater%b==0:
            lcm=greater
            break
        greater+=1
    return lcm

print(fn_LCM(a, b))