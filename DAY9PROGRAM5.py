def printSeries(n):
    for i in range(1,n+1):
        num=1
        print()
        for j in range(i):
            print(num,end=' ')
    return None
inp=int(input("Enter a number:"))
printSeries(inp)
