#Asking for choice
choice = int(input("Press 1 to check if n is prime. Press 2 to generate all prime numbers till n. /  Press 3 to Generate first n prime numbers. Press 4 to Find factorial of the number n. Press 5 to calculate table of number n :"))
assert choice==1 or choice==2 or choice==3 or choice==4 or choice==5, "Please enter a valid choice."

n=int(input("Enter a number :"))

#Defining Prime number checker function
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


#Defining a function to generate prime numbers till 'n'
def  prime_till_n(n):
    for num in range (2, n+1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')
            
            
#Defining a function to generate n primes.
def generate_primes(n):
    prime_count = 0
    num = 2 
    while prime_count < n:
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')
            prime_count += 1
        num += 1


#Defining factorial function
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
        
        
#Defining table function       
def table(n):
    for i in range(1,11):
        print(i,"*", n, "=", i*n)
        

                    
#Calling function according to choice                   
if choice==1:
    check_Prime(n)
elif choice==2:
    prime_till_n(n)
elif choice==3:
    generate_primes(n)
elif choice==4:
    factorial(n)
elif choice==5:
    table(n)