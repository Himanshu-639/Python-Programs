str=input("Enter a string :")

def string_Check(str):
    if str.isdigit():
        result=1
    elif str.isalnum():
        result=-1
    else:
        a=str.split(".")
        if len(a)==2:
            if a[0].isdigit() and a[1].isdigit():
                result=1
            else:
                result=2
        else:
            result=2
    print(result)
    
string_Check(str)

            