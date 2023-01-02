def findFrequency(s):
    frequencyDict=dict()
    for i in s:
        if i in frequencyDict:
             frequencyDict[i] +=1
        else:
            frequencyDict[i]=1
    return frequencyDict
def formatOutput(d):
    for i in sorted(d):
        print(i,d[i])
n=int(input())
for i in range(n):
    inpStr=input()
    print(findFrequency(inpStr))

##Output:
##IP 1
##IP Hello World
##{'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}
##IP d={'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}
##IP sorted(d,reverse=True)
##['r', 'o', 'l', 'e', 'd', 'W', 'H', ' ']
##IP sorted(d.items(),key=lambda x:x[1])
##[('H', 1), ('e', 1), (' ', 1), ('W', 1), ('r', 1), ('d', 1), ('o', 2), ('l', 3)]
##IP sorted(d.keys())
##IP sorted(d.values())
##IP for i in sorted(d.items(),key=lambda x:x[1],reverse=True):print(i[0],i[1])
