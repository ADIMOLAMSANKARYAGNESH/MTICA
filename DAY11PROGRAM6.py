d={
    "name":"Yagnesh",
    "age":22,
    "salary":30000,
    "city":"PGR"}
keys=["name","salary"]
dict={}
for i in keys:
    dict[i]=d[i]
print(dict)
##dict={i:d[i]for i in keys}
##print(dict)

####d={
####    "name":"Yagnesh",
####    "age":22,
####    "salary":30000,
####    "city":"PGR"}
####keys=["name","salary"]
####res=dict()
####for k in keys:
####    res.update({k:d[k]})
####print(res)
