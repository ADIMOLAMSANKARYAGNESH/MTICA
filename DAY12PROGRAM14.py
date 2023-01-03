class Circle:
    pi=22/7
    def __init__(self,radius):
        self.radius=radius
    def calculateArea(self):
        temp=self.pi*self.radius**2
        return temp
    def calculateParameter(self):
        temp=2*self.pi*self.radius
        return temp
r=int(input())
ob=Circle(r)
area=ob.calculateArea()
para=ob.calculateParameter()
print('Area of the circle with radius',r,'is',area)
print('Parameter of the circle with radius',r,'is',para)

                                                                                                                                                                                                                                                     
