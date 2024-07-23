print("\n ***This program gives the sum of digits of number*** \n")

num=int(input("Enter a number : "))
def digit_sum(num):
    sum=0
    while num>0:
        digit=num%10
        sum+=digit
        num=num//10
    print(sum)
        
digit_sum(num)