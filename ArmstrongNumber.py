import math
def checkarmstrongnumber(num):
    num=str(num)
    n=len(num)
    total=0
    for i in num:
        total +=int(i)**n
    if int(num)==total:
        return 1
    else:
        return 0
intNum=input()
if checkarmstrongnumber(intNum):
    print(intNum,"is a armstrong number")
else:
    print(intNum,"is not a armstrong number")

