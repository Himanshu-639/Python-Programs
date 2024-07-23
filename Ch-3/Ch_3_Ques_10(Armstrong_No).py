num=int(input("Enter a number : "))

def armstrong(num):
    digit=0
    sum=0
    while num>0:
        digit=num%10
        num=num//10
        sum+=(digit)**3
    print(sum)
    
    if (num==sum):
        print("Yes")
    
armstrong(num)