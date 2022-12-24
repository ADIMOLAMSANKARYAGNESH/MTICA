def interchange(n):
    n=str(n)
    n=n.replace('3','.')
    n=n.replace('5','3')
    n=n.replace('.','5')
    return n
int=input()
print(interchange(int))
