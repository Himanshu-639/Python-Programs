x=int(input("Enter the value of numerator base : "))
n=int(input("Enter the maximum power value of numerator : "))

def sum_of_series_b(x, n):
    sum=1
    for i in range (1,n+1):
        power=x**i
        factorial=1
        for j in range (1, i+1):
            factorial*=j
        series=power/factorial
        sum+=series
    print(sum)
#sum_of_series_b(x, n)


def sum_of_series_a(x,n):
    sum=1
    sub=0
    base=x
    for i in range (2, n+1, 4):
        power=(base)**i
        factorial_1=1
        for j in range (1,i+1):
            factorial_1*=j
        n_terms=power/factorial_1
    sub+=n_terms
    
    for i in range (4, n+1, 4):
        power=(base)**i
        factorial_2=1
        for j in range (1, i+1):
            factorial_2*=j
        p_terms=power/factorial_2
    sum+=p_terms
    print(sub)
    print(sum)
            
            
            
sum_of_series_a(x, n)