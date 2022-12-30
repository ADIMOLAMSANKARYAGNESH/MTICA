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
for i in range(2):
    inpNum=int(input())
    print(printMonth(inpNum))
