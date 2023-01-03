class Student:
    CLG_NAME='MTCA'
    COURSE='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def DisplayStudent(self):
        print('Name:',self.name.title(),'\nRoll.No:',self.rollno)
        print('College Name:'+self.CLG_NAME+'\nCourse:'+self.COURSE)
lstObj=[]
for i in range(2):
    Name=input()
    RollNo=int(input())
    temp='obj'+str(i)
    temp=Student(Name,RollNo)
    lstObj.append(temp)
for i in lstObj:
    i.DisplayStudent()
