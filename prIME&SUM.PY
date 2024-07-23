def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def sum_of_primes(n):
    sum_primes = 0
    prime_numbers = []
    for num in range(2,n+1):
        if is_prime(num):
            sum_primes += num
            prime_numbers.append(num)
    return sum_primes, prime_numbers
n = int(input('Enter the limit:'))
sum_primes, prime_numbers = sum_of_primes(n)
print(f"The sum of prime numbers up to {n} is: {sum_primes}")
print(f"The prime numbers up to {n} are: {prime_numbers}")