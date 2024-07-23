

import math
def primeCheck(n):
    if n == 2:
        print("Number is Prime")
        return True
    elif n%2 == 0:
        print("Number is Not prime")
        return False  
    x = math.sqrt(n)
    for i in range(2,math.ceil(x)+1):
        if n%i == 0:
            print("Number is Not prime")
            return False   
        else:
            print("Number is Prime")
            return True
            
n=int(input("A"))         
#primeCheck(n)

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

#generate_primes(n)


def  generate_primes(n):
    for num in range (2, n+1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end=' ')
            
        

generate_primes(n)


