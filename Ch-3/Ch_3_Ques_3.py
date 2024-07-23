print("\n \n *** This Program is to check if a number is perfect number *** \n \n")

def perfect_num():
    while True:
        divisor_sum=0
        num=int(input("Enter a number (stop to ends) : "))
        if num=="stop":
            break
        else:
            for i in range (1, ((num//2)+1)):
                if ((num%i)==0):
                    divisor_sum+=i
            if num==divisor_sum:
                print("It is a perfect number.")
            else:
                print("It is not a perfect number.")
            
perfect_num()
