#Que.7:

def list_check():
    user_input=[]
    size=int(input("Enter the number of input you wants to enter :"))

    for i in range (size):
        data=input("Enter the element :")
        user_input.append(data)
    print(user_input)
    sum=0
    for i in range (size):
        if user_input[i].isdigit():
            result=1
        elif user_input[i].isalpha():
            result=0
        else:
            result=-1
        
        
        if result==1:
            num=int(user_input[i])
        sum+=num
    print(sum)
        #if result==0:
         #   str=str(user_input[i])
            
    
list_check()