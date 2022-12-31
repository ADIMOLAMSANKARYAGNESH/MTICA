fo=open(r"D:\PYTHONPRACTICE65\DAY10\Day10.txt","a")
for i in range(5):
    inpstr=input("Enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("Written to file")
