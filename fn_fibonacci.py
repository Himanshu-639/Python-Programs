def fnfibo(n):
    assert n>=0, "Please Enter a Positive Number"
    n_list=[]
    n1=0
    n2=1
    if n==1:
        n_list.append(n1)
    elif n==2:
        n_list.append(n1)
        n_list.append(n2)
    else:
        n_list.append(n1)
        n_list.append(n2)
        for i in range(n-2):
            n3=n1+n2
            n_list.append(n3)
            n1=n2
            n2=n3
    return n_list
n=int(input("Enter a number to generate Fibonacci Series :"))
a=fnfibo(n)
print(a)