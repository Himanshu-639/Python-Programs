#Ques.3:

class point:
    def __init__(self, x, y):
        self.xcoordinate=x
        self.ycoordinate=y
    def distance(self, p):
        xdist=(self.xcoordinate-p.xcoordinate)**2
        ydist=(self.ycoordinate-p.ycoordinate)**2
        distance=(xdist+ydist)**0.5
        return distance
    
p1=point(3, 6)
p2=point(6, 7)
print(f"The distance between both points is {round(p1.distance(p2), 2)}")