class Dog:
    price=500#class attribute,created by assigning variables within the body of the class
    def __init__(self,name,color):
        self.color=color
        self.name=name
    def bark(self):
        print("Woof")
        print(self.name,"has",self.price,"price and its color is",self.color)
if __name__=="__main__":
    pet1=Dog("Tommy","brown")
    pet2=Dog("Sheru","white")
    pet1.bark()
    pet2.bark()
##    print(pet1.price)
##    print(pet2.price)
##    print(Dog.price)
    Dog('ABXYZ','blue').bark()
    
