d={'a':100,'b':200,'c':300}
if 300 in d.values():
    print("300 present in a dict")
for k,v in d.items():
    if v==300:
        print("For",v,"key is",k)

