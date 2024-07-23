set1=set(input("Enter your input"))
for i in range(1,4):
    if (len(set1))<=0:
        break
    print("{ ",",",end="")
for k in set1:
    print({k},end="")
x=set([(l)for l in set1])
print(x,"}")