import os
file=open("names.txt", "r")

while True:
    name=file.readline()
    if len(name)>6:
        print(name)
    
file.close()