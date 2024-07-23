num=int(input("Enter a number :"))
def odd_Even(num):
    
    while num!=0:
        if num%2==0:
            print("It is an even number.")
        else:
            print("It is an odd number.")
        num=int(input("Enter a number :"))
odd_Even(num)      


num = int(input("Enter a number :"))
greatest = 0
def find_greatest(num):
    global greatest
    while True:
        num = input("Enter a number :")
        if num==" ":
            break
        num = int(num)
        if num > greatest:
            greatest = num
    print("Greatest :", greatest)
      
find_greatest(num)
#print("Greatest :" + greatest)