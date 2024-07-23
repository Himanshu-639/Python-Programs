def cubed(L):
    newL=[i**3 for i in L if str(i).isdigit() and i%2==0]
    return newL
print(cubed([11,4,2,5,"a","c,d","adad",12]))