class student():
    def __init__(self, n, a, m):
        self.name=n
        self.age=a
        self.marks=m
    def fndisplay(self):
        print(self.__dict__)
       
        
s1=student("ram", 78, 899)
s2=student("taj", 45, 78)
s3=student('suraj',14,56)
s4=student('raman',15,78)
s5=student('lata',24,99)
s6=student('ramisha',24,89)
s7=student('manisha',23,90)
s8=student('naman', 15,67)
s9=student('chaman', 23,76)
s10=student('ritika',24,67)