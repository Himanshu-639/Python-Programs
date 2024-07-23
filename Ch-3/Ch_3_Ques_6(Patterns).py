num=int(input("Enter a number : "))

def fn_a(num):
    for i in range (1, num+1):
        print("")
        for j in range (1, i+1):
            print(j, end=" ")
#fn_a(num)


def fn_c(num):
    for i in range (num, 0, -1):
        for j in range (i, 0, -1):
            print(j, end=" ")
        print()
        
#fn_c(num)

def fn_d(num):
    for i in range (1, num+1):
        for j in range (1, i+1):
            print(j, end=" ")
        print()

#fn_d(num)

def fn_e(num):
    for i in range (0, num):
        spaces= "  " * (i)
        print(spaces, end=" ")
        for j in range(i+1, num+1):
            print( j, end=" ")
        print()
        
#fn_e(num)

def fn_f(num):
    stars= "* " * num
    print(stars)
    spaces= " " * ((2*num)-5)
    for i in range (2, num):
        print("*", spaces, "*")
    print(stars)
    
#fn_f(num)

def fn_g(num):
    for i in range(1, num+1):
        stars= "* " * num
        print(stars)
        
#fn_g(num)

def fn_h(num):
    for i in range (1, num):
        spaces=" " * (num-i)
        stars="*" * i
        rev_stars="*" * (i-1)
        print(spaces, stars, end="")
        print(rev_stars)
    
#fn_h(num)

def fn_i(num):
    starting_stars= "*" * ((2*num)-1)
    print(starting_stars)
    for i in range (0, num-2):
        spaces=" " * (i+1)
        mid_spaces=" " * (num-((2*i)-1))
        print(spaces, end="")
        print("*", end="")
        print(mid_spaces, end="")
        print("*")
        
#fn_i(num)

def fn_j(num):
    for i in range (1, (num)):
        spaces=" " * (i-1)
        stars= "*" * (num-i-1)
        rev_stars= "*" * (num-i)
        print(spaces, stars, end="")
        print(rev_stars)
        
fn_a(num)
        