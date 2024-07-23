
n=int(input("Enter a number :"))
def check_Prime(n):
    if n<=1:
        print("It is not a prime number.")
    elif n<=3:
        print("It is a prime number.")
    elif n%2==0:
        print("It is not a prime number.")
    elif n%3==0:
        print("It is not a prime number.")
    else:
        for i in range(3,n):
            if n%i==0:
                Prime="It is a not prime number."
                break
            elif n%i!=0:
                Prime="It is a prime number."
                break
        print(Prime)
#check_Prime(n)

def prime_till_n(n):
    prime=0
    checked=0
    for i in range (2, n+1):
        print(i, end=" ")
       # while prime<n:
        checked=check_Prime(i)
       # if check_Prime:
        prime+=1
            
#prime_till_n(n)

def n_prime(n):
    i=2
    checked=0
    while checked<n:
        check_Prime(i)
        
        print(i)
        i+=1
        
#n_prime(n)
        


def factorial(n):
    if n<0:
        print("Factorial is not defined for negative number.")
    elif n==0:
        print("1")
    else:
        fac=1
        for i in range(1,n+1):
            fac=fac*i
        print(fac)
#factorial(n)


def table(n):
    for i in range(1,11):
        print(i,"*", n, "=", i*n)
#table(n)


#num=int(input("Enter a number :"))
def generate_Prime(n):
    prime_count=0
    num=2
    while prime_count<n:
        is_prime=True
        for divisor in range (2, int(num**0.5)+1):
            if num%divisor==0:
                is_prime=False
                
            if check_Prime(num):
            print(num)
            prime_count+=1
        num+=1
generate_Prime(n)