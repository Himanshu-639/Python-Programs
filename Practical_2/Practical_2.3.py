num=int(input("Enter a number to find its reverse:"))

def reverse_and_diff(num):
    rev_num=0
    original_num=num
    
    while num>0:
        rem=num%10
        rev_num=rev_num*10+rem
        num=num//10
        diff=rev_num-original_num
    print("Reverse num is :", str(rev_num))
    print("Difference is :", str(diff))
    
    
reverse_and_diff(num)

