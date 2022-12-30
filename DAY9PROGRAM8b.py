def printDay(dn):
    mn=''
    if(dn==0):
        mn= 'Sunday'
    elif(dn==1):
        mn= 'Monday'
    elif(dn==2):
        mn= 'Tuesday'
    elif(dn==3):
        mn= 'Wednesday'
    elif(dn==4):
        mn= 'Thursday'
    elif(dn==5):
        mn= 'Friday'
    elif(dn==6):
        mn= 'Saturday'
    else:
        mn= 'Invalid'
    return mn
def printDay1(dn):
    mn=''
    if(dn==0):
        mn= 'Sunday'
    elif(dn==1):
        mn= 'Monday'
    elif(dn==2):
        mn= 'Tuesday'
    elif(dn==3):
        mn= 'Wednesday'
    elif(dn==4):
        mn= 'Thursday'
    elif(dn==5):
        mn= 'Friday'
    elif(dn==6):
        mn= 'Saturday'
    else:
        mn= 'Invalid'
    return mn
import time
for i in range(8):
    inpNum=int(input())
    start=time.time()
    print(printDay(inpNum))
    print((time.time()-start)*10000)
    start=time.time()
    print(printDay1(inpNum))
    print((time.time()-start)*10000)
