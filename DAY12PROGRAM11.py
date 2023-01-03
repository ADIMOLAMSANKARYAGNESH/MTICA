class Student:
    CLG_NAME='MTCA'
    COURSE='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def DisplayStudent(self):
        print('Name:',self.name.title(),'\nRoll.No:',self.rollno)
        print('College Name:'+self.CLG_NAME+'\nCourse:'+self.COURSE)
for i in range(2):
    Name=input()
    RollNo=int(input())
    obj=Student(Name,RollNo)
    obj.DisplayStudent()
