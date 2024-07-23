#Que.8:

def matrix(n,m):
    mark_matrix=[]
    for i in range (n):
        student_marks=[]
        for j in range (m):
            mark=int(input(f"Enter the mark of student {i+1} in subject {j+1} : "))
            student_marks.append(mark)
        mark_matrix.append(student_marks)
    print(mark_matrix)
    print("The maximum marks obtained in the class is : ", max(student_marks))
    
    
    
    class_total=0
    for k in range (n):
        total_marks=0
        for l in range (m):        
            total_marks+=mark_matrix[k][l]
            avg_marks=(total_marks/m)
        class_total+=avg_marks
        class_avg=(class_total/n)
        marks_dev=(avg_marks - class_avg)
        print("The average mark of student", (k+1), "is : ", avg_marks)
        print("The deviation of student's average marks from class average is : ", marks_dev)
    print("The average mark of the class is : ", class_avg)
    
    
       
            
n=int(input("Enter the number of students : "))
m=int(input("Enter the number of subjects : "))
matrix(n, m)