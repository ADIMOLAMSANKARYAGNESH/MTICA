class Rectangle:
    def __init__(self,length,width):
        assert (length>=0 and width>=0),"Negative values are not acceptable"
        self.length=length
        self.width=width
    def calculateArea(self):
        temp=self.length*self.width
        return temp
    def calculateParameter(self):
        temp=2*(self.length+self.width)
        return temp
l=int(input())
w=int(input())
try:
    ob=Rectangle(l,w)
    area=ob.calculateArea()
    para=ob.calculateParameter()
    print('Area of the rectangle is',area)
    print('Parameter of the rectangle is',para)
except AssertionError as a:
    print(a)

                                                                                                                                                                                                                                                     
