#Exercise questions
#Question 2 of page 80:
#A
total=0
count=20
while count>5:
    total+=count
    count-=1
print(total, "\n")

#B
total=0
N=5
for i in range (1, N+1):
    for j in range (1, i+1):
        total+=1
print(total, "\n")

#C 
total=0
N=10
for i in range (1, N+1):
    for j in range (1, N+1):
        total+=1
print(total, "\n")

#D
total=0
N=5
for i in range (1, N+1):
    for j in range (1, i+1):
        total+=1
    total-=1
print(total, "\n")

#E
total=0
N=5
for i in range (1, N+1):
    for j in range (1, N+1):
        total+=i
print(total, "\n")

#F
total=0
N=5
for i in range (1, N+1):
    for j in range (1, i+1):
        total+=j
print(total, "\n")

#G
total=0
N=5
for i in range (1, N+1):
    for j in range (1, N+1):
        total+= i+j
print(total, "\n")

#H
total=0
N=5
for i in range (1, N+1):
    for j in range (1, i+1):
        for k in range (1, j+1):
            total+=1
print(total, "\n")

#I
num=72958476
a, b = 0, 0
while (num>0):
    digit=num%10
    if (digit % 2 != 0):
        a +=digit
    else:
        b +=digit
    num /=10
print(a, b)