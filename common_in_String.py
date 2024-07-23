str1=input("Enter your 1st String :")
str2=input("Enter your 2nd String :")

def overlap(str1, str2):
    for ch in str1:
        for ch in str2:
            str==""
            str3=str(ch)
            if ch in str3:
                continue
            else:
                str3=str(str3)+str(ch)
    print(str3)
            
overlap(str1, str2)