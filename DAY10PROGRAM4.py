def printDetail(name,marks=70,age=22):#default argument
    print("Name:",name)
    print("Marks:",marks)
    print("Age:",age)
    return None
##printDetail()
##printDetail('Yagnesh')
##printDetail('Yagnesh',77)
##printDetail(77,'Yagnesh')
printDetail(marks=77,name='Yagnesh')#keyword argument
