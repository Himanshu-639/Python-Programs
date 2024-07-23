from os import system
system('clear')

print("\n")
print(" *** This program is to store the names of students in a file. *** ")
print("\n")

def fnwrite():
    
    fname=input("Enter the name of file you want to create (eg: filename.txt ) : ")
    
    file=open(fname, "w")
    rfile=open(fname, "r")
    
    while True:
        reply=input("Enter the name of student (stop to ends and save the file) :" )
        
        if reply=="stop":
            file.close()
            break
    
        try:
            splitted=reply.split( )
            without_spaces=reply.replace(" ", "")
            assert (without_spaces.isalpha())
            name=reply.title()
            
            if (len(splitted[0]))>2:
                file.write(name)
                file.write("\n")
                print(name, "is added to the file")
        
            elif (len(splitted[0]))<=2:
                print("*** It doesnot seems as a name!!! ***")
                        
        except (AssertionError):
            print("Names only contain alphabets.")
                
        finally:
            print("Done")
           
    file.close()
    rfile.close()




            

def fnappend():

    fname=input("Enter the name of file you want to append (eg. file1.txt) : ")

    file=open(fname, "a")

    while True:
        reply=input("Enter the name of student (stop to ends and save the file) :" )
        
        if reply=="stop":
            file.close()
            break

        try:
            splitted=reply.split( )
            without_spaces=reply.replace(" ", "")
            assert (without_spaces.isalpha())
            name=reply.title()

            if (len(splitted[0]))>2:
                file.write(name)
                file.write("\n")
                print(name, "is added to the file")

            elif (len(splitted[0]))<=2:
                print("*** It doesnot seems as a name!!! ***")
                        
        except (AssertionError):
            print("Names only contain alphabets.")
                
        finally:
            print("Done")
    file.close()



choice=int(input("Enter 1 to create a new file \nOR Enter 2 to append existing file : "))
assert (choice==1) or (choice==2), "Please enter a valid choice !"
if choice==1:
    fnwrite()
elif choice==2:
    fnappend()
print("\n")