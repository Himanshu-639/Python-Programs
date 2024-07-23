num=int(input("Enter a number : "))

def Palindrome_Check(num):
    reversed_num=0
    while num>0:
        digit=num%10
        num=num//10
        reversed_num=(reversed_num*10) + digit
    print(reversed_num)
    if (reversed_num==num):
        print("Yes, It is a Palindrome.")
    #else:
    #    print("No, It is not a Palindrome.")
        
Palindrome_Check(num)