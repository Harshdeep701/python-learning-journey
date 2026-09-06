class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def sum(self,p):
        return point(self.x+p.x,self.y+p.y)
    
    def print_point(self):
        print( f"x is {self.x} and y is {self.y} ")
p1= point(3,2)
p2=point(4,6)

p=p1.sum(p2) # returing a new point which is sum of p1 and p2 
p.print_point()