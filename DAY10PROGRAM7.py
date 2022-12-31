fo1=open(r"D:\PYTHONPRACTICE65\DAY10\DAY10.txt","r")
fo2=open(r"D:\PYTHONPRACTICE65\DAY10\DAY10(Copy).txt","w+")

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("File copied")
