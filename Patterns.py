def star(n):
    for i in range (0, n+1):
        print("*" * i)

def inverseStar(n):
    for i in range (n, 0, -1):
        print("*" * i)
        
def triangle(n):
    for i in range(1, n+1):
        spaces=" " * (n-i)
        stars="*" * (2*i-1)
        print(spaces + stars)

def inverseTriangle(n):
    for i in range(n, 0, -1):
        spaces=" " * (n-i)
        stars="*" * (2*i-1)
        print(spaces + stars)

def hollowSquare(n):
    print("*" * n)
    spaces=" " * (n-2)
    for i in range(2,n):
        print("*" + spaces + "*")
    print("*" * n)    
        
def diamond(n):
    for i in range(1, n+1):
        spaces=" " * (n-i)
        stars="*" * (2*i-1)
        print(spaces + stars)
    
    for i in range(n-1, 0, -1):
        spaces=" " * (n-i)
        stars="*" * (2*i-1)
        print(spaces + stars)
        
def numPattern(num_last=9):
    for i in range (1, num_last):
        print(i, end='')
    for i in range (num_last, 0, -1):
        print(i, end='')

inverseStar(5)        