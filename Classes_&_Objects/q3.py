class Student:
    def __init__(self, rollNum, name, marksList, stream):
        self.rollNum=rollNum
        self.name=name
        self.marksList=marksList
        self.stream=stream

    def setMarks(self, mark1, mark2, mark3, mark4, mark5):
        markList=[mark1, mark2, mark3, mark4, mark5]
        self.marksList=markList

    def getStream(self):
        return self.stream

    def percentage(self):
        total = sum(self.marksList)
        p= total/5
        return p

    def gradeGen(self):
        p=self.percentage()
        if p>=90:
            return 'A'
        elif p>=80:
            return 'B'
        elif p>=65:
            return 'C'
        elif p>=40:
            return 'D'
        else:
            return 'E'

    def division(self):
        p=self.percentage()
        if p>=60:
            return 'I'
        elif p>=50:
            return 'II'
        else:
            return 'III'

    def __str__(self):
        s='Name: '+self.name+'\n Roll No: '+str(self.rollNum)+'\n Stream :'+self.stream+'\n Percentage: '+str(self.percentage())+'\n Grade: '+self.gradeGen()+'\n Division: '+self.division()
        return s
s1 = Student(2729, "Ritik Gupta", [95,98,92,89,99], "CS")
print(s1.division())
