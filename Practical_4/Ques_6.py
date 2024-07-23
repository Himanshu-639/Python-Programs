#Ques.6 :

with open('student.txt', "w") as file_w:
    
    n=int(input("Enter the number of students : "))
    try:
        lst_name=[]
        lst_marks=[]
        for i in range (1, n+1):
            name=input("Enter the name of student : ")
            assert name.isalpha()
            name=name.title()
            lst_name.append(name)
            file_w.writelines(name)
            marks=(int(input("Enter the percentage obtained by student :")))
            assert 0<=marks<=100, 'Marks Percentage can only lie between 0 and 100.'
            lst_marks.append(marks)
            file_w.writelines(f" {str(marks)}% \n")
            
    except(AssertionError, ValueError):
        print("Name only contains alphabets")
        
with open('student.txt', "r") as file_r:
    try:
        for i in range (0, len(lst_name)):
            if lst_marks[i]>70:
                final_name=lst_name[i]
                final_student=(final_name)
                print(final_name)
    except(IndexError):
        print()    
