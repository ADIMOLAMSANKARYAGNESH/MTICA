s1={10,20}#{30}
s2={30,40,50,60,70}
if s1.isdisjoint(s2):
    print("Two sets have no common items")
else:
    print("Two sets have common items")
    print(s1.intersection(s2))
