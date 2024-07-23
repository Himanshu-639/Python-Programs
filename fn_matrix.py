def fnmatrix(m,n):
    my_matrix=[]
    for i in range (m):
        row=[]
        for j in range (n):
            value=int(input("Enter the value at a:"))
            row.append(value)
        my_matrix.append(row)
    for i in my_matrix:
        print("|",end=" ")
        for j in i:
            print(j,end=" ")
        print("|")
fnmatrix(2,2)
#print(a)