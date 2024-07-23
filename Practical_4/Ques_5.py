#Ques.5:

def email_check():
    while True:
        email=input("Please enter your input (or stop to ends) : ")
        
        if email=="stop":
            break
        
        try:
            assert email.endswith(".com")
            if email.count("@")==0:
                print("Email must contain one @ sign")
            elif email.count("@")>1:
                print("Email can contain only one @")
            else:
                splitted=email.split("@")
                if not splitted[0].isalnum():
                    print("Email can only contain alphabets and digits before @")
                else:
                    a=splitted[1]
                    b=a.split(".")
                    if not b[0].isalpha():
                        print("Email can only contains alphabets between @ and .com")
        except(AssertionError):
            print("Email must ends with .com and have one @ sign")
        finally:
            print()
            
email_check()